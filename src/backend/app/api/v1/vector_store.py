import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
from app.core.interface.service import ServiceType
from app.core.factories import get_database
from app.service.embedding.service import EmbeddingService
from app.components.Embedding.OpenAI import OpenAIEmbeddingComponent
from app.api.v1.schemas.embedding import EmbeddingResponse, EmbeddingMultipleResponse

router = APIRouter()
load_dotenv()
@router.post("/initialize-faiss")
async def initialize_faiss_store(session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))):
    embedding_service = EmbeddingService(session)
    openai_api_key = os.getenv("OPENAI_API_KEY")
    embedding_component = OpenAIEmbeddingComponent(openai_api_key)
    embedding_component.configure()
    await embedding_service.initialize_faiss_store(embedding_component)
    return {"status": "Faiss store initialized"}

@router.post("/add-to-faiss", response_model=EmbeddingMultipleResponse)
async def add_to_faiss_store(
        texts: List[str],
        session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    embedding_service = EmbeddingService(session)
    embeddings = await embedding_service.add_to_faiss_store(texts)
    return EmbeddingMultipleResponse(embeddings=embeddings)

@router.post("/query-faiss")
async def query_faiss_store(
        query: str,
        top_k: int = 5,
        session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    embedding_service = EmbeddingService(session)
    results = await embedding_service.query_faiss_store(query, top_k)
    return results

