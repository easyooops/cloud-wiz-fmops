import logging
import os
import chromadb
from langchain_openai import OpenAIEmbeddings
from app.components.VectorStore.Base import AbstractVectorStoreComponent
from langchain_chroma import Chroma

class ChromaVectorStoreComponent(AbstractVectorStoreComponent):
    def __init__(self, storage_service=None):
        super().__init__()
        self.embedding_function = None
        self.db = None
        self.persist_directory = None
        self.docs = None
        self.index_name = None
        self.storage_service = storage_service

    def initialize(self, docs, embedding_function, persist_directory=None, index_name=None, storage_location=None):
        self.embedding_function = embedding_function
        self.persist_directory = persist_directory
        self.docs = docs
        self.index_name = index_name

        client = chromadb.EphemeralClient()

        if persist_directory:
            # Load existing index if available
            if self.storage_service:
                self.load_index(storage_location, persist_directory)
            if self.db is None:  # If loading index failed, create a new one
                self.db = Chroma.from_documents(
                    docs, 
                    self.embedding_function,
                    client=client,
                    persist_directory=persist_directory, 
                    collection_name=index_name
                )
        else:
            self.db = Chroma.from_documents(
                docs, 
                self.embedding_function,
                client=client,
                collection_name=index_name
            )

    def add_embeddings(self, docs):
        if self.db:
            self.db.add(docs)
        else:
            raise ValueError("Database is not initialized. Call the initialize method first.")

    def query(self, query, top_k: int):
        if self.db:
            results = self.db.similarity_search(query, top_k=top_k)
            return results
        else:
            raise ValueError("Database is not initialized. Call the initialize method first.")

    def reset_index(self):
        if self.persist_directory and os.path.exists(self.persist_directory):
            # Remove existing index files
            for file in os.listdir(self.persist_directory):
                file_path = os.path.join(self.persist_directory, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
        
        # Reinitialize the index with stored documents
        self.initialize(self.docs, persist_directory=self.persist_directory, index_name=self.index_name)

    def save_index(self, storage_location):
        if self.db:
            if not self.persist_directory:
                raise ValueError("Persist directory is not set.")
            
            # Upload each file in the persist directory to the storage service
            if self.storage_service:
                for file_name in os.listdir(self.persist_directory):
                    file_path = os.path.join(self.persist_directory, file_name)
                    if os.path.isfile(file_path):  # 파일인지 확인
                        storage_file_path = os.path.join(storage_location, file_name)
                        with open(file_path, 'rb') as file:
                            logging.warning(f"Uploading file: {file_path} to {storage_file_path}")
                            self.storage_service.upload_file(file, storage_file_path)
        else:
            raise ValueError("Database is not initialized. Call the initialize method first.")

    def load_index(self, storage_location, persist_directory):
        if self.storage_service:
            os.makedirs(persist_directory, exist_ok=True)
            files = self.storage_service.list_files(storage_location)
            for file in files:
                # 파일 이름만 가져와서 persist_directory에 저장
                file_name = os.path.basename(file['Key'])
                file_path = os.path.join(persist_directory, file_name)
                self.storage_service.download_file(file['Key'], file_path)

            client = chromadb.EphemeralClient()

            try:
                self.db = Chroma(
                    self.embedding_function,
                    persist_directory=persist_directory
                )
            except Exception as e:
                logging.warning(f"Failed to load index from {persist_directory}: {e}")
                return None
