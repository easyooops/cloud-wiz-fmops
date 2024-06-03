from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
import socketio
from multiprocess import cpu_count

from app.core.config import Settings, settings
from app.api import api_router

class AuthenticationMiddleware(TrustedHostMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 인증 확인 로직
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
            # 예외 처리 및 사용자 정의 응답 생성
            return JSONResponse(status_code=500, content={"error": "An unexpected error occurred"})

class CustomMiddleware(TrustedHostMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 요청 처리 전에 수행할 작업
        print("Before handling request")
        response = await call_next(request)
        # 응답 처리 후에 수행할 작업
        print("After handling request")
        return response
    
def get_workers(workers=None):
    if workers == -1 or workers is None:
        workers = (cpu_count() * 2) + 1
    return workers

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
    
    app.include_router(api_router, prefix=settings.API_V1_STR)

    @app.get("/")
    async def welcome():
        return {"message": "Hello, World!"}
    
    return app

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        create_app,
        host="127.0.0.1",
        port=8000,
        workers=get_workers(),
        log_level="error",
        reload=True,
        loop="asyncio",
    )