import logging
from typing import Any, Dict, List, Optional
from uuid import UUID
from fastapi import HTTPException, UploadFile
from sqlmodel import Session, select, desc
from app.core.provider.google.google_drive import GoogleDriveService
from app.service.store.model import Store
from app.api.v1.schemas.store import StoreCreate, StoreUpdate


class StoreGoogleService(GoogleDriveService):
    def __init__(self, google_token: str, refresh_token: str, client_id: str, client_secret: str, token_uri: str, session: Session):
        super().__init__(google_token, refresh_token, client_id, client_secret, token_uri)
        self.session = session

    def get_all_stores(self, user_id: Optional[UUID] = None):
        try:
            statement = select(Store)
            if user_id:
                statement = statement.where(Store.user_id == user_id)

            statement = statement.order_by(Store.store_id.desc())
            return self.session.execute(statement).scalars().all()
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error retrieving stores")

    def get_store_directory_info_by_name(self, user_id: UUID, directory_name: str):
        try:
            folder_info = self.get_folder_info_by_name(directory_name)
            return folder_info
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error retrieving directory info")

    def create_store(self, store_data: StoreCreate, user_id: UUID):
        try:
            new_store = Store(**store_data.dict())
            self.session.add(new_store)
            self.session.commit()
            self.session.refresh(new_store)
            full_directory_name = f"{user_id}/{new_store.store_name}"
            self.create_folder(full_directory_name)
            return new_store
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error creating store: {str(e)}")

    def update_store(self, store_id: UUID, store_update: StoreUpdate, user_id: UUID):
        try:
            store = self.session.get(Store, store_id)
            if not store:
                raise HTTPException(status_code=404, detail="Store not found")
            for key, value in store_update.dict(exclude_unset=True).items():
                setattr(store, key, value)
            self.session.add(store)
            self.session.commit()
            self.session.refresh(store)
            return store
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error updating store: {str(e)}")

    def delete_store(self, store_id: UUID, user_id: UUID):
        try:
            store = self.session.get(Store, store_id)
            if not store:
                raise HTTPException(status_code=404, detail="Store not found")
            self.session.delete(store)
            self.session.commit()
            full_directory_name = f"{user_id}/{store.store_name}"
            self.delete_file(full_directory_name)
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error deleting store: {str(e)}")

    def list_files(self, user_id: UUID, store_name: str) -> List[Dict[str, Any]]:
        try:
            full_directory_name = f"{user_id}/{store_name}"
            objects = self.list_files(full_directory_name)
            logging.info(f"Objects listed from Google Drive: {objects}")
            files = []
            for obj in objects:
                file_info = {
                    "Key": obj["id"],
                    "Name": obj["name"],
                }
                files.append(file_info)
            logging.info(f"Files: {files}")
            return files
        except Exception as e:
            logging.error(f"Error listing files: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error listing files: {str(e)}")

    def upload_file_to_store(self, user_id: UUID, store_name: str, file: UploadFile):
        try:
            file_location = f"{user_id}/{store_name}"
            self.upload_file(file.file, file_location)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")

    def delete_directory(self, store_name: str):
        try:
            objects_to_delete = self.list_files(store_name)
            for obj in objects_to_delete:
                self.delete_file(obj['id'])
        except Exception as e:
            logging.error(f"Error deleting directory: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error deleting directory: {str(e)}")

    def delete_file_from_store(self, file_location: str):
        try:
            self.delete_file(file_location)
        except Exception as e:
            logging.error(f"Error deleting file from store: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error deleting file from store: {str(e)}")