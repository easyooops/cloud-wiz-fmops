import os
from typing import Optional
from fastapi import HTTPException
from sqlmodel import Session, select
from uuid import UUID
import logging

from app.components.Embedding.Bedrock import BedrockEmbeddingComponent
from app.components.Embedding.OpenAI import OpenAIEmbeddingComponent
from app.service.agent.model import Agent
from app.service.model.model import Model
from app.service.provider.model import Provider
from app.components.LLM.OpenAI import OpenAILLMComponent
from app.components.Chat.OpenAI import ChatOpenAIComponent
from app.components.Chat.Bedrock import ChatBedrockComponent
from app.components.LLM.Bedrock import BedrockLLMComponent
from app.core.util.token import TokenUtilityService
from app.api.v1.schemas.chat import ChatResponse



class PromptService:
    def __init__(self, session: Session):
        self.session = session

    def get_prompt(self, agent_id: UUID, query: Optional[str] = None) -> ChatResponse:
        
        response = []

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
                embedding = self._run_embedding(agent_data, query)

            # default llms
            response = self._run_provider(agent_data, query, history)

            # post-processing
            if _d_agent.processing_enabled:
                response = self._postprocess_response(response)

            # set history
            history = self._set_history(agent_id)

            # Extract tokens count from response if available
            tokens = 0
            logging.warning(response)


            # response_metadata = response.response_metadata  # AIMessage 객체의 usage_metadata

            # if response_metadata:
            #     usage = response_metadata.get('usage')
            #     if usage:
            #         total_tokens = usage.get('total_tokens')
            #         if isinstance(total_tokens, int):
            #             tokens = total_tokens
            #         else:
            #             # total_tokens가 int 형식이 아닌 경우 처리
            #             logging.warning(f"total_tokens is not an integer: {total_tokens}")
            # else:
            #     # usage_metadata가 없는 경우 처리
            #     logging.warning("usage_metadata is not available: {usage_metadata}")                    

            tokens = self._get_token_counts(agent_id, response)
            cost_per_token = 0.004
            tokens_per_thousand = 1000

            return ChatResponse(
                        answer=response, 
                        tokens=tokens, 
                        cost=(tokens/tokens_per_thousand)*cost_per_token
                    )

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

        

    def _get_agent_data(self, agent_id: UUID):
        statement = (
            select(Agent, Model, Provider)
            .join(Model, Agent.fm_model_id == Model.model_id)
            .join(Provider, Agent.fm_provider_id == Provider.provider_id)
        )
        statement = statement.where(Agent.agent_id == agent_id)

        result = self.session.exec(statement).first()

        if not result:
            raise HTTPException(status_code=404, detail="Agent not found")
        
        agent_data, model_data, provider_data = result
        return {"Agent": agent_data, "Provider": provider_data, "Model": model_data}
    
    
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

    def _preprocess_documents(self, documents:list):
        pass

    def _run_embedding(self, agent_data, query, documents):

        _d_provider = agent_data['Provider']

        if _d_provider.name == "OpenAI":
            return self._run_embedding_openai_model(agent_data, documents)
        elif _d_provider.name == "Bedrock":
            return self._run_embedding_bedrock_model(agent_data, documents)
        else:
            return self._run_embedding_openai_model(agent_data, documents)

    def _run_provider(self, agent_data, query, history):
        
        _d_provider = agent_data['Provider']

        if _d_provider.name == "OpenAI":
            return self._run_openai_model(agent_data, query)
        elif _d_provider.name == "Bedrock":
            return self._run_bedrock_model(agent_data, query)
        else:
            return self._run_openai_model(agent_data, query)

    def _run_embedding_openai_model(self, agent_data, documents):

        openai_api_key = os.getenv("OPENAI_API_KEY")

        if not openai_api_key:
            raise ValueError("OpenAI API key is not in the environment variables")

        embed_component = None
        _d_agent = agent_data['Agent']
        _d_model = agent_data['Model']

        if _d_agent.fm_provider_type == "E":
            embed_component = OpenAIEmbeddingComponent(openai_api_key)
            embed_component.build(model_id=_d_model.model_name)
        return embed_component.run_embed_documents(documents)

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

    def _run_rag_model(self, rag_model, embedding):
        return rag_model.generate_response(embedding)

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

    def _get_token_counts(self, agent_id: UUID, text: Optional[str] = None):
        try:
            token_counts = 0
            agent_data = self._get_agent_data(agent_id)
            _d_agent = agent_data['Model']
            _d_provider = agent_data['Provider']

            if _d_provider.name == "OpenAI":
                token_counts = self._get_openai_token_counts(text, _d_agent.model_name)
            elif _d_provider.name == "Bedrock":
                token_counts = self._get_bedrock_token_counts(text, _d_agent.model_name)
            else:
                token_counts = self._get_openai_token_counts(text, _d_agent.model_name)

            self.update_agent_count(agent_id, token_counts)

            return token_counts
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
    
    def update_agent_count(self, agent_id: UUID, token_count: int):
        try:
            agent = self.session.get(Agent, agent_id)
            cost_per_token = 0.004
            tokens_per_thousand = 1000
            if agent:
                agent.expected_token_count += token_count
                agent.expected_request_count += 1
                agent.expected_cost += (token_count/tokens_per_thousand) * cost_per_token
                self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise HTTPException(status_code=500, detail=str(e))    