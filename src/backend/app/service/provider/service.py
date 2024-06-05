from typing import List, Optional
from uuid import UUID
from fastapi import HTTPException
from sqlmodel import Session, select

from app.service.provider.model import Provider
from app.api.v1.schemas.provider import ProviderCreate, ProviderUpdate

class ProviderService:
    def __init__(self, session: Session):
        self.session = session

    def get_all_providers(self, type: Optional[str] = None, name: Optional[str] = None):
        statement = select(Provider)
        if type:
            statement = statement.where(Provider.type == type)
        if name:
            statement = statement.where(Provider.name == name)
        return self.session.exec(statement).all()

    def create_provider(self, provider_data: ProviderCreate):
        try:
            new_provider = Provider(**provider_data.model_dump())
            self.session.add(new_provider)
            self.session.commit()
            self.session.refresh(new_provider)
            return new_provider
        except Exception as e:
            raise e
        
    def update_provider(self, provider_id: UUID, provider_update: ProviderUpdate):
        try:
            provider = self.session.get(Provider, provider_id)
            if not provider:
                raise HTTPException(status_code=404, detail="Provider not found")
            for key, value in provider_update.model_dump(exclude_unset=True).items():
                setattr(provider, key, value)
            self.session.add(provider)
            self.session.commit()
            self.session.refresh(provider)
            return provider
        except Exception as e:
            raise e

    def delete_provider(self, provider_id: UUID):
        try:
            provider = self.session.get(Provider, provider_id)
            if not provider:
                raise HTTPException(status_code=404, detail="Provider not found")
            self.session.delete(provider)
            self.session.commit()
        except Exception as e:
            raise e
