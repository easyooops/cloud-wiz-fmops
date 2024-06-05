from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.interface.service import ServiceType
from app.core.factories import get_database
from app.service.credential.service import CredentialService
from app.service.credential.model import Credential
from app.api.v1.schemas.credential import CredentialCreate, CredentialUpdate
from app.core.exception import internal_server_error

router = APIRouter()

@router.get("/", response_model=List[Credential])
def get_credentials(
    user_id: Optional[UUID] = None,
    provider_id: Optional[UUID] = None,
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = CredentialService(session)
        return service.get_all_credentials(user_id, provider_id)
    except Exception as e:
        raise internal_server_error(e)

@router.post("/", response_model=Credential)
def create_credential(
    credential: CredentialCreate, 
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = CredentialService(session)
        return service.create_credential(credential)
    except Exception as e:
        raise internal_server_error(e)

@router.put("/{credential_id}", response_model=Credential)
def update_credential(
    credential_id: UUID,
    credential_update: CredentialUpdate,
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = CredentialService(session)
        return service.update_credential(credential_id, credential_update)
    except Exception as e:
        raise internal_server_error(e)

@router.delete("/{credential_id}")
def delete_credential(
    credential_id: UUID,
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = CredentialService(session)
        service.delete_credential(credential_id)
        return {"message": "Credential deleted successfully"}
    except Exception as e:
        raise internal_server_error(e)
