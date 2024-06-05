from fastapi import APIRouter
from app.api.v1 import provider, inquiry, auth, agent, chain, chat, model, credential, store

api_router = APIRouter()

api_router.include_router(auth.router, tags=["auth"], prefix="/auth")
api_router.include_router(agent.router, tags=["agent"], prefix="/agent")
api_router.include_router(chain.router, tags=["chain"], prefix="/chain")
api_router.include_router(provider.router, tags=["provider"], prefix="/provider")
api_router.include_router(credential.router, tags=["credential"], prefix="/credential")
api_router.include_router(inquiry.router, tags=["inquiry"], prefix="/inquiry")
api_router.include_router(store.router, tags=["store"], prefix="/store")

api_router.include_router(chat.router, tags=["chat"], prefix="/chat")
api_router.include_router(model.router, tags=["model"], prefix="/model")