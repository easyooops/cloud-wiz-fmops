import os
import boto3
import pandas as pd
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException
from langchain_core.documents import Document
from sqlmodel import Session
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader, Docx2txtLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter
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
):
    try:
        s3_client = boto3.client('s3')
        response = s3_client.list_objects_v2(Bucket=os.getenv("AWS_S3_BUCKET_STORE_NAME"), Prefix=f"{store_name}/")
        files = [content['Key'] for content in response.get('Contents', []) if content['Key'].endswith(('.txt', '.pdf', '.csv', '.docx', '.xlsx'))]

        if not files:
            raise ValueError("No documents found in the specified store")

        documents = []
        for s3_file_key in files:
            local_file_path = f"/tmp/{s3_file_key.split('/')[-1]}"
            s3_client.download_file(os.getenv("AWS_S3_BUCKET_STORE_NAME"), s3_file_key, local_file_path)

            if local_file_path.endswith('.txt'):
                loader = TextLoader(local_file_path)
                documents.extend(loader.load())
            elif local_file_path.endswith('.pdf'):
                loader = PyPDFLoader(local_file_path)
                documents.extend(loader.load())
            elif local_file_path.endswith('.csv'):
                loader = CSVLoader(local_file_path)
                documents.extend(loader.load())
            elif local_file_path.endswith('.docx'):
                loader = Docx2txtLoader(local_file_path)
                documents.extend(loader.load())
            elif local_file_path.endswith('.xlsx'):
                xlsx = pd.ExcelFile(local_file_path)
                for sheet_name in xlsx.sheet_names:
                    df = pd.read_excel(xlsx, sheet_name=sheet_name)
                    full_text = df.to_string(index=False)
                    documents.append(Document(page_content=full_text, metadata={"source": f"{local_file_path} - {sheet_name}"}))
            else:
                raise ValueError(f"Unsupported file format: {local_file_path}")

        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)

        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OpenAI API key is not set in the environment")

        embeddings = OpenAIEmbeddings(api_key=openai_api_key)
        db = await FAISS.afrom_documents(docs, embeddings)
        matching_docs = await db.asimilarity_search(query, k=top_k)
        llm = ChatOpenAI(api_key=openai_api_key, model="gpt-3.5-turbo", temperature=0)
        qa_chain = RetrievalQA.from_chain_type(llm, retriever=db.as_retriever())

        inputs = {"query": query, "input_documents": matching_docs}
        answer = qa_chain.invoke(inputs)
        result = answer['result'] if 'result' in answer else answer

        return {"results": result}

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))