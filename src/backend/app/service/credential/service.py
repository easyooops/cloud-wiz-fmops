from typing import List, Optional
from fastapi import HTTPException
from sqlmodel import Session, select
from uuid import UUID

from app.service.credential.model import Credential
from app.api.v1.schemas.credential import CredentialCreate, CredentialUpdate

class CredentialService:
    def __init__(self, session: Session):
        self.session = session

    def get_all_credentials(self, user_id: Optional[UUID] = None, provider_id: Optional[UUID] = None):
        statement = select(Credential)
        if user_id:
            statement = statement.where(Credential.user_id == user_id)
        if provider_id:
            statement = statement.where(Credential.provider_id == provider_id)
        return self.session.exec(statement).all()

    def create_credential(self, credential_data: CredentialCreate):
        try:
            new_credential = Credential(**credential_data.model_dump())
            self.session.add(new_credential)
            self.session.commit()
            self.session.refresh(new_credential)
            return new_credential
        except Exception as e:
            raise e

    def update_credential(self, credential_id: UUID, credential_update: CredentialUpdate):
        try:
            credential = self.session.get(Credential, credential_id)
            if not credential:
                raise HTTPException(status_code=404, detail="Credential not found")
            for key, value in credential_update.model_dump(exclude_unset=True).items():
                setattr(credential, key, value)
            self.session.add(credential)
            self.session.commit()
            self.session.refresh(credential)
            return credential
        except Exception as e:
            raise e

    def delete_credential(self, credential_id: UUID):
        try:
            credential = self.session.get(Credential, credential_id)
            if not credential:
                raise HTTPException(status_code=404, detail="Credential not found")
            self.session.delete(credential)
            self.session.commit()
        except Exception as e:
            raise e
