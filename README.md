# Permanent-GDrive-Cleaner
A Python Script to Permanently Delete Google Drive file and Folder without sending them to Trash.

# To use the provided Python script, follow these instructions:

### 1. Enable the Google Drive API:

- Go to the Google Cloud Console.
- Create a new project or select an existing one.
- Search for "Google Drive API" and enable it for your project.
- Go to the "Credentials" tab and click "Create credentials."
- Select "OAuth client ID" and choose "Desktop app" as the application type.
- Download the generated JSON file (credentials.json).

### 2. Install necessary Python packages:

- Open your terminal or command prompt.
- Install the required packages using pip by running the following command:
```
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```
### 3. Create a Python Script:
- Create a new Python file (e.g., delete_gdrive_file.py) and copy the provided script into the file.
- Place the downloaded credentials.json file in the same folder as the Python script.
### 4. Modify the Python script:
- Replace 'REPLACE_WITH_FILE_OR_FOLDER_ID' in the script with the ID of the file or folder you want to delete. You can find the ID in the Google Drive URL when you open the file or folder.
### 5. Run the script:
- In the terminal or command prompt, navigate to the folder containing the script and credentials.json file.
- Run the script using the following command:
```
python delete_gdrive_file.py
```
- On the first run, a new browser window will open, prompting you to authorize the application. Log in with your Google account and allow the required permissions.
- After authorization, the script will delete the specified file or folder permanently from your Google Drive.

Remember, permanently deleting files or folders is irreversible. Use this script with caution.
