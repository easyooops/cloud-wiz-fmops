from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlmodel import Session
from app.core.interface.service import ServiceType
from app.core.factories import get_database
from app.service.store.service import StoreService
from app.api.v1.schemas.store import StoreCreate, StoreUpdate
from app.core.exception import internal_server_error
from app.service.store.model import Store

router = APIRouter()

@router.get("/", response_model=List[Store])
def get_stores(
    user_id: Optional[UUID] = None,
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = StoreService(session)
        return service.get_all_stores(user_id)
    except Exception as e:
        raise internal_server_error(e)

@router.post("/", response_model=Store)
def create_store(
    store: StoreCreate,
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = StoreService(session)
        return service.create_store(store)
    except Exception as e:
        raise internal_server_error(e)

@router.put("/{store_id}", response_model=Store)
def update_store(
    store_id: UUID,
    store_update: StoreUpdate,
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = StoreService(session)
        return service.update_store(store_id, store_update)
    except Exception as e:
        raise internal_server_error(e)

@router.delete("/{store_id}")
def delete_store(
    store_id: UUID,
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = StoreService(session)
        service.delete_store(store_id)
        return {"message": "Store deleted successfully"}
    except Exception as e:
        raise internal_server_error(e)

@router.get("/{store_name}/files", response_model=List[str])
def get_store_files(
    store_name: str,
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = StoreService(session)
        return service.list_files(store_name)
    except Exception as e:
        raise internal_server_error(e)

@router.post("/{store_name}/upload")
def upload_file_to_store(
    store_name: str,
    file: UploadFile = File(...),
    session: Session = Depends(lambda: next(get_database(ServiceType.SQLALCHEMY)))
):
    try:
        service = StoreService(session)
        file_location = f"{store_name}/{file.filename}"
        service.upload_file(file.file, file_location)
        return {"message": "File uploaded successfully"}
    except Exception as e:
        raise internal_server_error(e)