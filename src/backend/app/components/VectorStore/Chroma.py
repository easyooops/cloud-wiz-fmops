import os
from app.components.VectorStore.Base import AbstractVectorStoreComponent
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings

class ChromaVectorStoreComponent(AbstractVectorStoreComponent):
    def __init__(self):
        super().__init__()
        self.embedding_function = None
        self.db = None
        self.persist_directory = None
        self.docs = None

    def initialize(self, docs, model_name="all-MiniLM-L6-v2", persist_directory=None):
        self.embedding_function = SentenceTransformerEmbeddings(model_name=model_name)
        self.persist_directory = persist_directory
        self.docs = docs
        if persist_directory:
            self.db = Chroma.from_documents(docs, self.embedding_function, persist_directory=persist_directory)
        else:
            self.db = Chroma.from_documents(docs, self.embedding_function)

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
        self.initialize(self.docs, model_name="all-MiniLM-L6-v2", persist_directory=self.persist_directory)
