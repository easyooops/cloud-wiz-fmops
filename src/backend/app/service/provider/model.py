from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Provider(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str = Field(index=True)
    description: Optional[str] = Field(default=None, index=True)
    logo: Optional[str] = Field(default=None)
    type: str
    sort_order: int
    is_deleted: bool = Field(default=False)
    creator_id: int
    created_at: datetime = Field(default_factory=datetime.now)
    updater_id: Optional[int] = Field(default=None)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)

    __tablename__ = 'providers' 