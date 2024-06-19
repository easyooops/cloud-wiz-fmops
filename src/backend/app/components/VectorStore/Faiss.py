import faiss
import numpy as np
import asyncio
from app.components.Embedding.Base import AbstractEmbeddingComponent


class FaissAsyncVectorStore:
    def __init__(self, embedding_component: AbstractEmbeddingComponent):
        self.embedding_component = embedding_component
        self.index = None

    async def initialize(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)

    async def add_embeddings(self, texts: list):
        loop = asyncio.get_event_loop()
        embeddings = await loop.run_in_executor(None, self.embedding_component.execute_embed_documents, texts)
        embeddings = np.array(embeddings).astype('float32')
        self.index.add(embeddings)
        return embeddings

    async def query(self, query_text: str, top_k: int):
        loop = asyncio.get_event_loop()
        query_embedding = await loop.run_in_executor(None, self.embedding_component.execute_embed_query, query_text)
        query_embedding = np.array([query_embedding]).astype('float32')
        distances, indices = self.index.search(query_embedding, top_k)
        return distances, indices
