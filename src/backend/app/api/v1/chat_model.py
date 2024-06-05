import os
from http.client import HTTPException
from dotenv import load_dotenv
from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import Optional

from app.core.interface.service import ServiceType
from app.core.factories import get_database
from app.core.exception import internal_server_error
from app.api.v1.schemas.chat import ChatResponse, ChatRequest
from app.service.chat.service import ChatService

router = APIRouter()
load_dotenv()

# OpenAI
@router.post("/chat-openai", response_model=ChatResponse)
def get_openai_chat_answer(
        query: Optional[str] = None,
        session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        if not query:
            raise HTTPException(status_code=400, detail="Query parameter is required")

        chat_service = ChatService(session)
        response = chat_service.get_llm_openai_response(query)
        return ChatResponse(answer=response)
    except Exception as e:
        raise internal_server_error(e)
