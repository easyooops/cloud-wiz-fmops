import json
import os

from fastapi import UploadFile
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from app.core.interface.service import ServiceFactory, StorageService
from typing import List, Dict, Any

from app.core.provider.aws.SecretManager import SecretManagerService


class GoogleDriveStorageService(StorageService):
    def __init__(self, access_token: str = None, refresh_token: str = None):
        client_id = os.getenv("GOOGLE_CLIENT_ID")
        client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
        token_uri = os.getenv("GOOGLE_TOKEN_URI")

        if refresh_token:
            self.credentials = Credentials(
                token=None,
                refresh_token=refresh_token,
                token_uri=token_uri,
                client_id=client_id,
                client_secret=client_secret
            )
        elif access_token:
            self.credentials = Credentials(token=access_token)
        else:
            raise ValueError("Either access_token or refresh_token must be provided")

        self.drive_service = build('drive', 'v3', credentials=self.credentials)

    def create_directory(self, directory_name: str):
        file_metadata = {
            'name': directory_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = self.drive_service.files().create(body=file_metadata, fields='id, name').execute()
        print(f"Directory creation response: {file}")
        return file

    def delete_directory(self, directory_name: str):
        folder_id = self.get_folder_id_by_name(directory_name)
        self.drive_service.files().delete(fileId=folder_id).execute()

    def list_files(self, directory_name: str = ''):
        if directory_name:
            folder_id = self.get_folder_id_by_name(directory_name)
            return self.list_files_in_folder(folder_id)
        else:
            return self.list_all_objects()

    def upload_file(self, file_path: str, file_location: str):
        file_metadata = {'name': file_location}
        media = MediaFileUpload(file_path, resumable=True)
        file = self.drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f'File ID: {file.get("id")}')
        return file

    def list_all_objects(self) -> List[Dict]:
        results = self.drive_service.files().list(pageSize=1000, fields="files(id, name)").execute()
        items = results.get('files', [])
        return items

    def get_directory_info(self, directory_name: str = ''):
        response = self.drive_service.files().list(q=f"'{directory_name}' in parents", fields="files(id, name, size)").execute()
        contents = response.get('files', [])
        total_size = sum(int(obj.get('size', 0)) for obj in contents)
        file_count = len(contents)
        return {
            'total_size': total_size,
            'file_count': file_count
        }

    def get_folder_id_by_name(self, folder_name: str) -> str:
        response = self.drive_service.files().list(
            q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false",
            fields="files(id, name)"
        ).execute()
        folders = response.get('files', [])
        if not folders:
            raise FileNotFoundError(f"No folder found with the name: {folder_name}")
        return folders[0]['id']

    def list_files_in_folder(self, folder_id: str) -> List[Dict[str, Any]]:
        response = self.drive_service.files().list(
            q=f"'{folder_id}' in parents and trashed=false",
            fields="files(id, name, size)"
        ).execute()
        return response.get('files', [])

    def upload_file_to_folder(self, folder_id: str, file: UploadFile):
        file_metadata = {'name': file.filename, 'parents': [folder_id]}
        media = MediaFileUpload(file.file, resumable=True)
        uploaded_file = self.drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f'File ID: {uploaded_file.get("id")}')
        return uploaded_file

    def delete_file(self, key: str):
        try:
            self.drive_service.files().delete(fileId=key).execute()
        except Exception as e:
            print(e)

    def retry(self, func, retries=5, delay=5, backoff=2):
        for attempt in range(retries):
            try:
                return func()
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt < retries - 1:
                    import time
                    time.sleep(delay)
                    delay *= backoff
                else:
                    raise e

    def download_file(self, s3_file_key: str, local_file_path: str):
        try:
            request = self.drive_service.files().get_media(fileId=s3_file_key)
            with open(local_file_path, 'wb') as file:
                downloader = MediaIoBaseDownload(file, request)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                    print(f"Download {int(status.progress() * 100)}%.")
        except Exception as e:
            print(f"Error downloading file from Google Drive: {str(e)}")
            raise

    def set_ready(self):
        print("GoogleDriveStorageService is ready")

    def teardown(self):
        print("GoogleDriveStorageService is being torn down")

    def get_folder_id_by_name(self, folder_name: str) -> str:
        response = self.drive_service.files().list(
            q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false",
            fields="files(id, name)"
        ).execute()
        folders = response.get('files', [])
        if not folders:
            raise FileNotFoundError(f"No folder found with the name: {folder_name}")
        return folders[0]['id']

    def list_all_objects(self, folder_id: str) -> List[Dict[str, Any]]:
        response = self.drive_service.files().list(
            q=f"'{folder_id}' in parents and trashed=false",
            fields="files(id, name, size)"
        ).execute()
        return response.get('files', [])

    def upload_file_to_folder(self, folder_id: str, file: UploadFile):
        file_metadata = {'name': file.filename, 'parents': [folder_id]}
        media = MediaFileUpload(file.file, resumable=True)
        uploaded_file = self.drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f'File ID: {uploaded_file.get("id")}')
        return uploaded_file

    def delete_file(self, key: str):
        try:
            self.drive_service.files().delete(fileId=key).execute()
        except Exception as e:
            print(e)

    def retry(self, func, retries=5, delay=5, backoff=2):
        for attempt in range(retries):
            try:
                return func()
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt < retries - 1:
                    import time
                    time.sleep(delay)
                    delay *= backoff
                else:
                    raise e

    def download_file(self, s3_file_key: str, local_file_path: str):
        try:
            request = self.drive_service.files().get_media(fileId=s3_file_key)
            with open(local_file_path, 'wb') as file:
                downloader = MediaIoBaseDownload(file, request)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                    print(f"Download {int(status.progress() * 100)}%.")
        except Exception as e:
            print(f"Error downloading file from Google Drive: {str(e)}")
            raise

    def set_ready(self):
        print("GoogleDriveStorageService is ready")

    def teardown(self):
        print("GoogleDriveStorageService is being torn down")

class GoogleDriveStorageServiceFactory(ServiceFactory):
    def __init__(self, access_token: str):
        self.access_token = access_token
    def create(self) -> GoogleDriveStorageService:
        return GoogleDriveStorageService(self.access_token)
