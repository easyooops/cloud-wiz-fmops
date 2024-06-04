from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class AgentCreate(BaseModel):
    user_id: int
    agent_type: str
    title: str
    description: str
    is_visible_in_marketplace: bool
    is_deleted: bool = False
    creator_id: int
    created_at: datetime = datetime.now()
    updater_id: int
    updated_at: datetime = datetime.now()

class AgentUpdate(BaseModel):
    user_id: Optional[int] = None
    agent_type: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    is_visible_in_marketplace: Optional[bool] = None
    is_deleted: Optional[bool] = None
    creator_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updater_id: Optional[int] = None
    updated_at: Optional[datetime] = None
