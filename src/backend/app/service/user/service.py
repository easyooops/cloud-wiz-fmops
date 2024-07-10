# services/user_service.py
from typing import Optional
from fastapi import HTTPException
from sqlmodel import Session, select
from datetime import datetime

from app.service.user.model import User

class UserService:
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_email(self, email: str) -> User:
        return self.session.query(User).filter(User.email == email).first()

    def create_user(self, name: str, email: str) -> User:
        try:
            new_user = User(username=name, email=email)
            new_user.creator_id = new_user.user_id
            new_user.updater_id = new_user.user_id
            self.session.add(new_user)
            self.session.commit()
            self.session.refresh(new_user)
            return new_user
        except Exception as e:
            raise e

    def update_last_login(self, user: User):
        try:
            user.last_login = datetime.now()
            user.updated_at = datetime.now()
            user.updater_id = user.user_id            
            self.session.add(user)
            self.session.commit()
        except Exception as e:
            raise e