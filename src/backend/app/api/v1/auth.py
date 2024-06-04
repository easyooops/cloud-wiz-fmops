from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from app.core.exception import authentication_error
from app.service.auth.service import get_user_from_token
from app.service.user.model import User


router = APIRouter()

@router.get("/me", response_model=User)
def read_users_me(current_user: User = Depends(get_user_from_token)):
    return current_user

@router.post("/auth")
def authenticate(token: str):
    try:
        get_user_from_token(token)
        return RedirectResponse(url="/dashboard")
    except Exception as e:
        raise authentication_error(e)
