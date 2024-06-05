import os
from fastapi import HTTPException
from sqlmodel import Session
from app.components.Chat.OpenAI import ChatOpenAIComponent

class ChatService:
    def __init__(self, session: Session):
        self.session = session

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
