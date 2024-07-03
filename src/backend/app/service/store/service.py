import logging
import boto3
import os
from typing import Any, Dict, List, Optional
from uuid import UUID
from fastapi import HTTPException, UploadFile
from sqlmodel import Session, select
from app.service.store.model import Store
from app.api.v1.schemas.store import StoreCreate, StoreUpdate
from app.core.provider.aws.s3 import S3Service
import pandas as pd
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader, Docx2txtLoader
from langchain_core.documents import Document

class StoreService(S3Service):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session
        self.store_bucket = os.getenv("AWS_S3_BUCKET_STORE_NAME")

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
            logging.info(f"Objects listed from S3: {objects}")
            files = []
            for obj in objects:
                file_info = {
                    "Key": obj["Key"],
                    "LastModified": obj["LastModified"],
                    "Size": obj["Size"],
                }
                files.append(file_info)
            logging.info(f"Files: {files}")
            return files
        except Exception as e:
            logging.error(f"Error listing files: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error listing files: {str(e)}")

    def upload_file(self, file, file_location: str):
        try:
            self.s3_client.upload_fileobj(file, self.bucket_name, file_location)
        except Exception as e:
            logging.error(f"Error uploading file: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")

    def upload_file_to_store(self, store_name: str, file: UploadFile):
        try:
            file_location = f"{store_name}/{file.filename}"
            self.upload_file(file.file, file_location)
        except Exception as e:
            logging.error(f"Error uploading file to store: {str(e)}")
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
            logging.error(f"Error deleting directory: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error deleting directory: {str(e)}")

    def delete_file_from_store(self, file_location: str):
        try:
            self.delete_file(file_location)
        except Exception as e:
            logging.error(f"Error deleting file from store: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error deleting file from store: {str(e)}")

    def load_documents(self, files: List[str]) -> List[Document]:
        try:
            if not files:
                logging.error("No files provided to load_documents.")
                raise HTTPException(status_code=400, detail="No files provided")

            documents = []
            s3_client = boto3.client('s3')
            bucket_name = os.getenv("AWS_S3_BUCKET_STORE_NAME")
            logging.info(f"Bucket name: {bucket_name}")

            for s3_file_key in files:
                local_file_path = f"/tmp/{s3_file_key.split('/')[-1]}"
                logging.info(f"Downloading file: {s3_file_key} to {local_file_path}")
                s3_client.download_file(bucket_name, s3_file_key, local_file_path)

                if local_file_path.endswith('.txt'):
                    loader = TextLoader(local_file_path)
                    documents.extend(loader.load())
                elif local_file_path.endswith('.pdf'):
                    loader = PyPDFLoader(local_file_path)
                    documents.extend(loader.load())
                elif local_file_path.endswith('.csv'):
                    loader = CSVLoader(local_file_path)
                    documents.extend(loader.load())
                elif local_file_path.endswith('.docx'):
                    loader = Docx2txtLoader(local_file_path)
                    documents.extend(loader.load())
                elif local_file_path.endswith('.xlsx'):
                    xlsx = pd.ExcelFile(local_file_path)
                    for sheet_name in xlsx.sheet_names:
                        df = pd.read_excel(xlsx, sheet_name=sheet_name)
                        full_text = df.to_string(index=False)
                        documents.append(Document(page_content=full_text, metadata={"source": f"{local_file_path} - {sheet_name}"}))
                else:
                    logging.error(f"Unsupported file format: {local_file_path}")
                    raise ValueError(f"Unsupported file format: {local_file_path}")
            logging.info(f"Loaded documents: {documents}")
            return documents
        except Exception as e:
            logging.error(f"Error in load_documents: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))

