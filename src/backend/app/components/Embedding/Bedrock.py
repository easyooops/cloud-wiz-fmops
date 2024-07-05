import boto3
from app.components.Embedding.Base import AbstractEmbeddingComponent
from langchain_community.embeddings import BedrockEmbeddings


class BedrockEmbeddingComponent(AbstractEmbeddingComponent):
    def __init__(self, aws_access_key, aws_secret_access_key, aws_region):
        super().__init__()
        self.aws_access_key = aws_access_key
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_region = aws_region

        self.boto3_session = boto3.Session(
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.aws_region
        )

    def build(self, model_id: str):

        if not model_id:
            model_id = "amazon.titan-embed-text-v1"

        self.model_instance = BedrockEmbeddings(
            model_id=model_id,
            client=self.boto3_session.client('bedrock-runtime')
        )

    def run_embed_query(self, input_text: str) -> list[float]:
        if self.model_instance is None:
            raise ValueError("Model instance is not initialized. Call the configure method first.")
        result = self.model_instance.embed_query(input_text)
        if isinstance(result, list) and all(isinstance(i, float)for i in result):
            return result
        else:
            raise ValueError("Unexpected return type from embed_query")

    def run_embed_documents(self, documents: list):
        if self.model_instance is None:
            raise ValueError("Model instance is not initialized. Call the configure method first")
        return self.model_instance.embed_documents(documents)
