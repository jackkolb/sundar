import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


# logins to google drive
def login():
    global gauth, drive
    gauth = GoogleAuth()  # general authentication object

    # Load the credentials file
    gauth.LoadCredentialsFile("drive_api_keys/credentials.json")
    if gauth.credentials is None:  # if the credentials file does not exist, do the browser authentication
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:  # if the credentials are expired, refresh them
        gauth.Refresh()
    else:  # Authorize the saved credentials
        gauth.Authorize()

    gauth.SaveCredentialsFile("drive_api_keys/credentials.json")  # Save the current credentials to a file

    drive = GoogleDrive(gauth)  # Create GoogleDrive instance with authenticated GoogleAuth instance


def find_folders(fldname):
    file_list = drive.ListFile({
        'q': "title='{}' and mimeType contains 'application/vnd.google-apps.folder' and trashed=false".format(fldname)
    }).GetList()
    return file_list


def upload_files_to_folder(fnames, folder):
    for fname in fnames:
        nfile = drive.CreateFile({'title': os.path.basename(fname),
                                  'parents': [{u'id': folder['id']}]})
        nfile.SetContentFile(fname)
        nfile.Upload()


def upload_file(filename, folder):
    try:
        login()
        logs_folder = find_folders(folder)[0]
        upload_files_to_folder([filename], logs_folder)
        return 1
    except:
        return 0
