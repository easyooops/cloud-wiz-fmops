from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlmodel import Session
from typing import List, Optional
from app.core.interface.service import ServiceType
from app.core.factories import get_database
from app.service.embedding.service import EmbeddingService
from app.api.v1.schemas.embedding import EmbeddingResponse, EmbeddingMultipleResponse
from app.service.store.service import StoreService

router = APIRouter()
load_dotenv()

# OpenAI Text Embedding
@router.post("/embedding-openai", response_model=EmbeddingResponse)
def get_openai_embedding(
        text: Optional[str] = None,
        session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        if not text:
            raise HTTPException(status_code=400, detail="Text parameter is required")

        embedding_service = EmbeddingService(session)
        embedding = embedding_service.get_openai_embedding(text)
        return EmbeddingResponse(embedding=embedding)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# OpenAI Embedding Single File (Upload to S3 store)
@router.post("/{store_name}/embedding-openai-file", response_model=EmbeddingMultipleResponse)
def openai_file_embeddings(
        store_name: str,
        files: List[UploadFile] = File(...),
        session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        store_service = StoreService(session)
        file_contents = []

        for file in files:
            # Read the file content into memory
            file_content = file.file.read().decode("utf-8")
            file_contents.append(file_content)

            # Reset file pointer and store the file in S3
            file.file.seek(0)
            store_service.upload_file_to_store(store_name, file)

        embedding_service = EmbeddingService(session)
        embeddings = embedding_service.get_openai_embeddings(file_contents)
        return EmbeddingMultipleResponse(embeddings=embeddings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# OpenAI Embedding Multi Files (Upload to S3 store)
@router.post("/{store_name}/embedding-openai-files", response_model=EmbeddingMultipleResponse)
def openai_multi_files_embeddings(
        store_name: str,
        files: List[UploadFile] = File(...),
        session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = StoreService(session)
        file_contents = []

        for file in files:
            content = file.file.read().decode("utf-8")
            file_contents.append(content)
            file.file.seek(0)

        for file in files:
            service.upload_file_to_store(store_name, file)

        embedding_service = EmbeddingService(session)
        if len(file_contents) == 1:
            embedding = embedding_service.get_openai_embedding(file_contents[0])
            return EmbeddingResponse(embedding=embedding)
        else:
            embeddings = embedding_service.get_openai_embeddings(file_contents)
            return EmbeddingMultipleResponse(embeddings=embeddings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading and embedding files: {str(e)}")