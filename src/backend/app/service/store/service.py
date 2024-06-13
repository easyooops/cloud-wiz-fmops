from typing import Any, Dict, List, Optional
from uuid import UUID
from fastapi import HTTPException, UploadFile
from sqlmodel import Session, select
from app.service.store.model import Store
from app.api.v1.schemas.store import StoreCreate, StoreUpdate
from app.core.provider.aws.s3 import S3Service

class StoreService(S3Service):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def get_all_stores(self, user_id: Optional[UUID] = None):
        try:
            statement = select(Store)
            if user_id:
                statement = statement.where(Store.user_id == user_id)
            return self.session.exec(statement).all()
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error retrieving stores")

    def get_store_directory_info(self, directory_name: str):
        try:
            return self.get_directory_info(directory_name)
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error retrieving directory info")
        
    def create_store(self, store_data: StoreCreate):
        try:
            new_store = Store(**store_data.model_dump())
            self.session.add(new_store)
            self.session.commit()
            self.session.refresh(new_store)
            print(f"store creating directory: {new_store.store_name}")
            self.retry(lambda: self.create_directory(new_store.store_name))
            return new_store
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error creating store: {str(e)}")

    def update_store(self, store_id: UUID, store_update: StoreUpdate):
        try:
            store = self.session.get(Store, store_id)
            if not store:
                raise HTTPException(status_code=404, detail="Store not found")
            for key, value in store_update.model_dump(exclude_unset=True).items():
                setattr(store, key, value)
            self.session.add(store)
            self.session.commit()
            self.session.refresh(store)
            return store
        except HTTPException as e:
            raise e  # Re-raise the HTTPException if it was already raised
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error updating store: {str(e)}")

    def delete_store(self, store_id: UUID):
        try:
            store = self.session.get(Store, store_id)
            if not store:
                raise HTTPException(status_code=404, detail="Store not found")
            self.session.delete(store)
            self.session.commit()
            self.delete_directory(store.store_name)
        except HTTPException as e:
            raise e  # Re-raise the HTTPException if it was already raised
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error deleting store: {str(e)}")

    def list_files(self, store_name: str) -> List[Dict[str, Any]]:
        try:
            objects = self.list_all_objects(store_name)
            files = []
            for obj in objects:
                file_info = {
                    "Key": obj["Key"],
                    "LastModified": obj["LastModified"],
                    "Size": obj["Size"],
                }
                files.append(file_info)
            return files
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error listing files: {str(e)}")

    def upload_file(self, file, file_location: str):
        try:
            self.s3_client.upload_fileobj(file, self.bucket_name, file_location)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")

    def upload_file_to_store(self, store_name: str, file: UploadFile):
        try:
            file_location = f"{store_name}/{file.filename}"
            self.upload_file(file.file, file_location)
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error uploading file to store")

    def delete_directory(self, store_name: str):
        try:
            objects_to_delete = self.list_objects(store_name)
            delete_keys = [{'Key': obj['Key']} for obj in objects_to_delete]

            if delete_keys:
                self.s3_client.delete_objects(
                    Bucket=self.bucket_name,
                    Delete={'Objects': delete_keys}
                )
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=f"{store_name}/")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error deleting directory: {str(e)}")
        
    def delete_file_from_store(self, file_location: str):
        try:
            self.delete_file(file_location)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error deleting file from store: {str(e)}")
