from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class CredentialCreate(BaseModel):
    user_id: UUID
    provider_id: UUID
    auth_name: str
    auth_key: str
    auth_key2: Optional[str] = None
    auth_key3: Optional[str] = None
    auth_user: Optional[str] = None
    auth_token: Optional[str] = None
    auth_endpoint: Optional[str] = None
    is_deleted: bool = False
    creator_id: int
    created_at: datetime = datetime.now()
    updater_id: int
    updated_at: datetime = datetime.now()

class CredentialUpdate(BaseModel):
    auth_name: Optional[str] = None
    auth_key: Optional[str] = None
    auth_key2: Optional[str] = None
    auth_key3: Optional[str] = None
    auth_user: Optional[str] = None
    auth_token: Optional[str] = None
    auth_endpoint: Optional[str] = None
    is_deleted: Optional[bool] = None
    creator_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updater_id: Optional[int] = None
    updated_at: Optional[datetime] = None
