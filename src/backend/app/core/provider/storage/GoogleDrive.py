import json
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from app.core.interface.service import ServiceFactory, StorageService
from typing import List, Dict

from app.core.provider.aws.SecretManager import SecretManagerService

class GoogleDriveStorageService(StorageService):
    def __init__(self, refresh_token: str):
        client_id = os.getenv("GOOGLE_CLIENT_ID")
        client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
        token_uri = "https://oauth2.googleapis.com/token"

        self.credentials = Credentials(
            # token=google_token,
            refresh_token=refresh_token,
            token_uri=token_uri,
            client_id=client_id,
            client_secret=client_secret
        )
        # self.credentials = Credentials(token=google_token)

        self.drive_service = build('drive', 'v3', credentials=self.credentials)

    def create_bucket_if_not_exists(self):
        print("Google Drive does not require bucket creation.")

    def create_directory(self, directory_name: str):
        file_metadata = {
            'name': directory_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = self.drive_service.files().create(body=file_metadata, fields='id').execute()
        print(f"Directory creation response: {file}")
        return file

    def list_objects(self, directory_name: str = ''):
        results = self.drive_service.files().list(pageSize=10, fields="files(id, name)").execute()
        items = results.get('files', [])
        return items

    def list_all_objects(self, directory_name: str = '') -> List[Dict]:
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

    def delete_directory(self, directory_name: str):
        try:
            query = f"'{directory_name}' in parents"
            response = self.drive_service.files().list(q=query, fields="files(id)").execute()
            for file in response.get('files', []):
                self.delete_file(file['id'])
            # 디렉토리 자체를 삭제하는 방법이 필요하면 추가합니다.
        except Exception as e:
            print(e)

    def upload_file(self, file, file_location: str):
        file_metadata = {'name': file_location}
        media = MediaFileUpload(file, resumable=True)
        file = self.drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f'File ID: {file.get("id")}')

    def delete_file(self, key: str):
        try:
            self.drive_service.files().delete(fileId=key).execute()
        except Exception as e:
            print(e)

    def list_files(self, directory_name: str = ''):
        return self.list_objects(directory_name)

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
    def __init__(self, google_token: str):
        self.google_token = google_token

    def create(self) -> GoogleDriveStorageService:
        return GoogleDriveStorageService(self.google_token)
