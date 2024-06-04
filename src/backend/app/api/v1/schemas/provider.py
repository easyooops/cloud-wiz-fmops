from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ProviderCreate(BaseModel):
    name: str
    description: str
    logo: str
    type: str
    sort_order: int
    is_deleted: bool = False
    creator_id: int
    created_at: datetime = datetime.now()
    updater_id: int
    updated_at: datetime = datetime.now()

class ProviderUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None
    type: Optional[str] = None
    sort_order: Optional[int] = None
    is_deleted: Optional[bool] = None
    creator_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updater_id: Optional[int] = None
    updated_at: Optional[datetime] = None    