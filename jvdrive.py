import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

class GoogleDriveHelper:
    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/drive']
        self.service = None
        self._authenticate()
    
    def _authenticate(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        
        self.service = build('drive', 'v3', credentials=creds)
    
    def upload_file(self, file_path, folder_id=None):
        try:
            file_metadata = {'name': os.path.basename(file_path)}
            if folder_id:
                file_metadata['parents'] = [folder_id]
            
            media = MediaFileUpload(file_path, resumable=True)
            file = self.service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id, webViewLink'
            ).execute()
            
            # Make file publicly accessible
            self.service.permissions().create(
                fileId=file['id'],
                body={'role': 'reader', 'type': 'anyone'}
            ).execute()
            
            return file['webViewLink']
        except HttpError as error:
            print(f'An error occurred: {error}')
            return None
    
    def create_folder(self, folder_name, parent_id=None):
        try:
            folder_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            if parent_id:
                folder_metadata['parents'] = [parent_id]
            
            folder = self.service.files().create(
                body=folder_metadata,
                fields='id'
            ).execute()
            
            return folder['id']
        except HttpError as error:
            print(f'An error occurred: {error}')
            return None