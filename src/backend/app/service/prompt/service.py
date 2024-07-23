import asyncio
from decimal import Decimal
import json
from langchain_core.documents import Document
from sqlalchemy.orm import aliased
import os
from typing import Dict, List, Optional
import openai
import tiktoken
from fastapi import HTTPException
from langchain_openai import OpenAIEmbeddings
from sqlmodel import Session, select
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter
from uuid import UUID
import logging
from app.components.Embedding.Bedrock import BedrockEmbeddingComponent
from app.components.Embedding.OpenAI import OpenAIEmbeddingComponent
from app.service.agent.model import Agent
from langchain.chains import RetrievalQA
from app.service.chat.service import ChatService
from app.service.model.model import Model
from app.service.store.model import Store
from app.service.provider.model import Provider
from app.components.LLM.OpenAI import OpenAILLMComponent
from app.components.Chat.OpenAI import ChatOpenAIComponent
from app.components.Chat.Bedrock import ChatBedrockComponent
from app.components.LLM.Bedrock import BedrockLLMComponent
from app.core.util.token import TokenUtilityService
from app.api.v1.schemas.chat import ChatResponse
from app.service.store.service import StoreService
from ddtrace.llmobs.decorators import workflow
from ddtrace.llmobs import LLMObs
from app.core.util.logging import LoggingConfigurator
from app.service.processing.model import Processing
from app.core.util.piimasking import PiiMaskingService
from app.core.util.textNormailization import TextNormalizationService
from app.service.credential.model import Credential
from app.core.provider.aws.SecretManager import SecretManagerService
from app.components.VectorStore.Chroma import ChromaVectorStoreComponent
from app.components.VectorStore.Pinecone import PineconeVectorStoreComponent
from app.service.credential.service import CredentialService
from app.components.VectorStore.Faiss import FaissVectorStoreComponent


