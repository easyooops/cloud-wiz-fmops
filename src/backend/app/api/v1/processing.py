from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.interface.service import ServiceType
from app.core.factories import get_database
from app.service.processing.service import ProcessingService
from app.service.processing.model import Processing
from app.api.v1.schemas.processing import ProcessingCreate, ProcessingUpdate
from app.core.exception import internal_server_error

router = APIRouter()

# GET
@router.get("/", response_model=List[Processing])
def get_processings(
    user_id: Optional[UUID] = None,
    processing_type: Optional[str] = None,
    session: Session = Depends(get_database)
):
    try:
        service = ProcessingService(session)
        return service.get_all_processings(user_id, processing_type)
    except Exception as e:
        raise internal_server_error(e)

# CREATE    
@router.post("/", response_model=Processing)
def create_processing(
    processing: ProcessingCreate, 
    session: Session = Depends(get_database)
):
    try:
        service = ProcessingService(session)
        return service.create_processing(processing)
    except Exception as e:
        raise internal_server_error(e)
    
# UPDATE
@router.put("/{processing_id}", response_model=Processing)
def update_processing(
    processing_id: UUID,
    processing_update: ProcessingUpdate,
    session: Session = Depends(get_database)
):
    try:
        service = ProcessingService(session)
        return service.update_processing(processing_id, processing_update)
    except Exception as e:
        raise internal_server_error(e)

# DELETE
@router.delete("/{processing_id}")
def delete_processing(
    processing_id: UUID,
    session: Session = Depends(get_database)
):
    try:
        service = ProcessingService(session)
        service.delete_processing(processing_id)
        return {"message": "Processing deleted successfully"}
    except Exception as e:
        raise internal_server_error(e)
