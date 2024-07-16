from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class StoreBase(BaseModel):
    store_id: Optional[UUID] = None
    credential_id: Optional[UUID] = None
    store_name: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None    
    user_id: Optional[UUID] = None

class StoreWithDirectory(StoreBase):
    total_size: Optional[int] = None
    file_count: Optional[int] = None

class StoreCreate(BaseModel):
    store_name: str
    description: str
    creator_id: UUID
    updater_id: UUID
    credential_id: UUID
    user_id: UUID

class StoreUpdate(BaseModel):
    store_name: Optional[str] = None
    description: Optional[str] = None
    updater_id: UUID
