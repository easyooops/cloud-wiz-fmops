from typing import List, Optional
from sqlmodel import Session, desc, select
from uuid import UUID

from app.service.credential.model import Credential
from app.api.v1.schemas.credential import CredentialCreate, CredentialProviderJoin, CredentialUpdate
from app.service.provider.model import Provider

class CredentialService:
    def __init__(self, session: Session):
        self.session = session

    def get_all_credentials(self, user_id: Optional[UUID] = None, credential_id: Optional[UUID] = None, provider_id: Optional[UUID] = None) -> List[CredentialProviderJoin]:
        statement = select(Credential, Provider).join(Provider, Credential.provider_id == Provider.provider_id)
        if user_id:
            statement = statement.where(Credential.user_id == user_id)
        if credential_id:
            statement = statement.where(Credential.credential_id == credential_id)
        if provider_id:
            statement = statement.where(Credential.provider_id == provider_id)
                    
        statement = statement.order_by(desc(Credential.credential_id))
                            
        results = self.session.execute(statement).all()
        return [self._map_to_credential_out(credential, provider) for credential, provider in results]

    def _map_to_credential_out(self, credential: Credential, provider: Provider) -> CredentialProviderJoin:
        return CredentialProviderJoin(
            credential_id=credential.credential_id,
            user_id=credential.user_id,
            provider_id=credential.provider_id,
            credential_name=credential.credential_name,
            access_key=credential.access_key,
            secret_key=credential.secret_key,
            session_key=credential.session_key,
            access_token=credential.access_token,
            api_key=credential.api_key,
            api_endpoint=credential.api_endpoint,
            provider_name=provider.name,
            provider_company=provider.company,
            provider_desc=provider.description,
            provider_logo=provider.logo,
            provider_type=provider.type,
            provider_ord=provider.sort_order
        )
    
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
            self.session.delete(credential)
            self.session.commit()
        except Exception as e:
            raise e
