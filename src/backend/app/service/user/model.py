# models.py
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True, index=True)
    username: str = Field(index=True)
    email: str = Field(index=True)
    last_login: datetime = Field(default_factory=datetime.now)    
    is_deleted: bool = Field(default=False)
    creator_id: int
    created_at: datetime = Field(default_factory=datetime.now)
    updater_id: Optional[int] = Field(default=None)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)

    __tablename__ = 'user'    