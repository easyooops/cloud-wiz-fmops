from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class StoreCreate(BaseModel):
    store_name: str
    description: str
    creator_id: int
    user_id: UUID

class StoreUpdate(BaseModel):
    store_name: Optional[str] = None
    description: Optional[str] = None
    creator_id: Optional[int] = None
