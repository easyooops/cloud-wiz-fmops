import os
from langchain_openai import OpenAIEmbeddings
from app.components.Embedding.Base import AbstractEmbeddingComponent


class OpenAIEmbeddingComponent(AbstractEmbeddingComponent):
    def __init__(self, openai_api_key: str):
        super().__init__()
        self.openai_api_key = openai_api_key

    def configure(self):
        self.model_instance = OpenAIEmbeddings(api_key=self.openai_api_key)

    def execute(self, input_text):
        if self.model_instance is None:
            raise ValueError("Model instance is not initialized. Call the configure method first.")
        return self.model_instance.embed_query(input_text)
