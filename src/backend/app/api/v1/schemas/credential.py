from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class CredentialBase(BaseModel):
    user_id: UUID
    provider_id: UUID
    credential_id: UUID
    credential_name: str
    access_key: Optional[str] = None
    secret_key: Optional[str] = None
    session_key: Optional[str] = None
    access_token: Optional[str] = None
    api_key: Optional[str] = None
    api_endpoint: Optional[str] = None
    provider_name: Optional[str] = None
    provider_company: Optional[str] = None
    provider_desc: Optional[str] = None
    provider_logo: Optional[str] = None
    provider_type: Optional[str] = None
    provider_ord: Optional[str] = None
    
class CredentialProviderJoin(CredentialBase):
    provider_name: Optional[str] = None
    provider_company: Optional[str] = None
    provider_desc: Optional[str] = None
    provider_logo: Optional[str] = None
    provider_type: Optional[str] = None
    provider_ord: Optional[int] = None

class CredentialCreate(BaseModel):
    user_id: UUID
    provider_id: UUID
    credential_name: str
    access_key: Optional[str] = None
    secret_key: Optional[str] = None
    session_key: Optional[str] = None
    access_token: Optional[str] = None
    api_key: Optional[str] = None
    api_endpoint: Optional[str] = None
    is_deleted: bool = False
    creator_id: UUID
    created_at: datetime = datetime.now()
    updater_id: UUID
    updated_at: datetime = datetime.now()

class CredentialUpdate(BaseModel):
    credential_name: Optional[str] = None
    access_key: Optional[str] = None
    secret_key: Optional[str] = None
    session_key: Optional[str] = None
    access_token: Optional[str] = None
    api_key: Optional[str] = None
    api_endpoint: Optional[str] = None
    is_deleted: Optional[bool] = None
    creator_id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updater_id: Optional[UUID] = None
    updated_at: Optional[datetime] = None
