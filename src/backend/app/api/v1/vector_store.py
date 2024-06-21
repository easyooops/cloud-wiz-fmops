import os
import boto3
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException
from langchain_core.documents import Document
# from langchain_community.llms import OpenAI
from sqlmodel import Session
from typing import List
from app.core.interface.service import ServiceType
from app.core.factories import get_database
from app.service.embedding.service import EmbeddingService
from app.components.Embedding.OpenAI import OpenAIEmbeddingComponent
from app.api.v1.schemas.embedding import EmbeddingMultipleResponse

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
        store_name: str,
        top_k: int = 5,
        session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        embedding_service = EmbeddingService(session)

        s3_client = boto3.client('s3')
        response = s3_client.list_objects_v2(Bucket=os.getenv("AWS_S3_BUCKET_VECTOR_STORE_NAME"), Prefix=f"{store_name}/")
        files = [content['Key'] for content in response.get('Contents', [])]

        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OpenAI API key is not set in the environment")

        embedding_component = OpenAIEmbeddingComponent(openai_api_key)
        embedding_component.configure()
        dimension = 1536
        await embedding_service.initialize_faiss_store(embedding_component, dimension)

        for s3_faiss_key in files:
            local_faiss_path = f"/tmp/{s3_faiss_key.split('/')[-1]}"
            embedding_service.load_faiss_index_from_s3(s3_faiss_key, local_faiss_path)

        query_vector: list[float] = embedding_component.execute_embed_query(query)
        if not isinstance(query_vector, list) or not all(isinstance(x, float) for x in query_vector):
            raise ValueError("query_vector must be a list of floats")

        results = await embedding_service.query_faiss_store(query_vector, top_k)
        documents = [Document(page_content=str(result)) for result in results]

        response_text = generate_response_from_documents(query, documents, openai_api_key)
        return {"results": response_text}
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


def generate_response_from_documents(query, documents, openai_api_key):
    client = OpenAI(api_key=openai_api_key)
    context = "\n\n".join([f"문서 {i+1}: {doc.page_content}" for i, doc in enumerate(documents)])
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "당신은 도움을 주는 어시스턴트입니다. 주어진 문서를 기반으로 정확하고 상세한 답변을 제공하세요."},
            {"role": "user", "content": f"문맥: {context}\n\n질문: {query}\n\n정확하고 상세한 답변을 한국어로 작성하세요:"},
        ],
        temperature=0.5,
        max_tokens=1000
    )
    return response.choices[0].message.content.strip()
