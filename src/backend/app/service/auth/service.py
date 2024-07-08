from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
import boto3

from app.core.factories import get_database
from app.core.interface.service import ServiceType
from app.service.user.service import UserService
from app.core.config import settings
from sqlmodel import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_cognito_client():
    return boto3.client("cognito-idp", region_name=settings.COGNITO_REGION)

def get_user_from_token(token: str = Depends(oauth2_scheme), session: Session = Depends(get_database)):
    try:
        client = get_cognito_client()
        response = client.get_user(AccessToken=token)
        username = response["Username"]
        email = next(attr["Value"] for attr in response["UserAttributes"] if attr["Name"] == "email")
        
        user_service = UserService(session)
        user = user_service.get_user_by_username(username)
        if not user:
            user = user_service.create_user(username, email)
        user_service.update_last_login(user)
        return user
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")
