import faiss
import numpy as np
from app.components.VectorStore.Base import AbstractVectorStoreComponent

class FaissVectorStoreComponent(AbstractVectorStoreComponent):
    def __init__(self):
        super().__init__()
        self.dimension = None

    def initialize(self, dimension):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)

    def add_embeddings(self, embeddings: list):
        vectors = np.array(embeddings).astype('float32')
        self.index.add(vectors)

    def query(self, query_vector: list[float], top_k: int):
        query_vector_np = np.array([query_vector]).astype('float32')
        distances, indices = self.index.search(query_vector_np, top_k)
        return indices[0]

    def reset_index(self):
        if self.dimension is not None:
            self.index = faiss.IndexFlatL2(self.dimension)
        else:
            raise ValueError("Dimension not set. Initialize the index first.")

    def save_index(self, file_path):
        if self.index:
            faiss.write_index(self.index, file_path)
        else:
            raise ValueError("Index is not initialized.")

    def load_index(self, file_path):
        self.index = faiss.read_index(file_path)

