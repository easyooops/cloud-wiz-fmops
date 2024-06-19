import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlmodel import Session
from typing import List, Optional
from datetime import datetime
from app.components.Embedding.OpenAI import OpenAIEmbeddingComponent
from app.components.Embedding.Bedrock import BedrockEmbeddingComponent
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
async def openai_file_embeddings(
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

        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OpenAI API key is not set in the environment variables")

        openai_embedding_component = OpenAIEmbeddingComponent(openai_api_key)
        openai_embedding_component.configure()

        await embedding_service.initialize_faiss_store(openai_embedding_component)
        await embedding_service.add_to_faiss_store(file_contents)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        local_faiss_path = f"/tmp/faiss_index_{timestamp}.index"
        s3_faiss_path = f"{store_name}/faiss_index_{timestamp}.index"
        embedding_service.save_faiss_index_to_s3(s3_faiss_path, local_faiss_path)

        embeddings = embedding_service.get_openai_embeddings(file_contents)
        return EmbeddingMultipleResponse(embeddings=embeddings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.post("/{store_name}/embedding-openai-files", response_model=EmbeddingMultipleResponse)
async def openai_multi_files_embeddings(
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
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OpenAI API key is not set in the environment variables")

        embedding_component = OpenAIEmbeddingComponent(openai_api_key)
        embedding_component.configure()

        await embedding_service.initialize_faiss_store(embedding_component)

        embeddings = embedding_service.get_openai_embeddings(file_contents)
        await embedding_service.add_to_faiss_store(file_contents)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        local_faiss_path = f"/tmp/faiss_index_{timestamp}.index"
        s3_faiss_path = f"{store_name}/faiss_index_{timestamp}.index"
        embedding_service.save_faiss_index_to_s3(s3_faiss_path, local_faiss_path)

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
async def bedrock_single_file_embedding(
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

        bedrock_embedding_component = BedrockEmbeddingComponent()
        bedrock_embedding_component.configure(model_id=model)

        await embedding_service.initialize_faiss_store(bedrock_embedding_component)
        embeddings = [embedding_service.get_bedrock_embedding(model, chunk) for chunk in chunks]
        await embedding_service.add_to_faiss_store(chunks)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        local_faiss_path = f"/tmp/faiss_index_{timestamp}.index"
        s3_faiss_path = f"{store_name}/faiss_index_{timestamp}.index"
        embedding_service.save_faiss_index_to_s3(s3_faiss_path, local_faiss_path)

        return EmbeddingResponse(embedding=embeddings)
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error uploading and embedding file: {str(e)}")

@router.post("/{store_name}/embedding-bedrock-files", response_model=EmbeddingMultipleResponse)
async def bedrock_multi_files_embeddings(
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

        bedrock_embedding_component = BedrockEmbeddingComponent()
        bedrock_embedding_component.configure(model_id=model)

        await embedding_service.initialize_faiss_store(bedrock_embedding_component)
        embeddings = embedding_service.get_bedrock_embeddings(model, file_contents)
        await embedding_service.add_to_faiss_store(file_contents)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        local_faiss_path = f"/tmp/faiss_index_{timestamp}.index"
        s3_faiss_path = f"{store_name}/faiss_index_{timestamp}.index"
        embedding_service.save_faiss_index_to_s3(s3_faiss_path, local_faiss_path)

        return EmbeddingMultipleResponse(embeddings=embeddings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading and embedding files: {str(e)}")