import os
import time
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec
from app.components.VectorStore.Base import AbstractVectorStoreComponent

class PineconeVectorStoreComponent(AbstractVectorStoreComponent):
    def __init__(self):
        super().__init__()
        self.embedding_function = None
        self.index_name = None
        self.api_key = os.getenv("PINECONE_API_KEY")
        self.pc = Pinecone(api_key=self.api_key)

    def initialize(self, docs, model_name="all-MiniLM-L6-v2", index_name="langchain-index"):
        self.embedding_function = OpenAIEmbeddings()
        self.index_name = index_name
        existing_indexes = [index_info["name"] for index_info in self.pc.list_indexes()]

        if index_name not in existing_indexes:
            self.pc.create_index(
                name=index_name,
                dimension=1536,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )
            while not self.pc.describe_index(index_name).status["ready"]:
                time.sleep(1)

        self.index = self.pc.Index(index_name)
        self.db = PineconeVectorStore.from_documents(docs, self.embedding_function, index_name=index_name)

    def add_embeddings(self, docs):
        if self.db:
            self.db.add_texts(docs)
        else:
            raise ValueError("Database is not initialized. Call the initialize method first.")

    def query(self, query, top_k: int):
        if self.db:
            results = self.db.similarity_search(query, top_k=top_k)
            return results
        else:
            raise ValueError("Database is not initialized. Call the initialize method first.")
