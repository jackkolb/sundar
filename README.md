# Sundar's Lab
Our Codebase for Sundar's Lab


## Modules:

### drive.py
Contains functions to manage the Google Drive

Usage:
```
import drive

# to upload a file
drive.upload_file("some_file.txt", "Folder")
```

All the authentication should be handled automatically, otherwise
the output will try opening a browser to login and reauthenticate.
Just login for the sundarlabucr@gmail.com account.


### email.py
Contains functions to manage email communications (and through that,
SMS communications for emergencies)

Usage:
```
import mail

# to send an email
mail.send_email("someone@gmail.com", "some subject", "some message")
```

### logs.py
Contains functions to manage the log files, will automatically write to
the current day's file

Usage:
```
import logs

# to add a log entry to the day's log file
logs.log("some message")
```