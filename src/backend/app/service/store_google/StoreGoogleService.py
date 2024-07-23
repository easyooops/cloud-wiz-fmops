import os
from sqlmodel import Session
from typing import List, Dict, Any
from app.core.provider.storage.GoogleDrive import GoogleDriveStorageService
from app.service.store.model import Store
from app.api.v1.schemas.store import StoreCreate, StoreUpdate, FileInfo, StoreWithDirectoryGoogle
from fastapi import HTTPException, UploadFile
from uuid import UUID

class StoreGoogleService:
    def __init__(self, access_token: str = None, refresh_token: str = None, session: Session = None):
        self.google_drive_service = GoogleDriveStorageService(access_token=access_token, refresh_token=refresh_token)
        self.session = session

    def get_store_directory_info_by_name(self, user_id: UUID, folder_name: str) -> StoreWithDirectoryGoogle:
        folder_id = self.google_drive_service.get_folder_id_by_name(folder_name)
        files_info = self.google_drive_service.list_files_in_folder(folder_id)
        total_size = sum(int(file.get('size', 0)) for file in files_info)
        file_count = len(files_info)

        return StoreWithDirectoryGoogle(
            total_size=total_size,
            file_count=file_count,
            files=[FileInfo(id=file['id'], name=file['name'], size=int(file.get('size', 0))) for file in files_info]
        )

    def list_files(self, user_id: UUID, store_name: str) -> List[Dict[str, Any]]:
        files = self.google_drive_service.list_files(store_name)
        return files

    def upload_file_to_store(self, user_id: UUID, store_name: str, file: UploadFile):
        folder_id = self.google_drive_service.get_folder_id_by_name(store_name)
        return self.google_drive_service.upload_file_to_folder(folder_id, file)

    def delete_file_from_store(self, user_id: UUID, store_name: str, file_name: str):
        folder_id = self.google_drive_service.get_folder_id_by_name(store_name)
        files = self.google_drive_service.list_files_in_folder(folder_id)
        file_id = next((f['id'] for f in files if f['name'] == file_name), None)
        if not file_id:
            raise HTTPException(status_code=404, detail="File not found")
        self.google_drive_service.delete_file(file_id)
