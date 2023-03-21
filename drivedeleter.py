import os
import pickle
import google.auth
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def get_credentials():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def delete_file(service, file_id):
    try:
        service.files().delete(fileId=file_id).execute()
        print(f'File with ID "{file_id}" permanently deleted.')
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None

def main():
    creds = get_credentials()
    service = build('drive', 'v3', credentials=creds)
    
    # Replace 'file_id' with the ID of the file or folder you want to delete
    file_id = 'REPLACE_WITH_FILE_OR_FOLDER_ID'
    delete_file(service, file_id)

if __name__ == '__main__':
    main()
