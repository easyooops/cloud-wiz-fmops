from typing import List, Optional
from uuid import UUID
from fastapi import HTTPException
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

    def create_store(self, store_data: StoreCreate):
        try:
            new_store = Store(**store_data.model_dump())
            self.session.add(new_store)
            self.session.commit()
            self.session.refresh(new_store)
            self.create_directory(new_store.store_name)
            return new_store
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error creating store")

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
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error deleting store")

    def delete_store(self, store_id: UUID):
        try:
            store = self.session.get(Store, store_id)
            if not store:
                raise HTTPException(status_code=404, detail="Store not found")
            self.session.delete(store)
            self.session.commit()
            self.delete_directory(store.store_name)
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error deleting store")

    def list_files(self, store_name: str) -> List[str]:
        try:
            objects = self.list_objects(store_name)
            return [obj['Key'] for obj in objects]
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error listing files")

    def upload_file(self, file, file_location: str):
        try:
            self.s3_client.upload_fileobj(file, self.bucket_name, file_location)
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error uploading file")

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
            raise HTTPException(status_code=500, detail="Error deleting directory")