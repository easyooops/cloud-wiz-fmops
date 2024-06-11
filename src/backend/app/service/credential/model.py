from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4

class Credential(SQLModel, table=True):
    credential_id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    user_id: UUID = Field(index=True)
    provider_id: UUID = Field(index=True)
    credential_name: str
    access_key: Optional[str] = None
    secret_key: Optional[str] = None
    session_key: Optional[str] = None
    access_token: Optional[str] = None
    api_key: Optional[str] = None
    api_endpoint: Optional[str] = None
    is_deleted: bool = Field(default=False)
    creator_id: UUID
    created_at: datetime = Field(default_factory=datetime.now)
    updater_id: Optional[UUID] = Field(default=None)
    updated_at: datetime = Field(default_factory=datetime.now)

    __tablename__ = 'credentials'
