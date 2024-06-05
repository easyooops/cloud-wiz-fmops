from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4

class Provider(SQLModel, table=True):
    provider_id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
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