from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from app.service.model.service import (
    OpenAIService, OllamaService, AnthropicService,
    AL21LabsService, CohereService, TitanService
)
from app.core.exception import internal_server_error

router = APIRouter()

SERVICE_CLASSES = {
    "openai": OpenAIService,
    "ollama": OllamaService,
    "anthropic": AnthropicService,
    "al21labs": AL21LabsService,
    "cohere": CohereService,
    "titan": TitanService
}

@router.get("/{model_name}/models")
def get_models(model_name: str):
    try:
        service_class = SERVICE_CLASSES.get(model_name.lower())
        if not service_class:
            raise HTTPException(status_code=400, detail="Invalid model name")
        
        service = service_class()
        return service.get_models()
    except Exception as e:
        raise internal_server_error(e)
