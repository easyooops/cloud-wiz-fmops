from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.interface.service import ServiceType
from app.core.factories import get_database
from app.core.util import internal_server_error
from app.service.provider.service import ProviderService
from app.service.provider.model import Provider
from app.api.v1.schemas.provider import ProviderCreate, ProviderUpdate

router = APIRouter()

# GET
@router.get("/", response_model=List[Provider])
def get_provider(
    type: Optional[str] = None,
    name: Optional[str] = None,
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = ProviderService(session)
        return service.get_all_providers(type, name)
    except Exception as e:
        raise internal_server_error(e)

# CREATE    
@router.post("/", response_model=Provider)
def create_provider(
    provider: ProviderCreate, 
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = ProviderService(session)
        return service.create_provider(provider)
    except Exception as e:
        raise internal_server_error(e)
    
# UPDATE
@router.put("/{provider_id}", response_model=Provider)
def update_provider(
    provider_id: int,
    provider_update: ProviderUpdate,
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = ProviderService(session)
        return service.update_provider(provider_id, provider_update)
    except Exception as e:
        raise internal_server_error(e)

# DELETE
@router.delete("/{provider_id}")
def delete_provider(
    provider_id: int,
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = ProviderService(session)
        service.delete_provider(provider_id)
        return {"message": "Provider deleted successfully"}
    except Exception as e:
        raise internal_server_error(e)    