import os
import boto3
from app.components.Embedding.Base import AbstractEmbeddingComponent
from langchain_community.embeddings import BedrockEmbeddings

class BedrockEmbeddingComponent(AbstractEmbeddingComponent):
    def __init__(self):
        super().__init__()
        self.aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.aws_region = os.getenv("AWS_REGION")

        self.boto3_session = boto3.Session(
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.aws_region
        )

    def configure(self, model_id: str):
        self.model_instance = BedrockEmbeddings(
            model_id=model_id,
            client=self.boto3_session.client('bedrock-runtime')
        )

    def execute_embed_query(self, input_text):
        if self.model_instance is None:
            raise ValueError("Model instance is not initialized. Call the configure method first.")
        return self.model_instance.embed_query(input_text)

    def execute_embed_documents(self, documents: list):
        if self.model_instance is None:
            raise ValueError("Model instance is not initialized. Call the configure method first")
        return self.model_instance.embed_documents(documents)