class PromptService:
    def __init__(self, session: Session):
        self.session = session

    @workflow(name="cloudwiz-ai-fmops")
    @LoggingConfigurator.log_method
    def get_prompt(self, agent_id: UUID, query: Optional[str] = None) -> ChatResponse:

        response = []

        try:
            agent_data = self._get_agent_data(agent_id)
            _d_agent = agent_data['Agent']

            # check limit
            _d_credential = agent_data['Credential']
            limit_response = self._check_limit_token(_d_agent, _d_credential)
            if limit_response:
                return limit_response

            # verify                
            self._verify_query(agent_data)

            # get history
            history = self._get_history(agent_id)

            # pre-processing
            if _d_agent.processing_enabled:
                query = self._preprocess_query(agent_data, query)

            # template
            if _d_agent.template_enabled:
                query = self._replace_question(_d_agent.template, query)

            # embedding
            if _d_agent.embedding_enabled:

                # check storage limit
                store_data = agent_data['Store']
                user_id = _d_agent.user_id
                storage_limit_response = self._check_storage_limit(user_id, store_data)
                if storage_limit_response:
                    return storage_limit_response
                        
                try:
                    # documents = asyncio.run(self._run_embedding(agent_data, query))
                    documents = asyncio.run(self._run_embedding_main(agent_data))
                    
                    if agent_data["Provider"].name == "OpenAI":
                        rag_response = asyncio.run(self.run_rag_openai(agent_data, query, documents))
                    elif agent_data["Provider"].name == "Bedrock":
                        rag_response = asyncio.run(self.run_rag_bedrock(agent_data, query, documents))
                    else:
                        raise ValueError("Unsupported embedding provider")

                    response = rag_response["llm_response"]
                except openai.PermissionDeniedError as e:
                    logging.error(f"Embedding generation permission denied: {str(e)}")
                    raise HTTPException(status_code=403, detail="Embedding generation permission denied")
            else:
                response = self._run_provider(agent_data, query, history)

            # post-processing
            if _d_agent.processing_enabled:
                response = self._postprocess_response(agent_data, response)

            # set history
            history = self._set_history(agent_id)

            # tokens, cost
            tokens = self._get_token_counts(agent_id, query, response)

            LLMObs.annotate(
                span=None,
                input_data=query,
                output_data=response,
                tags={"host":_d_agent.agent_id, "result": "success"}
            )
                
            return ChatResponse(
                        answer=response,
                        tokens=tokens['token_counts'],
                        cost=tokens['total_cost']
                    )

        except Exception as e:
            LLMObs.annotate(
                span=None,
                input_data=query,
                output_data=response,
                tags={"host":_d_agent.agent_id, "result": "fail", "error": e}
            )            
            raise HTTPException(status_code=500, detail=str(e))

    def _get_agent_data(self, agent_id: UUID):
        EmbeddingModel = aliased(Model)
        statement = (
            select(
                Agent, Model, Credential, Provider, Store,
                EmbeddingModel.model_name.label('embedding_model_name'),
                Provider.name.label('embedding_provider_name')
            )
            .join(Model, Agent.fm_model_id == Model.model_id)
            .join(Credential, Agent.fm_provider_id == Credential.credential_id)
            .join(Provider, Credential.provider_id == Provider.provider_id)
            .join(Store, Agent.storage_object_id == Store.store_id)
            .outerjoin(EmbeddingModel, Agent.embedding_model_id == EmbeddingModel.model_id)
        )
        statement = statement.where(Agent.agent_id == agent_id)

        result = self.session.execute(statement).first()

        if not result:
            raise HTTPException(status_code=404, detail="Agent not found")

        agent_data, model_data, credential_data, provider_data, store_data, embedding_model_name, embedding_provider_name = result

        return {
            "Agent": agent_data,
            "Model": model_data,
            "Credential": credential_data,
            "Provider": provider_data,
            "Store": store_data,
            "EmbeddingModelName": embedding_model_name,
            "EmbeddingProviderName": embedding_provider_name
        }
    
    def _get_processing_data(self, processing_id: UUID):

        statement = select(Processing).where(Processing.processing_id == processing_id)
        result = self.session.execute(statement).first()

        if not result:
            raise HTTPException(status_code=404, detail="Agent not found")

        return result
    
    def _check_limit_token(self, _d_agent, _d_credential) -> Optional[ChatResponse]:
        if _d_credential.inner_used:
            if _d_agent.expected_token_count > _d_credential.limit_cnt:
                return ChatResponse(
                        answer="Token usage limits. Please ask your system administrator.",
                        tokens=0,
                        cost=0
                    )
        return None
    
    def _check_storage_limit(self, user_id, store_data) -> Optional[ChatResponse]:

        directory_name = store_data.store_name
        credential_id = store_data.credential_id

        service = StoreService(self.session)
        storage_info = service.get_store_directory_info(user_id, directory_name, credential_id)
        total_size = storage_info.get('total_size', 0)

        credential = self.session.get(Credential, store_data.credential_id)
        if not credential:
            raise HTTPException(status_code=404, detail="Credential not found")
        
        if total_size > credential.limit_cnt:
            return ChatResponse(
                answer="Storage size limits exceeded. Please contact your system administrator.",
                tokens=0,
                cost=0
            )
        return None

    def _get_history(self, agent_id: UUID):
        # Logic to retrieve history
        return None

    def _set_history(self, agent_id: UUID):
        # Logic to retrieve history
        return None

    def _verify_query(self, agent_data):
        pass

    def _parse_options(self, data: str) -> Dict[str, bool]:
        options = data.split('|')
        return {option: True for option in options}

    def _convert_list(self, data: str) -> List[str]:
        return data.split('|')

    def _replace_question(self, template: str, question: str) -> str:
        return template.format(question=question)

    def _preprocess_query(self, agent_data, query: str):

        _d_agent = agent_data['Agent']
        pre_processing_id = _d_agent.pre_processing_id
        processing_data = self._get_processing_data(pre_processing_id)[0]

        # pii mask
        if processing_data.pii_masking:
            pii_options = self._parse_options(processing_data.pii_masking)
            pii_masking_service = PiiMaskingService()
            query = pii_masking_service.mask_pii(query, pii_options)

        # normalize text
        if processing_data.normalization:
            normalize_options = self._parse_options(processing_data.normalization)
            text_normalization_service = TextNormalizationService()
            query = text_normalization_service.normalize_text(query, normalize_options)

        # stopword removal
        if processing_data.stopword_removal:
            stopwords = set(self._convert_list(processing_data.stopword_removal))
            for stopword in stopwords:
                query = query.replace(stopword, '')

        return query

    def split_text_into_chunks(self, text, max_tokens, model_name='cl100k_base'):
        try:
            encoding = tiktoken.get_encoding(model_name)
        except KeyError:
            logging.warning(f"Warning: model {model_name} not found. Using cl100k_base encoding.")
            encoding = tiktoken.get_encoding("cl100k_base")

        tokens = encoding.encode(text)

        chunks = []
        for i in range(0, len(tokens), max_tokens):
            chunk_tokens = tokens[i:i + max_tokens]
            chunks.append(encoding.decode(chunk_tokens))
        return chunks

    async def _run_embedding_main(self, agent_data):
        store = agent_data['Store']
        agent = agent_data['Agent']

        credential_service = CredentialService(self.session)
        store_service = StoreService(self.session)
        
        storage_service = credential_service._set_storage_credential(credential_id=store.credential_id)
        if not storage_service:
            logging.error("Failed to initialize storage service")
            raise HTTPException(status_code=500, detail="Failed to initialize storage service")

        vector_store_type = store_service.get_provider_info(agent.vector_db_provider_id)
        if vector_store_type == "FS":
            return await self._run_embedding_faiss(agent_data)
        elif vector_store_type == "CM":
            return await self._run_embedding_chroma(agent_data)
        elif vector_store_type == "PC":
            return await self._run_embedding_pinecone(agent_data)
        else:
            return await self._run_embedding_faiss(agent_data)
    
    def get_embedding_credential(self, credential_id: UUID):
        try:
            statement = (
                select(Credential).where(Credential.credential_id == credential_id)
            )
            provider = self.session.execute(statement).one_or_none()

            if provider is None:
                raise HTTPException(status_code=404, detail="Store not found")
            
            return provider[0].pvd_key

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error retrieving store: {str(e)}")        
            
    async def _run_embedding_faiss(self, agent_data):
        """
        Run the embedding process using FAISS.
        
        Args:
            agent_data (Dict[str, Any]): Dictionary containing agent-related data.
        
        Returns:
            Any: The FAISS engine or an error message.
        """
        store_service = StoreService(self.session)

        try:
            agents_store = agent_data['Agent']
            storage_store = agent_data['Store']
            embedding_model_name = agent_data['EmbeddingModelName']

            # Load Object
            file_metadata_list = store_service.list_files(storage_store.user_id, storage_store.store_id)
            files = [file_metadata['Key'] for file_metadata in file_metadata_list]

            # Load Document
            documents = store_service.load_documents_v2(storage_store.credential_id, files)

            # Make Chunks
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            chunks = text_splitter.split_documents(documents)

            # Credential Type
            embedding_type = store_service.get_provider_info(agents_store.embedding_provider_id)
            embed_component = self._initialize_embedding_component(embedding_type, agent_data)

            embed_component.build(embedding_model_name)
            embeddings = await embed_component.run_embed_documents([doc.page_content for doc in chunks])
            docs_with_embeddings = [
                Document(page_content=doc.page_content, metadata={"embedding": embedding})
                for doc, embedding in zip(documents, embeddings)
            ]
            engine = await FAISS.afrom_documents(docs_with_embeddings, embed_component.model_instance)

            return engine
        except Exception as e:
            logging.error(f"An error occurred during the FAISS embedding process: {e}")
            return f"An error occurred: {e}"

    def _initialize_embedding_component(self, embedding_type: str, agent_data):
        """
        Initialize the embedding component based on the embedding type.
        
        Args:
            embedding_type (str): Type of embedding provider (e.g., "OA" for OpenAI, "BR" for Bedrock).
            agent_data (Dict[str, Any]): Dictionary containing agent-related data.
        
        Returns:
            Any: The initialized embedding component.
        
        Raises:
            ValueError: If required credentials are missing.
        """
        if embedding_type == "OA":
            openai_api_key = self._get_credential_info(agent_data, "OPENAI_API_KEY")
            if not openai_api_key:
                raise ValueError("OpenAI API key is not set in the provider information.")
            return OpenAIEmbeddingComponent(openai_api_key)

        elif embedding_type == "BR":
            aws_access_key = self._get_credential_info(agent_data, "AWS_ACCESS_KEY_ID")
            aws_secret_access_key = self._get_credential_info(agent_data, "AWS_SECRET_ACCESS_KEY")
            aws_region = self._get_credential_info(agent_data, "AWS_REGION")
            if not all([aws_access_key, aws_secret_access_key, aws_region]):
                raise ValueError("AWS credentials or region are not set in the provider information.")
            return BedrockEmbeddingComponent(aws_access_key, aws_secret_access_key, aws_region)
        
        else:
            raise ValueError(f"Unsupported embedding type: {embedding_type}")
        
    async def _run_embedding_chroma(self, agent_data):
        """
        Load the Chroma engine for querying.
        
        Args:
            agent_data (Dict[str, Any]): Dictionary containing agent-related data.
        
        Returns:
            Any: The Chroma engine or an error message.
        """    
        store_service = StoreService(self.session)
        credential_service = CredentialService(self.session)

        try:            
            agents_store = agent_data['Agent']
            storage_store = agent_data['Store']
            embedding_model_name = agent_data['EmbeddingModelName']

            # Load Object
            file_metadata_list = store_service.list_files(storage_store.user_id, storage_store.store_id)
            files = [file_metadata['Key'] for file_metadata in file_metadata_list]

            # Load Document
            documents = store_service.load_documents_v2(storage_store.credential_id, files)

            # Make Chunks
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            chunks = text_splitter.split_documents(documents)

            storage_service = credential_service._set_storage_credential(credential_id=storage_store.credential_id)
            if not storage_service:
                logging.error("Failed to initialize storage service")
                raise HTTPException(status_code=500, detail="Failed to initialize storage service")

            embedding_type = store_service.get_provider_info(agents_store.embedding_provider_id)
            embed_component = self._initialize_embedding_component(embedding_type, agent_data)
            embed_component.build(embedding_model_name)

            persist_directory = f"./chroma_db/{storage_store.store_id}"
            storage_location = f"{storage_store.user_id}/chroma_indexes/{storage_store.store_id}"
            chroma_component = ChromaVectorStoreComponent(storage_service=storage_service)
            # chroma_component.initialize(docs=chunks, embedding_function=embed_component.model_instance, persist_directory=persist_directory, index_name=str(storage_store.store_id), storage_location=storage_location)
            # chroma_component.save_index(storage_location)
            chroma_component.embedding_function = embed_component.model_instance
            chroma_component.load_index(storage_location, persist_directory)

            if chroma_component.db:
                logging.warning("Database initialized successfully.")
            else:
                logging.warning("Database initialization failed.")

            return chroma_component.db
        except Exception as e:
            logging.error(f"An error occurred while loading the Chroma engine: {e}")
            return f"An error occurred: {e}"

    async def _run_embedding_pinecone(self, agent_data):
        pass

    async def _run_embedding(self, agent_data, query):

        store_service = StoreService(self.session)

        storage_store = agent_data['Store']
        store_id = storage_store.store_id
        user_id = storage_store.user_id

        file_metadata_list = store_service.list_files(user_id, store_id)
        files = [file_metadata['Key'] for file_metadata in file_metadata_list]

        if not files:
            logging.error("No files found in storage Object")
            raise HTTPException(status_code=500, detail="No files found in storage object")

        documents = store_service.load_documents_v2(storage_store.credential_id, files)

        if not documents:
            logging.error("No documents found in files")
            raise HTTPException(status_code=500, detail="No documents found in files")

        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        chunks = text_splitter.split_documents(documents)

        if not chunks:
            raise ValueError("No chunks were split into chunks")

        if agent_data["Provider"].name == "OpenAI":
            return await self._run_embedding_openai_model(agent_data, chunks)
        elif agent_data["Provider"].name == "Bedrock":
            return await self._run_embedding_bedrock_model(agent_data, chunks)
        else:
            return await self._run_embedding_openai_model(agent_data, chunks)

    def _run_provider(self, agent_data, query, history):

        _d_provider = agent_data['Provider']

        if _d_provider.name == "OpenAI":
            return self._run_openai_model(agent_data, query)
        elif _d_provider.name == "Bedrock":
            return self._run_bedrock_model(agent_data, query)
        else:
            return self._run_openai_model(agent_data, query)

    async def _run_embedding_openai_model(self, agent_data, documents):
        store = agent_data['Store']
        agent = agent_data['Agent']
        embedding_model_name = agent_data['EmbeddingModelName']

        credential_service = CredentialService(self.session)
        store_service = StoreService(self.session)

        openai_api_key = self._get_credential_info(agent_data, "OPENAI_API_KEY")

        if not openai_api_key:
            return "OpenAI API key is not set in the provider information."
        
        storage_service = credential_service._set_storage_credential(credential_id=store.credential_id)
        if not storage_service:
            logging.error("Failed to initialize storage service")
            raise HTTPException(status_code=500, detail="Failed to initialize storage service")

        vector_store_type = store_service.get_provider_info(agent.vector_db_provider_id)
        if vector_store_type == "CM":
            
            embed_component = OpenAIEmbeddingComponent(openai_api_key)
            embed_component.build(embedding_model_name)
            embeddings = await embed_component.run_embed_documents([doc.page_content for doc in documents])

            docs_with_embeddings = [Document(page_content=doc.page_content, metadata={"embedding": embedding}) for doc, embedding in zip(documents, embeddings)]

            db = await FAISS.afrom_documents(docs_with_embeddings, embed_component.model_instance)

        elif vector_store_type == "FS":
            persist_directory = f"/tmp/chroma_db/{store.store_id}"
            storage_location = f"{store.user_id}/chroma_indexes/{store.store_id}"

            os.makedirs(persist_directory, exist_ok=True)

            vector_store = ChromaVectorStoreComponent(storage_service=storage_service)
            vector_store.load_index(storage_location, persist_directory)
            db = vector_store.db

        elif vector_store_type == "PC":
            vector_store = PineconeVectorStoreComponent()
            vector_store.initialize(index_name=str(store.store_id))
            db = vector_store

        else:
            raise ValueError(f"Unsupported vector store type: {vector_store_type}")

        return db

    async def run_rag_openai(self, agent_data, query: str, db, top_k: int = 5):
        try:
            _d_agent = agent_data['Agent']
            _d_model = agent_data['Model']
            
            logging.info(f"FAISS database created")
            matching_docs = db.similarity_search(query, k=top_k)
            logging.info(f"Matching documents: {matching_docs}")

            if not matching_docs:
                raise ValueError("No matching documents found")

            retriever = db.as_retriever()

            openai_api_key = self._get_credential_info(agent_data, "OPENAI_API_KEY")
            
            if not openai_api_key:
                return "OpenAI API key is not set in the provider information."
                    
            if _d_agent.fm_provider_type == "T":
                openai_component = OpenAILLMComponent(openai_api_key)
                openai_component.build(
                    model_id=_d_model.model_name,
                    temperature=_d_agent.fm_temperature,
                    top_p=_d_agent.fm_top_p,
                    max_tokens=_d_agent.fm_response_token_limit
                )
            elif _d_agent.fm_provider_type == "C":
                openai_component = ChatOpenAIComponent(openai_api_key)
                openai_component.build(
                    model_id=_d_model.model_name,
                    temperature=_d_agent.fm_temperature,
                    max_tokens=_d_agent.fm_response_token_limit
                )
            else:
                openai_component = OpenAILLMComponent(openai_api_key)
                openai_component.build(
                    model_id=_d_model.model_name,
                    temperature=_d_agent.fm_temperature,
                    top_p=_d_agent.fm_top_p,
                    max_tokens=_d_agent.fm_response_token_limit
                )

            llm_instance = openai_component.model_instance
            logging.info(f"LLM instance created")

            qa_chain = RetrievalQA.from_chain_type(llm=llm_instance, chain_type="stuff", retriever=retriever)
            inputs = {"query": query, "input_documents": matching_docs}
            try:
                answer = await asyncio.to_thread(qa_chain.invoke, inputs)
                result = answer['result'] if 'result' in answer else answer
                logging.info(f"Generated answer: {result}")
            except Exception as e:
                logging.error(f"Error generating response from QA chain: {str(e)}")
                result = "Error generating response from QA chain"

            return {
                "matching_documents": matching_docs,
                "llm_response": result
            }

        except Exception as e:
            logging.error(f"Exception in run_rag_openai: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))


    async def _run_embedding_bedrock_model(self, agent_data, documents):
        _d_agent = agent_data['Agent']
        embedding_model_name = agent_data['EmbeddingModelName']

        aws_access_key = self._get_credential_info(agent_data, "AWS_ACCESS_KEY_ID")
        aws_secret_access_key = self._get_credential_info(agent_data, "AWS_SECRET_ACCESS_KEY")
        aws_region = self._get_credential_info(agent_data, "AWS_REGION")

        if not all([aws_access_key, aws_secret_access_key, aws_region]):
            return "AWS credentials or region are not set in the provider information."

        embed_component = BedrockEmbeddingComponent(aws_access_key, aws_secret_access_key, aws_region)
        embed_component.build(embedding_model_name)
        embeddings = await embed_component.run_embed_documents([doc.page_content for doc in documents])

        docs_with_embeddings = [Document(page_content=doc.page_content, metadata={"embedding": embedding}) for doc, embedding in zip(documents, embeddings)]

        db = await FAISS.afrom_documents(docs_with_embeddings, embed_component.model_instance)
        return db

    async def run_rag_bedrock(self, agent_data, query: str, db, top_k: int = 5):
        try:
            _d_agent = agent_data['Agent']
            _d_model = agent_data['Model']

            matching_docs = db.similarity_search(query, k=top_k)

            if not matching_docs:
                raise ValueError("No matching documents found")

            retriever = db.as_retriever()

            aws_access_key = self._get_credential_info(agent_data, "AWS_ACCESS_KEY_ID")
            aws_secret_access_key = self._get_credential_info(agent_data, "AWS_SECRET_ACCESS_KEY")
            aws_region = self._get_credential_info(agent_data, "AWS_REGION")

            if not all([aws_access_key, aws_secret_access_key, aws_region]):
                return "AWS credentials are not set in the provider information."

            if _d_agent.fm_provider_type == "T":
                bedrock_component = BedrockLLMComponent(aws_access_key, aws_secret_access_key, aws_region)
            elif _d_agent.fm_provider_type == "C":
                bedrock_component = ChatBedrockComponent(aws_access_key, aws_secret_access_key, aws_region)
            else:
                bedrock_component = ChatBedrockComponent(aws_access_key, aws_secret_access_key, aws_region)

            bedrock_component.build(
                model_id=_d_model.model_name,
                temperature=_d_agent.fm_temperature,
                top_p=_d_agent.fm_top_p,
                max_tokens=_d_agent.fm_response_token_limit
            )
            llm_instance = bedrock_component.model_instance

            qa_chain = RetrievalQA.from_chain_type(llm=llm_instance, chain_type="stuff", retriever=retriever)
            inputs = {"query": query, "input_documents": matching_docs}

            try:
                answer = await asyncio.to_thread(qa_chain.invoke, inputs)
                result = answer['result'] if 'result' in answer else answer
            except Exception as e:
                logging.error(f"Error generating response from QA chain: {str(e)}")
                result = "Error generating response from QA chain"

            return {
                "matching_documents": matching_docs,
                "llm_response": result
            }

        except Exception as e:
            logging.error(f"Exception in run_rag_bedrock: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))

    def _initialize_rag_model(self, agent_data, history):
        # Logic to initialize RAG model
        return None


    def _run_openai_model(self, agent_data, query):

        llms_component = None

        _d_agent = agent_data['Agent']
        _d_model = agent_data['Model']

        openai_api_key = self._get_credential_info(agent_data, "OPENAI_API_KEY")

        if not openai_api_key:
            return "OpenAI API key is not set in the provider information."
        
        if _d_agent.fm_provider_type == "T":
            llms_component = OpenAILLMComponent(openai_api_key)
            llms_component.build(
                    model_id=_d_model.model_name,
                    temperature=_d_agent.fm_temperature,
                    top_p=_d_agent.fm_top_p,
                    max_tokens=_d_agent.fm_response_token_limit
                )
        elif _d_agent.fm_provider_type == "C":
            llms_component = ChatOpenAIComponent(openai_api_key)
            llms_component.build(
                    model_id=_d_model.model_name,
                    temperature=_d_agent.fm_temperature,
                    max_tokens=_d_agent.fm_response_token_limit
                )
        else:
            llms_component = OpenAILLMComponent(openai_api_key)
            llms_component.build(
                    model_id=_d_model.model_name,
                    temperature=_d_agent.fm_temperature,
                    top_p=_d_agent.fm_top_p,
                    max_tokens=_d_agent.fm_response_token_limit
                )

        return llms_component.run(query)

    def _run_bedrock_model(self, agent_data, query):

        llms_component = None
        _d_agent = agent_data['Agent']
        _d_model = agent_data['Model']
 
        aws_access_key = self._get_credential_info(agent_data, "AWS_ACCESS_KEY_ID")
        aws_secret_access_key = self._get_credential_info(agent_data, "AWS_SECRET_ACCESS_KEY")
        aws_region = self._get_credential_info(agent_data, "AWS_REGION")

        if not all([aws_access_key, aws_secret_access_key, aws_region]):
            return "AWS credentials or region are not set in the provider information."
        
        if _d_agent.fm_provider_type == "T":
            llms_component = BedrockLLMComponent(aws_access_key, aws_secret_access_key, aws_region)
        elif _d_agent.fm_provider_type == "C":
            llms_component = ChatBedrockComponent(aws_access_key, aws_secret_access_key, aws_region)
        else:
            llms_component = BedrockLLMComponent(aws_access_key, aws_secret_access_key, aws_region)

        llms_component.build(
                model_id=_d_model.model_name,
                temperature=_d_agent.fm_temperature,
                top_p=_d_agent.fm_top_p,
                max_tokens=_d_agent.fm_response_token_limit
            )

        return llms_component.run(query)

    def _postprocess_response(self, agent_data, response: str):

        _d_agent = agent_data['Agent']
        post_processing_id = _d_agent.post_processing_id
        processing_data = self._get_processing_data(post_processing_id)[0]

        # pii mask
        if processing_data.pii_masking:
            pii_options = self._parse_options(processing_data.pii_masking)
            pii_masking_service = PiiMaskingService()
            response = pii_masking_service.mask_pii(response, pii_options)

        # normalize text
        if processing_data.normalization:
            normalize_options = self._parse_options(processing_data.normalization)
            text_normalization_service = TextNormalizationService()
            response = text_normalization_service.normalize_text(response, normalize_options)

        # stopword removal
        if processing_data.stopword_removal:
            stopwords = set(self._convert_list(processing_data.stopword_removal))
            for stopword in stopwords:
                response = response.replace(stopword, '')

        return response

    def _get_token_counts(self, agent_id: UUID, query: Optional[str] = None, text: Optional[str] = None):
        try:

            agent_data = self._get_agent_data(agent_id)
            _d_agent = agent_data['Model']
            
            logging.warning('=== _get_token_counts()  =====================================')

            logging.warning(query)
            logging.warning(_d_agent.model_name)
            logging.warning(text)
            token_component = TokenUtilityService(None, None, None)
            prompt_token_counts = token_component.get_token_count(query, _d_agent.model_name)
            completion_token_counts = token_component.get_token_count(text, _d_agent.model_name)
            prompt_cost = token_component.get_prompt_cost(text, _d_agent.model_name)
            completion_cost = token_component.get_completion_cost(query, _d_agent.model_name)

            logging.warning(prompt_token_counts)
            logging.warning(completion_token_counts)
            logging.warning(prompt_cost)
            logging.warning(completion_cost)

            logging.warning('=== _get_token_counts()  =====================================')

            prompt_token_counts = prompt_token_counts or 0
            completion_token_counts = completion_token_counts or 0
            prompt_cost = prompt_cost or 0.0
            completion_cost = completion_cost or 0.0

            if isinstance(prompt_cost, Decimal):
                prompt_cost = float(prompt_cost)
            if isinstance(completion_cost, Decimal):
                completion_cost = float(completion_cost)

            total_token_counts = prompt_token_counts+completion_token_counts
            total_cost = prompt_cost+completion_cost

            self.update_agent_count(agent_id, total_token_counts, total_cost)

            result = {
                "token_counts": total_token_counts,
                "total_cost": total_cost
            }

            return result

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def _get_openai_token_counts(self, text: Optional[str] = None, model_name: Optional[str] = None):

        token_component = TokenUtilityService(None, None, None)
        return token_component.get_openai_token_count(
                text=text,
                model_id=model_name
            )

    def _get_bedrock_token_counts(self, text: Optional[str] = None, model_name: Optional[str] = None):

        aws_access_key = os.getenv("INNER_AWS_ACCESS_KEY_ID")
        aws_secret_access_key = os.getenv("INNER_AWS_SECRET_ACCESS_KEY")
        aws_region = os.getenv("INNER_AWS_REGION")

        if not aws_access_key:
            return "aws_access_key is not set in the environment variables"
        if not aws_secret_access_key:
            return "aws_secret_access_key is not set in the environment variables"
        if not aws_region:
            return "aws_region is not set in the environment variables"

        token_component = TokenUtilityService(aws_access_key, aws_secret_access_key, aws_region)
        return token_component.get_bedrock_token_count(
                text=text,
                model_id=model_name
            )

    def update_agent_count(self, agent_id: UUID, token_count: int, total_cost: float):
        try:
            agent = self.session.get(Agent, agent_id)

            if agent:
                agent.expected_token_count += token_count
                agent.expected_request_count += 1
                agent.expected_cost += total_cost
                self.session.commit()

        except Exception as e:
            self.session.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        
    def _get_credential_info(self, agent_data, key):

        _d_credential = agent_data['Credential']

        if not _d_credential.inner_used:
            if key == "AWS_ACCESS_KEY_ID":
                return _d_credential.access_key
            elif key == "AWS_SECRET_ACCESS_KEY":
                return _d_credential.secret_key
            elif key == "AWS_REGION":
                return os.getenv(key)
            elif key == "OPENAI_API_KEY":
                return _d_credential.api_key
        else:
            return os.getenv(key)