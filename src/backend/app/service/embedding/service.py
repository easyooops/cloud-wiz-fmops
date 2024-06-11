from sqlmodel import Session
from fastapi import HTTPException
from app.components.Embedding.OpenAI import OpenAIEmbeddingComponent
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
            embedding = embedding_component.execute(text)
            return embedding
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
