import os
import boto3
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException
from langchain_core.documents import Document
from sqlmodel import Session
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader, Docx2txtLoader
from typing import List
import pandas as pd
from app.components.Chat.OpenAI import ChatOpenAIComponent
from app.core.interface.service import ServiceType
from app.core.factories import get_database
from app.service.chat.service import ChatService
from app.service.embedding.service import EmbeddingService
from app.components.Embedding.OpenAI import OpenAIEmbeddingComponent
from app.api.v1.schemas.embedding import EmbeddingMultipleResponse
from app.service.store.service import StoreService
from langchain.chains.question_answering import load_qa_chain

router = APIRouter()
load_dotenv()


@router.post("/initialize-faiss")
async def initialize_faiss_store(session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))):
    embedding_service = EmbeddingService(session)
    openai_api_key = os.getenv("OPENAI_API_KEY")
    embedding_component = OpenAIEmbeddingComponent(openai_api_key)
    embedding_component.build(model_id="text-embedding-ada-002")
    await embedding_service.initialize_faiss_store(embedding_component, dimension=2056)
    return {"status": "Faiss store initialized"}


@router.post("/add-to-faiss", response_model=EmbeddingMultipleResponse)
async def add_to_faiss_store(
        texts: List[str],
        session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    embedding_service = EmbeddingService(session)
    embeddings = await embedding_service.add_to_faiss_store(texts)
    return EmbeddingMultipleResponse(embeddings=embeddings)


@router.post("/rag-open-ai")
async def rag_open_ai(
        query: str,
        store_name: str,
        top_k: int = 5,
        session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        store_service = StoreService(session)
        chat_service = ChatService(session)

        files = store_service.list_files(store_name)
        documents = store_service.load_documents(files)
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)

        if not docs:
            raise ValueError("No documents were split into chunks")

        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OpenAI API key is not set in the environment")
        embeddings = OpenAIEmbeddings(api_key=openai_api_key)
        db = await FAISS.afrom_documents(docs, embeddings)
        matching_docs = await db.asimilarity_search(query, k=top_k)

        if not matching_docs:
            raise ValueError("No matching documents found")

        retriever = db.as_retriever()
        llm_instance = chat_service.get_llm_openai_instance(model_id="gpt-3.5-turbo", max_tokens=600, temperature=0.1)
        qa_chain = RetrievalQA.from_chain_type(llm=llm_instance, chain_type="stuff", retriever=retriever)

        inputs = {"query": query, "input_documents": matching_docs}
        try:
            answer = qa_chain.invoke(inputs)
            result = answer['result'] if 'result' in answer else answer
        except Exception as e:
            result = "Error generating response from QA chain"
        return {"response": result}
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))