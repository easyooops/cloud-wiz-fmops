# services/user_service.py
from typing import Optional
from fastapi import HTTPException
from sqlmodel import Session, select
from datetime import datetime

from app.service.user.model import User

class UserService:
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_username(self, username: str) -> Optional[User]:
        statement = select(User).where(User.username == username)
        return self.session.execute(statement).first()

    def create_user(self, username: str, email: str) -> User:
        new_user = User(username=username, email=email)
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user

    def update_last_login(self, user: User):
        user.last_login = datetime.now()
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
