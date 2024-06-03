from fastapi import APIRouter
from app.api.v1 import provider

api_router = APIRouter()

api_router.include_router(provider.router, tags=["provider"], prefix="/provider")