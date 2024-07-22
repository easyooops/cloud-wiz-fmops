from typing import Any, Dict, List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, Header, Query
from sqlmodel import Session
from app.core.exception import internal_server_error
from app.core.factories import get_database
from app.service.store.model import Store
from app.api.v1.schemas.store import StoreCreate, StoreUpdate, StoreWithDirectoryGoogle
from app.service.store_google.StoreGoogleService import StoreGoogleService

router = APIRouter()


@router.get("/{user_id}", response_model=StoreWithDirectoryGoogle)
def get_files_by_name(
        user_id: UUID,
        folder_name: str = Query(...),
        session: Session = Depends(get_database),
        access_token: str = Header(...),
        refresh_token: str = Header(None)
):
    try:
        service = StoreGoogleService(access_token=access_token, refresh_token=refresh_token, session=session)
        directory_info = service.get_store_directory_info_by_name(user_id, folder_name)
        return directory_info
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise internal_server_error(e)


@router.get("/drive/files", response_model=List[Dict[str, Any]])
async def list_drive_files(
        access_token: str = Header(...),
        refresh_token: str = Header(None),
        folder_id: str = None
):
    try:
        service = StoreGoogleService(access_token=access_token, refresh_token=refresh_token)
        files = service.google_drive_service.list_files(folder_id)
        return files
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/{user_id}/{store_name}/upload")
def upload_file_to_folder(
        store_name: str,
        user_id: UUID,
        file: UploadFile = File(...),
        session: Session = Depends(get_database),
        access_token: str = Header(...),
        refresh_token: str = Header(None)
):
    try:
        service = StoreGoogleService(access_token=access_token, refresh_token=refresh_token, session=session)
        service.upload_file_to_store(user_id, store_name, file)
        return {"message": "File uploaded successfully"}
    except Exception as e:
        raise internal_server_error(e)


@router.delete("/{user_id}/{store_name}/files/{file_name}")
def delete_file_from_folder(
        store_name: str,
        file_name: str,
        user_id: UUID,
        session: Session = Depends(get_database),
        access_token: str = Header(...),
        refresh_token: str = Header(None)
):
    try:
        service = StoreGoogleService(access_token=access_token, refresh_token=refresh_token, session=session)
        service.delete_file_from_store(user_id, store_name, file_name)
        return {"message": "File deleted successfully"}
    except Exception as e:
        raise internal_server_error(e)