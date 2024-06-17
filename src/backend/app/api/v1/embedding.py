from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlmodel import Session
from typing import List, Optional
from app.core.interface.service import ServiceType
from app.core.factories import get_database
from app.service.embedding.service import EmbeddingService
from app.api.v1.schemas.embedding import EmbeddingResponse, EmbeddingMultipleResponse
from app.service.store.service import StoreService
import tiktoken

router = APIRouter()
load_dotenv()

def split_text_into_chunks(text, max_tokens):
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)

    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i:i + max_tokens]
        chunks.append(encoding.decode(chunk_tokens))

    return chunks

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

@router.post("/{store_name}/embedding-openai-file", response_model=EmbeddingMultipleResponse)
def openai_file_embeddings(
        store_name: str,
        files: List[UploadFile] = File(...),
        session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        store_service = StoreService(session)
        file_contents = []
        MAX_TOKENS = 5000

        for file in files:
            raw_content = file.file.read()
            try:
                content = raw_content.decode("utf-8")
            except UnicodeDecodeError:
                try:
                    content = raw_content.decode("latin1")
                except UnicodeDecodeError:
                    raise HTTPException(status_code=400, detail="File encoding not supported")

            chunks = split_text_into_chunks(content, MAX_TOKENS)
            file_contents.extend(chunks)

            file.file.seek(0)
            store_service.upload_file_to_store(store_name, file)

        embedding_service = EmbeddingService(session)
        embeddings = embedding_service.get_openai_embeddings(file_contents)
        return EmbeddingMultipleResponse(embeddings=embeddings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{store_name}/embedding-openai-files", response_model=EmbeddingMultipleResponse)
def openai_multi_files_embeddings(
        store_name: str,
        files: List[UploadFile] = File(...),
        session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = StoreService(session)
        file_contents = []
        MAX_TOKENS = 5000

        for file in files:
            raw_content = file.file.read()
            try:
                content = raw_content.decode("utf-8")
            except UnicodeDecodeError:
                try:
                    content = raw_content.decode("latin1")
                except UnicodeDecodeError:
                    raise HTTPException(status_code=400, detail="File encoding not supported")

            chunks = split_text_into_chunks(content, MAX_TOKENS)
            file_contents.extend(chunks)
            file.file.seek(0)

        for file in files:
            service.upload_file_to_store(store_name, file)

        embedding_service = EmbeddingService(session)
        embeddings = embedding_service.get_openai_embeddings(file_contents)
        return EmbeddingMultipleResponse(embeddings=embeddings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading and embedding files: {str(e)}")

@router.post("/embedding-bedrock", response_model=EmbeddingResponse)
def get_bedrock_embedding(
        text: Optional[str] = None,
        model: Optional[str] = None,
        session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        if not text or not model:
            raise HTTPException(status_code=400, detail="Text and model parameters are required")

        embedding_service = EmbeddingService(session)
        embedding = embedding_service.get_bedrock_embedding(model, text)
        return EmbeddingResponse(embedding=embedding)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{store_name}/embedding-bedrock-file", response_model=EmbeddingResponse)
def bedrock_single_file_embedding(
        store_name: str,
        model: Optional[str] = None,
        file: UploadFile = File(...),
        session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        if not store_name or not model:
            raise HTTPException(status_code=400, detail="store_name and model parameters are required")

        service = StoreService(session)
        raw_content = file.file.read()
        try:
            content = raw_content.decode("utf-8")
        except UnicodeDecodeError:
            try:
                content = raw_content.decode("latin1")
            except UnicodeDecodeError:
                raise HTTPException(status_code=400, detail="File encoding not supported")

        file.file.seek(0)
        service.upload_file_to_store(store_name, file)

        MAX_TOKENS = 5000
        chunks = split_text_into_chunks(content, MAX_TOKENS)

        embedding_service = EmbeddingService(session)
        embeddings = [embedding_service.get_bedrock_embedding(model, chunk) for chunk in chunks]

        return EmbeddingResponse(embedding=embeddings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading and embedding file: {str(e)}")

@router.post("/{store_name}/embedding-bedrock-files", response_model=EmbeddingMultipleResponse)
def bedrock_multi_files_embeddings(
        store_name: str,
        model: Optional[str] = None,
        files: List[UploadFile] = File(...),
        session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        if not store_name or not model:
            raise HTTPException(status_code=400, detail="store_name and model parameters are required")

        service = StoreService(session)
        file_contents = []
        MAX_TOKENS = 5000

        for file in files:
            raw_content = file.file.read()
            try:
                content = raw_content.decode("utf-8")
            except UnicodeDecodeError:
                try:
                    content = raw_content.decode("latin1")
                except UnicodeDecodeError:
                    raise HTTPException(status_code=400, detail="File encoding not supported")

            chunks = split_text_into_chunks(content, MAX_TOKENS)
            file_contents.extend(chunks)
            file.file.seek(0)
            service.upload_file_to_store(store_name, file)

        embedding_service = EmbeddingService(session)
        embeddings = embedding_service.get_bedrock_embeddings(model, file_contents)
        return EmbeddingMultipleResponse(embeddings=embeddings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading and embedding files: {str(e)}")