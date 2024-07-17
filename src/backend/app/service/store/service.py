import logging
from aiohttp import ClientError
import boto3
import os
from typing import Any, Dict, List, Optional
from uuid import UUID
from fastapi import HTTPException, UploadFile
from sqlmodel import Session, desc, select
from app.service.store.model import Store
from app.api.v1.schemas.store import StoreCreate, StoreUpdate
from app.core.provider.aws.s3 import S3Service
import pandas as pd
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader, Docx2txtLoader
from langchain_core.documents import Document

from app.service.credential.model import Credential
from app.service.credential.service import CredentialService

class StoreService():
    def __init__(self, session: Session, user_id: Optional[UUID] = None):
        super().__init__()
        self.session = session
        self.credential_service = CredentialService(session)
        self.store_bucket = os.getenv("AWS_S3_BUCKET_STORE_NAME")
    
    def get_all_stores(self, user_id: Optional[UUID] = None, store_id: Optional[UUID] = None):
        try:
            statement = select(Store)
            if user_id:
                statement = statement.where(Store.user_id == user_id)
            if store_id:
                statement = statement.where(Store.store_id == store_id)

            statement = statement.order_by(desc(Store.store_id))

            return self.session.execute(statement).scalars().all()
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error retrieving stores")

    def get_store_directory_info(self, user_id: UUID, directory_name: str, credential_id: UUID):
        try:
            full_directory_name = f"{user_id}/{directory_name}"

            storage_service = self.credential_service._set_storage_credential(credential_id=credential_id)
            if storage_service:
                return storage_service.get_directory_info(full_directory_name)
            else:
                print("Failed to initialize storage service")
                return {'total_size': 0, 'file_count': 0}
        except Exception as e:
            print(f"Error while retrieving directory info: {e}")
            return {'total_size': 0, 'file_count': 0}

    def create_store(self, store_data: StoreCreate, user_id: UUID):
        try:
            new_store = Store(**store_data.model_dump())
            self.session.add(new_store)
            self.session.commit()
            self.session.refresh(new_store)
            full_directory_name = f"{user_id}/{new_store.store_name}"

            storage_service = self.credential_service._set_storage_credential(credential_id=new_store.credential_id)
            if storage_service:
                storage_service.retry(lambda: storage_service.create_directory(full_directory_name))
            else:
                print("Failed to initialize storage service")                    
            return new_store
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error creating store: {str(e)}")

    def update_store(self, store_id: UUID, store_update: StoreUpdate, user_id: UUID):
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

    def delete_store(self, store_id: UUID, user_id: UUID):
        try:
            store = self.session.get(Store, store_id)
            if not store:
                raise HTTPException(status_code=404, detail="Store not found")
            self.session.delete(store)
            self.session.commit()
            full_directory_name = f"{user_id}/{store.store_name}"

            storage_service = self.credential_service._set_storage_credential(credential_id=store.credential_id)
            storage_service.delete_directory(full_directory_name)
        
        except HTTPException as e:
            raise e  # Re-raise the HTTPException if it was already raised
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error deleting store: {str(e)}")

    def list_files(self, user_id: UUID, store_id: UUID) -> List[Dict[str, Any]]:
        try:
            store = self.session.get(Store, store_id)
            if not store:
                raise HTTPException(status_code=404, detail="Store not found")            
            full_directory_name = f"{user_id}/{store.store_name}"

            storage_service = self.credential_service._set_storage_credential(credential_id=store.credential_id)
            if not storage_service:
                logging.error("Failed to initialize storage service")
                return []

            objects = storage_service.list_all_objects(full_directory_name)

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
            return []

    def upload_file_to_store(self, user_id: UUID, store_id: UUID, file: UploadFile):
        try:
            store = self.session.get(Store, store_id)
            if not store:
                raise HTTPException(status_code=404, detail="Store not found")            
            file_location = f"{user_id}/{store.store_name}/{file.filename}"

            storage_service = self.credential_service._set_storage_credential(credential_id=store.credential_id)
            if not storage_service:
                logging.error("Failed to initialize storage service")
                raise HTTPException(status_code=500, detail="Failed to initialize storage service")
            
            storage_service.upload_file(file.file, file_location)

        except Exception as e:
            logging.error(f"Error uploading file: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")


    def delete_file_from_store(self, user_id: UUID, store_id: UUID, file_name: str):
        try:
            store = self.session.get(Store, store_id)
            if not store:
                raise HTTPException(status_code=404, detail="Store not found")              
            file_location = f"{user_id}/{store.store_name}/{file_name}"

            storage_service = self.credential_service._set_storage_credential(credential_id=store.credential_id)
            storage_service.delete_file(file_location)

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

    def load_documents_v2(self, credential_id: UUID, files: List[str]) -> List[Document]:
        try:
            if not files:
                logging.error("No files provided to load_documents.")
                raise HTTPException(status_code=400, detail="No files provided")

            storage_service = self.credential_service._set_storage_credential(credential_id=credential_id)
            
            if not storage_service:
                logging.error("Failed to initialize storage service")
                raise HTTPException(status_code=500, detail="Failed to initialize storage service")

            documents = []
            for s3_file_key in files:
                local_file_path = f"/tmp/{s3_file_key.split('/')[-1]}"
                logging.info(f"Downloading file: {s3_file_key} to {local_file_path}")
                
                try:
                    storage_service.download_file(s3_file_key, local_file_path)
                except ClientError as e:
                    logging.error(f"Error downloading file from S3: {str(e)}")
                    raise HTTPException(status_code=500, detail=f"Error downloading file from S3: {str(e)}")

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

