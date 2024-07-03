import asyncio
from decimal import Decimal
from sqlalchemy.orm import aliased
import os
from typing import Optional
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
from ddtrace.llmobs.decorators import agent, workflow, tool, task
from app.core.util.logging import LoggingConfigurator


class PromptService:
    def __init__(self, session: Session):
        self.session = session

    # @agent(name="prompt_agent")
    # @tool(name="get_current_weather")
    # @task
    # @log_method
    # @workflow
    @LoggingConfigurator.log_method
    def get_prompt(self, agent_id: UUID, query: Optional[str] = None) -> ChatResponse:

        response = []

        logger = logging.getLogger('agent')
        logging.warning(logger.callHandlers)
        logger.debug("Agent logger is configured debug.")
        logger.info("Agent logger is configured info.")

        try:
            agent_data = self._get_agent_data(agent_id)
            _d_agent = agent_data['Agent']

            # get history
            history = self._get_history(agent_id)
            self._verify_query(query)

            # pre-processing
            if _d_agent.processing_enabled:
                query = self._preprocess_query(query)

            # embedding
            if _d_agent.embedding_enabled:
                try:
                    documents = asyncio.run(self._run_embedding(agent_data, query))
                    rag_response = asyncio.run(self.run_rag_openai(agent_data, query, documents))
                    response = rag_response["llm_response"]
                except openai.PermissionDeniedError as e:
                    logging.error(f"Embedding generation permission denied: {str(e)}")
                    raise HTTPException(status_code=403, detail="Embedding generation permission denied")
            else:
                response = self._run_provider(agent_data, query, history)

            # post-processing
            if _d_agent.processing_enabled:
                response = self._postprocess_response(response)

            # set history
            history = self._set_history(agent_id)

            # tokens, cost
            tokens = self._get_token_counts(agent_id, query, response)

            # logger.debug("Inside debug example_method")
            # logger.info("Inside info example_method")
            # logger.warn("Inside warn example_method")
            # logger.warning("Inside warning example_method")
            # logger.error("Inside error example_method")

            return ChatResponse(
                        answer=response,
                        tokens=tokens['token_counts'],
                        cost=tokens['total_cost']
                    )

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))



    def _get_agent_data(self, agent_id: UUID):
        EmbeddingModel = aliased(Model)
        statement = (
            select(Agent, Model, Provider, Store, EmbeddingModel.model_name.label('embedding_model_name'))
            .join(Model, Agent.fm_model_id == Model.model_id)
            .join(Provider, Agent.fm_provider_id == Provider.provider_id)
            .join(Store, Agent.storage_object_id == Store.store_id)
            .outerjoin(EmbeddingModel, Agent.embedding_model_id == EmbeddingModel.model_id)
        )
        statement = statement.where(Agent.agent_id == agent_id)

        result = self.session.exec(statement).first()

        if not result:
            raise HTTPException(status_code=404, detail="Agent not found")

        agent_data, model_data, provider_data, store_data, embedding_model_name = result
        return {"Agent": agent_data, "Provider": provider_data, "Model": model_data, "Store": store_data, "EmbeddingModelName": embedding_model_name}



    def _get_history(self, agent_id: UUID):
        # Logic to retrieve history
        return None
    
    def _set_history(self, agent_id: UUID):
        # Logic to retrieve history
        return None    

    def _verify_query(self, query: str):
        # Logic to verify query
        pass

    def _preprocess_query(self, query: str):
        pass

    def split_text_into_chunks(self, text, max_tokens):
        encoding = tiktoken.get_encoding("cl100k_base")
        tokens = encoding.encode(text)

        chunks = []
        for i in range(0, len(tokens), max_tokens):
            chunk_tokens = tokens[i:i + max_tokens]
            chunks.append(encoding.decode(chunk_tokens))
        return chunks

    async def _run_embedding(self, agent_data, query):

        _d_provider = agent_data['Provider']
        store_service = StoreService(self.session)

        storage_object_id = str(agent_data['Agent'].storage_object_id)
        storage_store = agent_data['Store']
        store_name = storage_store.store_name

        logging.info(f"Storage Object ID:{storage_object_id}")
        logging.info(f"Store Name: {store_name}")

        file_metadata_list = store_service.list_files(store_name)
        files = [file_metadata['Key'] for file_metadata in file_metadata_list]
        logging.info(f"Files: {files}")

        if not files:
            logging.error("No files found in storage Object")
            raise HTTPException(status_code=500, detail="No files found in storage object")

        documents = store_service.load_documents(files)
        logging.info(f"Documents: {documents}")

        if not documents:
            logging.error("No documents found in files")
            raise HTTPException(status_code=500, detail="No documents found in files")

        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        chunks = text_splitter.split_documents(documents)
        logging.info(f"Chunks: {chunks}")

        if not chunks:
            raise ValueError("No chunks were split into chunks")

        if _d_provider.name == "OpenAI":
            return await self._run_embedding_openai_model(agent_data, chunks)
        elif _d_provider.name == "Bedrock":
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
        _d_agent = agent_data['Agent']
        embedding_model_name = agent_data['EmbeddingModelName']

        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OpenAI API key is not in the environment variables")

        embed_component = OpenAIEmbeddingComponent(openai_api_key)
        embed_component.build(
            model_id=embedding_model_name
        )
        embeddings = embed_component.run_embed_documents([doc.page_content for doc in documents])
        db = await FAISS.afrom_documents(documents, OpenAIEmbeddings(api_key=openai_api_key))
        return db


    async def run_rag_openai(self, agent_data, query: str, db, top_k: int = 5):
        try:
            _d_agent = agent_data['Agent']
            _d_model = agent_data['Model']

            logging.info(f"FAISS database created")
            matching_docs = await db.asimilarity_search(query, k=top_k)
            logging.info(f"Matching documents: {matching_docs}")

            if not matching_docs:
                raise ValueError("No matching documents found")

            retriever = db.as_retriever()
            openai_api_key = os.getenv("OPENAI_API_KEY")
            if not openai_api_key:
                raise ValueError("OpenAI API key is not set in the environment variables")
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


    def _run_embedding_bedrock_model(self, agent_data, documents):

        aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        aws_region = os.getenv("AWS_REGION")

        if not aws_access_key:
            raise ValueError("aws_access_key is not set in the environment variables")
        if not aws_secret_access_key:
            raise ValueError("aws_secret_access_key is not set in the environment variables")
        if not aws_region:
            raise ValueError("aws_region is not set in the environment variables")

        embed_component = None
        _d_agent = agent_data['Agent']
        _d_model = agent_data['Model']

        if _d_agent.fm_provider_type == "E":
            embed_component = BedrockEmbeddingComponent(aws_access_key, aws_secret_access_key, aws_region)
            embed_component.build(model_id=_d_model.model_name)
        return embed_component.run_embed_documents(documents)

    def _initialize_rag_model(self, agent_data, history):
        # Logic to initialize RAG model
        return None


    def _run_openai_model(self, agent_data, query):
        
        openai_api_key = os.getenv("OPENAI_API_KEY")

        if not openai_api_key:
            raise ValueError("OpenAI API key is not set in the environment variables")
                
        llms_component = None

        _d_agent = agent_data['Agent']
        _d_model = agent_data['Model']

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

        aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        aws_region = os.getenv("AWS_REGION")

        if not aws_access_key:
            raise ValueError("aws_access_key is not set in the environment variables")
        if not aws_secret_access_key:
            raise ValueError("aws_secret_access_key is not set in the environment variables")
        if not aws_region:
            raise ValueError("aws_region is not set in the environment variables")
                                
        llms_component = None
        _d_agent = agent_data['Agent']
        _d_model = agent_data['Model']

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
    
    def _postprocess_response(self, response):
        # Logic for post-processing
        return response

    def _get_token_counts(self, agent_id: UUID, query: Optional[str] = None, text: Optional[str] = None):
        try:

            agent_data = self._get_agent_data(agent_id)
            _d_agent = agent_data['Model']
            # _d_provider = agent_data['Provider']

            # if _d_provider.name == "OpenAI":
            #     token_counts = self._get_openai_token_counts(text, _d_agent.model_name)
            # elif _d_provider.name == "Bedrock":
            #     token_counts = self._get_bedrock_token_counts(text, _d_agent.model_name)
            # else:
            #     token_counts = self._get_openai_token_counts(text, _d_agent.model_name)

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

        aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        aws_region = os.getenv("AWS_REGION")

        if not aws_access_key:
            raise ValueError("aws_access_key is not set in the environment variables")
        if not aws_secret_access_key:
            raise ValueError("aws_secret_access_key is not set in the environment variables")
        if not aws_region:
            raise ValueError("aws_region is not set in the environment variables")
        
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