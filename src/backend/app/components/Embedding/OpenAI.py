from langchain_openai import OpenAIEmbeddings
from app.components.Embedding.Base import AbstractEmbeddingComponent


class OpenAIEmbeddingComponent(AbstractEmbeddingComponent):
    def __init__(self, openai_api_key: str):
        super().__init__()
        self.openai_api_key = openai_api_key
        self.model_instance = None

    def build(self, model_id):

        if not model_id:
            model_id = "text-embedding-3-small"

        self.model_instance = OpenAIEmbeddings(
            openai_api_key=self.openai_api_key,
            model=model_id
        )

    def run_embed_query(self, input_text: str) -> list[float]:
        if self.model_instance is None:
            raise ValueError("Model instance is not initialized. Call the configure method first.")
        result = self.model_instance.embed_query(input_text)
        if isinstance(result, list) and all(isinstance(i, float) for i in result):
            return result
        else:
            raise ValueError("Unexpected return type from embed_query")

    def run_embed_documents(self, documents: list[str]) -> list[list[float]]:
        if self.model_instance is None:
            raise ValueError("Model instance is not initialized. Call the configure method first.")
        return self.model_instance.embed_documents(documents)
