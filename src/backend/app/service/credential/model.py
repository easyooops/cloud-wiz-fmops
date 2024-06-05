from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID

class Credential(SQLModel, table=True):
    user_id: UUID = Field(primary_key=True, index=True)
    provider_id: UUID = Field(primary_key=True, index=True)
    auth_name: str
    auth_key: str
    auth_key2: Optional[str] = None
    auth_key3: Optional[str] = None
    auth_user: Optional[str] = None
    auth_token: Optional[str] = None
    auth_endpoint: Optional[str] = None
    is_deleted: bool = Field(default=False)
    creator_id: int
    created_at: datetime = Field(default_factory=datetime.now)
    updater_id: int
    updated_at: datetime = Field(default_factory=datetime.now)

    __tablename__ = 'credentials'
