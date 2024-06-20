import os
from typing import List, Optional
from fastapi import HTTPException
from sqlmodel import Session, select
from uuid import UUID

from app.service.agent.model import Agent
from app.api.v1.schemas.agent import AgentCreate, AgentUpdate
from app.logging import Logger
from app.providers import ProviderA, ProviderB
from app.preprocessing import Preprocessor
from app.llm import OpenAILLMComponent
from app.rag import RAGModel


class PromptService:
    def __init__(self, session: Session, logger: Logger):
        self.session = session
        self.logger = logger

    def get_prompt(self, agent_id: UUID, query: Optional[str] = None):
        
        response = None

        try:
            agent_data = self._get_agent_data(agent_id)

            history = self._get_history(agent_id)
            self._verify_query(query)
            
            if agent_data.processing_enabled:
                query = self._preprocess_query(query)

            embedding_provider = options.get("embedding_provider", "default")
            provider_name = options.get("provider_name", "default")

            if agent_data.embedding_enabled:
                embedding = self._run_embedding(agent_data, query, embedding_provider)

            response = self._run_provider(agent_data, embedding, history, provider_name)

            if agent_data.processing_enabled:
                response = self._postprocess_response(response)

        except Exception as e:
            self.logger.error(f"Error processing query: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))

        return response

    def _get_agent_data(self, agent_id: UUID):
        statement = select(Agent).where(Agent.agent_id == agent_id)
        agent_data = self.session.exec(statement).first()
        if not agent_data:
            raise HTTPException(status_code=404, detail="Agent not found")
        return agent_data

    def _get_history(self, agent_id: UUID):
        # Logic to retrieve history
        return None

    def _verify_query(self, query: str):
        # Logic to verify query
        pass

    def _preprocess_query(self, query: str):
        preprocessor = Preprocessor()
        return preprocessor.process(query)

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
        document_loader = DocumentLoader(agent_data)
        vector_store = VectorStore()
        embedding_model = EmbeddingModel(document_loader, vector_store)
        return embedding_model.embed(query)

    def _run_provider(self, agent_data, embedding, history, provider_name):
        # Logic to run specified provider
        if provider_name == "RAG":
            rag_model = self._initialize_rag_model(agent_data, history)
            return self._run_rag_model(rag_model, embedding)
        elif provider_name == "OpenAI":
            return self._run_openai_model(embedding)
        else:
            # Default provider or other providers
            provider = ProviderA()  # Example provider
            return provider.process(embedding)

    def _run_embedding_provider_a(self, agent_data, query):
        # Logic to run embedding provider A
        pass

    def _run_embedding_provider_b(self, agent_data, query):
        # Logic to run embedding provider B
        pass

    def _initialize_rag_model(self, agent_data, history):
        # Logic to initialize RAG model
        rag_model = RAGModel(agent_data, history)
        return rag_model

    def _run_rag_model(self, rag_model, embedding):
        return rag_model.generate_response(embedding)

    def _run_openai_model(self, embedding):
        # Logic to run OpenAI model
        openai_api_key = os.getenv("OPENAI_API_KEY")
        openai_component = OpenAILLMComponent(openai_api_key)
        openai_component.build(temperature=0.5)
        return openai_component.run(embedding)

    def _postprocess_response(self, response):
        # Logic for post-processing
        return response
