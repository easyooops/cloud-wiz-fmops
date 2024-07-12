from typing import Any, Dict, List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, Header, Query
from sqlmodel import Session
from app.core.factories import get_database
from app.service.store_google.service import StoreGoogleService
from app.api.v1.schemas.store import StoreCreate, StoreUpdate, StoreWithDirectory
from app.core.exception import internal_server_error
from app.service.store.model import Store

router = APIRouter()


@router.get("/{user_id}", response_model=StoreWithDirectory)
def get_store_by_name(
        user_id: UUID,
        folder_name: str = Query(...),
        session: Session = Depends(get_database),
        google_token: str = Header(...),
        refresh_token: str = Header(...),
        client_id: str = Header(...),
        client_secret: str = Header(...),
        token_uri: str = Header(...)
):
    try:
        service = StoreGoogleService(google_token, refresh_token, client_id, client_secret, token_uri, session)
        directory_info = service.get_store_directory_info_by_name(user_id, folder_name)
        return directory_info
    except Exception as e:
        raise internal_server_error(e)


@router.post("/{user_id}", response_model=Store)
def create_store(
        store: StoreCreate,
        user_id: UUID,
        session: Session = Depends(get_database),
        google_token: str = Header(...),
        refresh_token: str = Header(...),
        client_id: str = Header(...),
        client_secret: str = Header(...),
        token_uri: str = Header(...)
):
    try:
        service = StoreGoogleService(google_token, refresh_token, client_id, client_secret, token_uri, session)
        return service.create_store(store, user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating store: {str(e)}")


@router.put("/{user_id}/{store_id}", response_model=Store)
def update_store(
        store_id: UUID,
        store_update: StoreUpdate,
        user_id: UUID,
        session: Session = Depends(get_database),
        google_token: str = Header(...),
        refresh_token: str = Header(...),
        client_id: str = Header(...),
        client_secret: str = Header(...),
        token_uri: str = Header(...)
):
    try:
        service = StoreGoogleService(google_token, refresh_token, client_id, client_secret, token_uri, session)
        return service.update_store(store_id, store_update, user_id)
    except Exception as e:
        raise internal_server_error(e)


@router.delete("/{user_id}/{store_id}")
def delete_store(
        store_id: UUID,
        user_id: UUID,
        session: Session = Depends(get_database),
        google_token: str = Header(...),
        refresh_token: str = Header(...),
        client_id: str = Header(...),
        client_secret: str = Header(...),
        token_uri: str = Header(...)
):
    try:
        service = StoreGoogleService(google_token, refresh_token, client_id, client_secret, token_uri, session)
        service.delete_store(store_id, user_id)
        return {"message": "Store deleted successfully"}
    except Exception as e:
        raise internal_server_error(e)


@router.get("/{user_id}/{store_name}/files", response_model=List[Dict[str, Any]])
def get_store_files(
        store_name: str,
        user_id: UUID,
        session: Session = Depends(get_database),
        google_token: str = Header(...),
        refresh_token: str = Header(...),
        client_id: str = Header(...),
        client_secret: str = Header(...),
        token_uri: str = Header(...)
):
    try:
        service = StoreGoogleService(google_token, refresh_token, client_id, client_secret, token_uri, session)
        return service.list_files(user_id, store_name)
    except Exception as e:
        raise internal_server_error(e)


@router.post("/{user_id}/{store_name}/upload")
def upload_file_to_store(
        store_name: str,
        user_id: UUID,
        file: UploadFile = File(...),
        session: Session = Depends(get_database),
        google_token: str = Header(...),
        refresh_token: str = Header(...),
        client_id: str = Header(...),
        client_secret: str = Header(...),
        token_uri: str = Header(...)
):
    try:
        service = StoreGoogleService(google_token, refresh_token, client_id, client_secret, token_uri, session)
        service.upload_file_to_store(user_id, store_name, file)
        return {"message": "File uploaded successfully"}
    except Exception as e:
        raise internal_server_error(e)


@router.delete("/{user_id}/{store_name}/files/{file_name}")
def delete_file_from_store(
        store_name: str,
        file_name: str,
        user_id: UUID,
        session: Session = Depends(get_database),
        google_token: str = Header(...),
        refresh_token: str = Header(...),
        client_id: str = Header(...),
        client_secret: str = Header(...),
        token_uri: str = Header(...)
):
    try:
        service = StoreGoogleService(google_token, refresh_token, client_id, client_secret, token_uri, session)
        file_location = f"{user_id}/{store_name}/{file_name}"
        service.delete_file_from_store(file_location)
        return {"message": "File deleted successfully"}
    except Exception as e:
        raise internal_server_error(e)