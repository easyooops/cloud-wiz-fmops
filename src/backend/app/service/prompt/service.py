import os
from typing import Optional
from fastapi import HTTPException
from sqlmodel import Session, select
from uuid import UUID
import logging

from app.service.agent.model import Agent
from app.service.model.model import Model
from app.service.provider.model import Provider
from app.components.LLM.OpenAI import OpenAILLMComponent
from app.components.Chat.OpenAI import ChatOpenAIComponent
from app.components.Chat.Bedrock import ChatBedrockComponent
from app.components.LLM.Bedrock import BedrockLLMComponent



class PromptService:
    def __init__(self, session: Session):
        self.session = session

    def get_prompt(self, agent_id: UUID, query: Optional[str] = None):
        
        response = None

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

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

        return response

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

    def _run_embedding(self, agent_data, query, embedding_provider):
        # Logic to run specified embedding provider
        if embedding_provider == "ProviderA":
            return self._run_embedding_provider_a(agent_data, query)
        elif embedding_provider == "ProviderB":
            return self._run_embedding_provider_b(agent_data, query)
        else:
            return self._run_default_embedding(agent_data, query)

    def _run_default_embedding(self, agent_data, query):
        # Default embedding provider or other providers
        return None

    def _run_provider(self, agent_data, query, history):
        
        _d_provider = agent_data['Provider']

        if _d_provider.name == "OpenAI":
            return self._run_openai_model(agent_data, query)
        elif _d_provider.name == "Bedrock":
            return self._run_bedrock_model(agent_data, query)
        else:
            return self._run_openai_model(agent_data, query)

    def _run_embedding_provider_a(self, agent_data, query):
        # Logic to run embedding provider A
        pass

    def _run_embedding_provider_b(self, agent_data, query):
        # Logic to run embedding provider B
        pass

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
