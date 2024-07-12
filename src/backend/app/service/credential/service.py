import os
from typing import List, Optional
from sqlalchemy import func
from sqlmodel import Session, desc, select
from uuid import UUID

from app.service.credential.model import Credential
from app.api.v1.schemas.credential import CredentialCreate, CredentialProviderJoin, CredentialUpdate
from app.service.provider.model import Provider
from app.service.agent.model import Agent
from app.core.provider.aws.s3 import S3Service

class CredentialService(S3Service):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session
        self.store_bucket = os.getenv("AWS_S3_BUCKET_STORE_NAME")

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

        credentials = []
        for credential, provider in results:
            expected_count = self._calculate_expected_count(user_id, provider)
            credentials.append(self._map_to_credential_out(credential, provider, expected_count))
        
        return credentials

    def _calculate_expected_count(self, user_id: UUID, provider: Provider) -> int:

        result = 0

        if provider.type == 'M':
            agent_statement = select(func.sum(Agent.expected_token_count)).where(
                Agent.user_id == user_id
            )            
            agent_statement = agent_statement.where(Agent.fm_provider_id == provider.provider_id)
            result = self.session.execute(agent_statement).scalar() or 0
        elif provider.type == 'S':
            full_directory_name = f"{user_id}"
            result = self.get_directory_info(full_directory_name)['total_size']
        elif provider.type == 'V':
            result = 0

        return result
    
    def _map_to_credential_out(self, credential: Credential, provider: Provider, expected_count: int) -> CredentialProviderJoin:
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
            client_id=credential.client_id,
            auth_secret_key=credential.auth_secret_key,
            inner_used=credential.inner_used,
            limit_cnt=credential.limit_cnt,
            provider_name=provider.name,
            provider_company=provider.company,
            provider_desc=provider.description,
            provider_logo=provider.logo,
            provider_type=provider.type,
            provider_ord=provider.sort_order,
            expected_count=expected_count  
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
