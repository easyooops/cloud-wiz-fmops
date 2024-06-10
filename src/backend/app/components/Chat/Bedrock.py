import os
import boto3
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from app.components.Chat.Base import AbstractLLMComponent

class ChatBedrockComponent(AbstractLLMComponent):
    def __init__(self):
        super().__init__()
        self.aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.aws_region = os.getenv("AWS_REGION")

        # boto3 로 AWS 자격증명 처리
        self.boto3_session = boto3.Session(
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.aws_region
        )

    def configure(self, model_id: str):
        self.model_instance = ChatBedrock(
            model_id=model_id,
            client=self.boto3_session.client('bedrock-runtime')

        )

    def execute(self, prompt):
        if self.model_instance is None:
            raise ValueError("Model instance is not initialized. Call the configure method first.")
        human_message = HumanMessage(content=prompt)
        response = self.model_instance.invoke([human_message])
        return response.content
