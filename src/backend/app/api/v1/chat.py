import os
from typing import Optional
from fastapi import APIRouter
from getpass import getpass

from app.core.exception import internal_server_error
from app.api.v1.schemas.chat import ChatResponse
from app.components.LLM.OpenAI import OpenAILLMComponent
from app.components.LLM.Ollama import OllamaLLMComponent
from app.components.LLM.Bedrock import BedrockLLMComponent

router = APIRouter()

@router.get("/llms-openai", response_model=ChatResponse)
def get_llm_openai_answer(
    query: Optional[str] = None
):
    try:
        openai_api_key = "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"
        openai_component = OpenAILLMComponent(openai_api_key)
        openai_component.build(temperature=0.5)

        return ChatResponse(answer=openai_component.run(query))
    except Exception as e:
        raise internal_server_error(e)

@router.get("/llms-ollama", response_model=ChatResponse)
def get_llm_ollama_answer(
    query: Optional[str] = None
):
    try:
        ollama_component = OllamaLLMComponent()
        ollama_component.build()

        return ChatResponse(answer=ollama_component.run(query))
    except Exception as e:
        raise internal_server_error(e)
    
@router.get("/llms-bedrock", response_model=ChatResponse)
def get_llm_bedrock_answer(
    model: str = None,
    query: Optional[str] = None
):
    try:
        # model = "amazon.titan-text-express-v1"
        bedrock_component = BedrockLLMComponent(model)
        bedrock_component.build()

        return ChatResponse(answer=bedrock_component.run(query))
    except Exception as e:
        raise internal_server_error(e)    