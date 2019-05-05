from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os


# Authenticate the client.
gauth = GoogleAuth()
# Load the credentials file
gauth.LoadCredentialsFile("./credentials.json")
if gauth.credentials is None:  # if the credentials file does not exist, do the browser authentication
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:  # if the credentials are expired, refresh them
    gauth.Refresh()
else:  # Authorize the saved credentials
    gauth.Authorize()

gauth.SaveCredentialsFile("./credentials.json")  # Save the current credentials to a file

drive = GoogleDrive(gauth)


def find_folders(fldname):
    file_list = drive.ListFile({
        'q': "title='{}' and mimeType contains 'application/vnd.google-apps.folder' and trashed=false".format(fldname)
    }).GetList()
    return file_list


def get_file_tree(parent_name):
    parent_id = find_folders(parent_name)[0]
    print(parent_id)
    input()
    overall_tree_list = []
    file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % parent_id}).GetList()

    for f in file_list:
        if f['mimeType'] == 'application/vnd.google-apps.folder':  # if folder
            overall_tree_list.append({"id": f['id'], "title": f['title'], "list": get_file_tree(f['id'])})
        else:
            overall_tree_list.append(f['title'])
    return overall_tree_list


def upload_files_to_folder(fname, folder):
    nfile = drive.CreateFile({'title': os.path.basename(fname),
                                  'parents': [{u'id': folder['id']}]})
    nfile.SetContentFile(fname)
    nfile.Upload()


def upload_file(filename, folder):
#   try:
    upload_folder = find_folders(folder)[0]
    nfile = drive.CreateFile({'title': os.path.basename(filename), 'parents': [{u'id': upload_folder['id']}]})
    nfile.SetContentFile(filename)
    nfile.Upload()
    return 1

#    except Exception as e:
#        print("upload failed: " + str(e))
#        return 0


print(str(len(get_file_tree("data"))))
#input()
#upload_file("./src/settings.py", "SundarLab")
