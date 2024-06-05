import os
from dotenv import load_dotenv
import boto3

from langchain_community.llms import Bedrock
from langchain_aws import BedrockLLM
from langchain_core.callbacks import StreamingStdOutCallbackHandler
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

from app.components.LLM.Base import BaseLLMComponent

class BedrockLLMComponent(BaseLLMComponent):
    def __init__(self, model_id):
        super().__init__()
        self.model_id = model_id
        self.llm = None
        self.conversation = None

    def load_credentials(self):
        load_dotenv()
        self.aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.aws_region = os.getenv("AWS_REGION")

    def create_boto3_session(self):
        self.load_credentials()
        session = boto3.Session(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.aws_region
        )
        return session
    
    def build(self):
        session = self.create_boto3_session()
        # llm = Bedrock(
        #     credentials_profile_name=session,
        #     model_id=self.model_id,
        #     streaming=True,
        #     callbacks=[StreamingStdOutCallbackHandler()],
        # )
        llm = BedrockLLM(
            region_name=self.aws_region,
            # credentials_profile_name=session,
            model_id=self.model_id,
            streaming=True,
            callbacks=[StreamingStdOutCallbackHandler()],
        )        
        self.conversation = ConversationChain(
            llm=llm, verbose=True, memory=ConversationBufferMemory()
        )

    def run(self, prompt):
        if self.conversation is None:
            raise ValueError("LLM is not initialized. Call the build method first.")
        return self.conversation.predict(input=prompt)