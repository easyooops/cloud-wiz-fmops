from fastapi import APIRouter
from app.api.v1 import provider, inquiry

api_router = APIRouter()

api_router.include_router(provider.router, tags=["provider"], prefix="/provider")
api_router.include_router(inquiry.router, tags=["inquiry"], prefix="/inquiry")