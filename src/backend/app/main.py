import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
import socketio
from multiprocess import cpu_count
from sqlmodel import SQLModel, Session, create_engine
from alembic import command
from alembic.config import Config

from app.core.config import settings
from app.api import api_router
from app.initial_data import init_db

from ddtrace.llmobs import LLMObs

from app.core.util.logging import LoggingConfigurator

class AuthenticationMiddleware(TrustedHostMiddleware):
    async def dispatch(self, request: Request, call_next):
        # if not authenticate(request):
        #     return JSONResponse(status_code=401, content={"message": "Unauthorized"})
        response = await call_next(request)
        return response

class AddHeaderMiddleware(TrustedHostMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Custom-Header"] = "Custom Value"
        return response
        
class CustomErrorHandlerMiddleware(TrustedHostMiddleware):
    async def dispatch(self, request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": "An unexpected error occurred"})

class CustomMiddleware(TrustedHostMiddleware):
    async def dispatch(self, request: Request, call_next):
        print("Before handling request")
        response = await call_next(request)
        print("After handling request")
        return response
    
def get_workers(workers=None):
    if workers == -1 or workers is None:
        workers = (cpu_count() * 2) + 1
    return workers

def create_db_and_tables():
    engine = create_engine(os.getenv("DATABASE_URL"), echo=True)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        init_db(session)

def configure_datadog():
    LLMObs.enable(
        ml_app=os.getenv("DATADOG_ML_APP"),
        api_key=os.getenv("DATADOG_API_KEY"),
        site=os.getenv("DATADOG_SITE"),
        agentless_enabled=True,
        integrations_enabled=True,
        )
    
def create_app():
    
    app = FastAPI()
    
    sio = socketio.AsyncServer(
                async_mode="asgi", 
                cors_allowed_origins="*", 
                logger=True
            )
    app.mount("/ws", socketio.ASGIApp(sio))

    app.add_middleware(
        TrustedHostMiddleware, allowed_hosts=["*"]
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],    # 허용할 오리진을 설정합니다.
        allow_credentials=True, # 자격 증명 허용 여부를 설정합니다.
        allow_methods=["*"],    # 허용할 HTTP 메서드를 설정합니다.
        allow_headers=["*"]     # 허용할 HTTP 헤더를 설정합니다.
    )
    app.add_middleware(AuthenticationMiddleware)
    app.add_middleware(AddHeaderMiddleware)    
    app.add_middleware(CustomErrorHandlerMiddleware)

    alembic_cfg = Config("alembic.ini")

    @app.on_event("startup")
    def on_startup():
        # create_db_and_tables()
        command.upgrade(alembic_cfg, "head")

    LoggingConfigurator()
    configure_datadog()
    
    app.include_router(api_router, prefix=settings.API_V1_STR)

    @app.get("/health")
    async def welcome():
        return {"message": "Hello, World!"}
    
    return app
# uvicorn
# if __name__ == "__main__":
#     import uvicorn
    
#     uvicorn.run(
#         create_app,
#         host="127.0.0.1",
#         port=8000,
#         workers=get_workers(),        
#         log_config="uvicorn_logging_config.yaml",
#         log_level="debug", 
#         access_log=True,
#         reload=True,
#         loop="asyncio",
#     )
if __name__ == "__main__":
    create_app()