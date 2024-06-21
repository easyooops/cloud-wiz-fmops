from langchain_openai import OpenAIEmbeddings
from app.components.Embedding.Base import AbstractEmbeddingComponent


class OpenAIEmbeddingComponent(AbstractEmbeddingComponent):
    def __init__(self, openai_api_key: str):
        super().__init__()
        self.openai_api_key = openai_api_key

    def configure(self):
        self.model_instance = OpenAIEmbeddings(api_key=self.openai_api_key)

    # def execute_embed_query(self, input_text):
    #     if self.model_instance is None:
    #         raise ValueError("Model instance is not initialized. Call the configure method first.")
    #     return self.model_instance.embed_query(input_text)

    def execute_embed_query(self, input_text: str) -> list[float]:
        if self.model_instance is None:
            raise ValueError("Model instance is not initialized. Call the configure method first.")
        result = self.model_instance.embed_query(input_text)
        if isinstance(result, list) and all(isinstance(i, float) for i in result):
            return result
        else:
            raise ValueError("Unexpected return type from embed_query")

    # def execute_embed_documents(self, documents: list):
    #     if self.model_instance is None:
    #         raise ValueError("Model instance is not initialized. Call the configure method first.")
    #     return self.model_instance.embed_documents(documents)

    def execute_embed_documents(self, documents: list) -> list[list[float]]:
        if self.model_instance is None:
            raise ValueError("Model instance is not initialized. Call the configure method first.")
        return self.model_instance.embed_documents(documents)
