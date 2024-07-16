from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials
from app.core.interface.service import ServiceFactory, StorageService

class GoogleDriveStorageService(StorageService):
    def __init__(self, credentials_json: str):
        self.credentials = Credentials.from_service_account_file(credentials_json)
        self.drive_service = build('drive', 'v3', credentials=self.credentials)

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
        results = self.drive_service.files().list(pageSize=10, fields="files(id, name)").execute()
        items = results.get('files', [])
        return items

    def create_directory(self, directory_name: str):
        file_metadata = {
            'name': directory_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = self.drive_service.files().create(body=file_metadata, fields='id').execute()
        print(f'Directory ID: {file.get("id")}')

    def set_ready(self):
        print("GoogleDriveStorageService is ready")

    def teardown(self):
        print("GoogleDriveStorageService is being torn down")


class GoogleDriveStorageServiceFactory(ServiceFactory):
    def __init__(self, credentials_json: str):
        self.credentials_json = credentials_json

    def create(self) -> GoogleDriveStorageService:
        return GoogleDriveStorageService(self.credentials_json)