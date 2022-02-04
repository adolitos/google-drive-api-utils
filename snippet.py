from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


SCOPES = 'https://www.googleapis.com/auth/drive'
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scopes=SCOPES)

service = build('drive', 'v3', credentials=credentials)
results = service.files().list(pageSize=10, fields="nextPageToken, files(id, name)",driveId='0AXXXXXXXXXPVA',includeItemsFromAllDrives=True,corpora='drive',supportsAllDrives=True).execute()
items = results.get('files', [])

if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print(u'{0} ({1})'.format(item['name'], item['id']))

        print('Test with delete method.')
        try:
            service.files().delete(fileId=item['id'],supportsAllDrives=True).execute()
            print("Item deleted. {0}".format(item['name']))
        except Exception as e:
            print("Failure on deleting file: {0}".format(str(e)))
            #raise Exception(e)
