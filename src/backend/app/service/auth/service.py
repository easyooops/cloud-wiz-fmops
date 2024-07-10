import logging
import os
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta
from google.auth.transport import requests
from google.oauth2 import id_token
from fastapi import Depends, HTTPException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
load_dotenv()

class AuthService:
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")    # 구글 클라이언트 ID로 교체
    AUTH_SECRET_KEY = os.getenv("AUTH_SECRET_KEY")      # 비밀 키
    ALGORITHM = "HS256"                                 # 사용할 알고리즘
    ACCESS_TOKEN_EXPIRE_MINUTES = 30                    # 엑세스 토큰 유효 시간
    REFRESH_TOKEN_EXPIRE_DAYS = 7

    @staticmethod
    def verify_google_token(token: str):
        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), AuthService.GOOGLE_CLIENT_ID)

            if idinfo['aud'] != AuthService.GOOGLE_CLIENT_ID:
                raise ValueError('Invalid client ID.')
            
            user_id = idinfo['sub']
            email = idinfo['email']
            name = idinfo['family_name']

            return {'user_id': user_id, 'email': email, 'name': name}
        except ValueError as e:
            raise HTTPException(status_code=403, detail="Invalid token")

    @staticmethod
    def create_access_token(data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=AuthService.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, AuthService.AUTH_SECRET_KEY, algorithm=AuthService.ALGORITHM)
        return encoded_jwt

    @staticmethod
    def create_refresh_token(data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(days=AuthService.REFRESH_TOKEN_EXPIRE_DAYS)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, AuthService.AUTH_SECRET_KEY, algorithm=AuthService.ALGORITHM)

    @staticmethod
    def verify_jwt_token(token: str):
        try:
            payload = jwt.decode(token, AuthService.AUTH_SECRET_KEY, algorithms=[AuthService.ALGORITHM])
            user_id: str = payload.get("user_id")
            if user_id is None:
                raise HTTPException(status_code=401, detail="Invalid credentials")
            return payload
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid credentials")

def get_current_user(token: str = Depends(oauth2_scheme)):
    return AuthService.verify_jwt_token(token)