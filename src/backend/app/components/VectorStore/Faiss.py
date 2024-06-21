import faiss
import numpy as np
import asyncio
from app.components.Embedding.Base import AbstractEmbeddingComponent


class FaissAsyncVectorStore:
    def __init__(self, embedding_component):
        self.embedding_component = embedding_component
        self.index = None

    async def initialize(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)

    async def add_embeddings(self, embeddings: list):
        vectors = np.array(embeddings).astype('float32')
        self.index.add(vectors)

    async def query(self, query_vector: list[float], top_k: int):
        query_vector_np = np.array([query_vector]).astype('float32')
        distances, indices = self.index.search(query_vector_np, top_k)
        return indices[0]  # return the indices of the nearest neighbors
