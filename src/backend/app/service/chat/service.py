import os
from fastapi import HTTPException
from sqlmodel import Session
from typing import Optional
from app.components.Chat.OpenAI import ChatOpenAIComponent
from app.components.Chat.Bedrock import ChatBedrockComponent
from app.components.Chat.QueryTuning import QueryTuningComponent

class ChatService:
    def __init__(self, session: Session):
        self.session = session

    # OpenAI
    def get_llm_openai_response(self, query: str):
        try:
            openai_api_key = os.getenv("OPENAI_API_KEY")
            if not openai_api_key:
                raise ValueError("OpenAI API key is not set in the environment variables")

            openai_component = ChatOpenAIComponent(openai_api_key)
            openai_component.configure(temperature=0.7)
            response = openai_component.execute(query)
            return response
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    # Bedrock
    def get_llm_bedrock_response(self, model_id: str, query: str):
        try:
            aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
            aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
            aws_region = os.getenv("AWS_REGION")
            if not all([aws_access_key, aws_secret_access_key, aws_region]):
                raise ValueError("AWS credentials or region are not set in the environment variables")

            bedrock_component = ChatBedrockComponent()
            bedrock_component.configure(model_id=model_id)
            response = bedrock_component.execute(query)
            return response
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    # QueryTuning (OpenAI + Bedrock)
    def openai_chaining(self, query: str, model_id: Optional[str] = None, service_type: str = "openai"):
        try:
            openai_api_key = os.getenv("OPENAI_API_KEY")
            aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
            aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
            aws_region = os.getenv("AWS_REGION")

            if not all([openai_api_key, aws_access_key, aws_secret_access_key, aws_region]):
                raise ValueError("API keys or AWS credentials are not set in the environment variables")

            # 쿼리 유형 감지 및 전처리
            refinement_component = QueryTuningComponent(openai_api_key)
            refinement_component.configure()
            refined_query = refinement_component.execute(query)

            # 서비스 유형에 따른 컴포넌트 선택
            if service_type == "bedrock":
                bedrock_component = ChatBedrockComponent()
                bedrock_component.configure(model_id=model_id)
                response = bedrock_component.execute(refined_query)
            else:
                openai_component = ChatOpenAIComponent(openai_api_key)
                openai_component.configure(temperature=0.7)
                response = openai_component.execute(refined_query)

            return response
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))