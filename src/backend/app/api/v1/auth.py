import logging
import requests
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.exception import authentication_error
from app.service.auth.service import AuthService
from app.service.user.model import User
from app.api.v1.schemas.auth import UserCreate  # Adjust the import if necessary
from app.core.factories import get_database
from app.service.user.service import UserService
from app.service.init.service import InitDataService

router = APIRouter()

@router.post("/")
async def authenticate_with_google(
    auth: UserCreate, 
    session: Session = Depends(get_database)
):
    auth_service = AuthService()
    user_service = UserService(session)

    try:
        user_info = auth_service.verify_google_token(auth.token)

        user = user_service.get_user_by_email(user_info['email'])

        jwt_token = auth_service.create_access_token(user_info)

        if not user:
            user = user_service.create_user(user_info['name'], user_info['email'])
            data_service = InitDataService(session, user.user_id)
            data_service.run()

        user_service.update_last_login(user, auth.token)

        return {
            "accessToken": jwt_token,
            "userName": user.username,
            "userId": user.user_id,
            "refreshToken": user_info.get('refresh_token'),
            "clientId": user_info.get('client_id'),
            "clientSecret": user_info.get('client_secret'),
            "tokenUri": user_info.get('token_uri')
        }
    
    except Exception as e:
        raise authentication_error(e)

@router.post("/logout")
async def logout(
    auth: UserCreate,
    session: Session = Depends(get_database)
):
    # Perform logout actions such as invalidating tokens, clearing sessions, etc.
    try:
        # Verify the token or extract user info as needed
        # Example: auth_service.verify_google_token(token)

        # Revoke the Google token using Google's OAuth 2.0 token revocation endpoint
        revoke_token_url = "https://accounts.google.com/o/oauth2/revoke"
        revoke_params = {
            'token': auth.token
        }
        response = requests.post(revoke_token_url, params=revoke_params)

        # Check if token revocation was successful
        if response.status_code == 200:
            return {"message": "Successfully logged out and revoked token"}
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to revoke token")

    except Exception as e:
        raise authentication_error(e)
