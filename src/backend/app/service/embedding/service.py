from sqlmodel import Session
from fastapi import HTTPException
from app.components.Embedding.OpenAI import OpenAIEmbeddingComponent
from app.components.Embedding.Bedrock import BedrockEmbeddingComponent
import os

class EmbeddingService:
    def __init__(self, session: Session):
        self.session = session

    def get_openai_embedding(self, text: str):
        try:
            openai_api_key = os.getenv("OPENAI_API_KEY")
            if not openai_api_key:
                raise ValueError("OpenAI API key is not set in the environment variables")

            embedding_component = OpenAIEmbeddingComponent(openai_api_key)
            embedding_component.configure()
            embedding = embedding_component.execute_embed_query(text)
            return embedding
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_openai_embeddings(self, texts: list):
        try:
            openai_api_key = os.getenv("OPENAI_API_KEY")
            if not openai_api_key:
                raise ValueError("OpenAI API key is not set in the environment variables")
            embedding_component = OpenAIEmbeddingComponent(openai_api_key)
            embedding_component.configure()
            embeddings = embedding_component.execute_embed_documents(texts)
            return embeddings
        except Exception as e:
            raise  HTTPException(status_code=500, detail=str(e))

    def get_bedrock_embedding(self, model_id: str, text: str):
        try:
            aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
            aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
            aws_region = os.getenv("AWS_REGION")
            if not all([aws_access_key, aws_secret_access_key, aws_region]):
                raise ValueError("AWS credentials or region are not set in the environment variables")

            embedding_component = BedrockEmbeddingComponent()
            embedding_component.configure(model_id=model_id)
            embedding = embedding_component.execute_embed_query(text)
            return embedding
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_bedrock_embeddings(self, model_id: str, texts: list):
        try:
            aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
            aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
            aws_region = os.getenv("AWS_REGION")
            if not all([aws_access_key, aws_secret_access_key, aws_region]):
                raise ValueError("AWS credentials or region are not set in the environment variables")

            embedding_component = BedrockEmbeddingComponent()
            embedding_component.configure(model_id=model_id)
            embedding = embedding_component.execute_embed_documents(texts)
            return embedding
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
