from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Agent(SQLModel, table=True):
    agent_id: Optional[int] = Field(default=None, primary_key=True, index=True)
    user_id: int = Field(index=True)
    agent_type: str
    title: str
    description: str
    is_visible_in_marketplace: bool
    is_deleted: bool
    creator_id: int
    created_at: datetime = Field(default_factory=datetime.now)
    updater_id: Optional[int] = Field(default=None)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)

    __tablename__ = 'agent'
