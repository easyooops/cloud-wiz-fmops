import os

from fastapi import HTTPException
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError


class GoogleDriveService:
    def __init__(self, google_token: str, refresh_token: str, client_id: str, client_secret: str, token_uri: str):
        self.creds = Credentials(
            token=google_token,
            refresh_token=refresh_token,
            token_uri=token_uri,
            client_id=client_id,
            client_secret=client_secret
        )
        self.service = build('drive', 'v3', credentials=self.creds)
        self.folder_mime_type = 'application/vnd.google-apps.folder'

    def list_files(self, folder_id=None):
        query = f"'{folder_id}' in parents" if folder_id else None
        results = self.service.files().list(q=query, spaces='drive', pageSize=100, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        return items

    def upload_file(self, file_path, folder_id=None):
        file_metadata = {
            'name': os.path.basename(file_path),
            'parents': [folder_id] if folder_id else []
        }
        media = MediaFileUpload(file_path, resumable=True)
        file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id')

    def create_folder(self, name, parent_id=None):
        file_metadata = {
            'name': name,
            'mimeType': self.folder_mime_type,
            'parents': [parent_id] if parent_id else []
        }
        folder = self.service.files().create(body=file_metadata, fields='id').execute()
        return folder.get('id')

    def delete_file(self, file_id):
        try:
            self.service.files().delete(fileId=file_id).execute()
        except HttpError as error:
            print(f'An error occurred: {error}')
            return None
        return True

    def get_folder_info(self, folder_id):
        files = self.list_files(folder_id)
        total_size = 0
        file_count = 0
        for file in files:
            if file['mimeType'] != self.folder_mime_type:
                total_size += int(file.get('size', 0))
                file_count += 1
        return {
            'total_size': total_size,
            'file_count': file_count
        }

    def get_folder_info_by_name(self, folder_name):
        results = self.service.files().list(q=f"name='{folder_name}' and mimeType='{self.folder_mime_type}'", spaces='drive', fields="files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            raise HTTPException(status_code=404, detail=f"Folder {folder_name} not found")
        folder_id = items[0]['id']
        return self.get_folder_info(folder_id)