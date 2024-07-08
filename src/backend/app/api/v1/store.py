from typing import Any, Dict, List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlmodel import Session
from app.core.interface.service import ServiceType
from app.core.factories import get_database
from app.service.store.service import StoreService
from app.api.v1.schemas.store import StoreCreate, StoreUpdate, StoreWithDirectory
from app.core.exception import internal_server_error
from app.service.store.model import Store

router = APIRouter()

@router.get("/", response_model=List[StoreWithDirectory])
def get_stores(
    user_id: Optional[UUID] = None,
    session: Session = Depends(lambda: next(get_database()))
):
    try:
        service = StoreService(session)
        stores = service.get_all_stores(user_id)
    
        store_responses = []
        for store in stores:
            directory_info = service.get_directory_info(store.store_name)
            store_with_directory = StoreWithDirectory(
                store_id=store.store_id,
                store_name=store.store_name,
                description=store.description,
                created_at=store.created_at,
                updated_at=store.updated_at,
                user_id=store.user_id,
                total_size=directory_info['total_size'],
                file_count=directory_info['file_count']
            )
            store_responses.append(store_with_directory)
        return store_responses
        
    except Exception as e:
        raise internal_server_error(e)

@router.post("/", response_model=Store)
def create_store(
    store: StoreCreate,
    session: Session = Depends(lambda: next(get_database()))
):
    try:
        service = StoreService(session)
        return service.create_store(store)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating store: {str(e)}")

@router.put("/{store_id}", response_model=Store)
def update_store(
    store_id: UUID,
    store_update: StoreUpdate,
    session: Session = Depends(lambda: next(get_database()))
):
    try:
        service = StoreService(session)
        return service.update_store(store_id, store_update)
    except Exception as e:
        raise internal_server_error(e)

@router.delete("/{store_id}")
def delete_store(
    store_id: UUID,
    session: Session = Depends(lambda: next(get_database()))
):
    try:
        service = StoreService(session)
        service.delete_store(store_id)
        return {"message": "Store deleted successfully"}
    except Exception as e:
        raise internal_server_error(e)

@router.get("/{store_name}/files", response_model=List[Dict[str, Any]])
def get_store_files(
    store_name: str,
    session: Session = Depends(lambda: next(get_database()))
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
    session: Session = Depends(lambda: next(get_database()))
):
    try:
        service = StoreService(session)
        file_location = f"{store_name}/{file.filename}"
        service.upload_file(file.file, file_location)
        return {"message": "File uploaded successfully"}
    except Exception as e:
        raise internal_server_error(e)
    
@router.delete("/{store_name}/files/{file_name}")
def delete_file_from_store(
    store_name: str,
    file_name: str,
    session: Session = Depends(lambda: next(get_database()))
):
    try:
        service = StoreService(session)
        file_location = f"{store_name}/{file_name}"
        service.delete_file_from_store(file_location)
        return {"message": "File deleted successfully"}
    except Exception as e:
        raise internal_server_error(e)
