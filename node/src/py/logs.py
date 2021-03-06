# logs.py: contains functions for logging system messages
import datetime  # used to get the current date and time
import smtplib, ssl  # used to send emails

# get_date: gets the current date in the form YYYY_MM_DD
def get_date():
    now = datetime.datetime.now()
    year = now.year

    month = now.month
    if month < 10:
        month = "0" + str(month)

    day = now.day
    if day < 10:
        day = "0" + str(day)

    hour = now.hour
    if hour < 10:
        hour = "0" + str(hour)

    minute = now.minute
    if minute < 10:
        minute = "0" + str(minute)

    second = now.second
    if second < 10:
        second = "0" + str(second)

    return str(year) + "_" + str(month) + "_" + str(day)


# generate_log_name: uses the current date to determine the log file name
def generate_log_name():
    filename = "log_" + "pi" "_" + get_date()
    return filename


# generate_log_variables: gets the current year, month, day, hour, minute, and second
def generate_log_variables():
    now = datetime.datetime.now()
    year = now.year

    month = now.month
    if month < 10:
        month = "0" + str(month)

    day = now.day
    if day < 10:
        day = "0" + str(day)

    hour = now.hour
    if hour < 10:
        hour = "0" + str(hour)

    minute = now.minute
    if minute < 10:
        minute = "0" + str(minute)

    second = now.second
    if second < 10:
        second = "0" + str(second)

    return year, month, day, hour, minute, second


# log: appends a message to the day's log file
def log(module, message):
    filename = "logs/" + generate_log_name()

    year, month, day, hour, minute, second = generate_log_variables()

    entry_time = "[ " + str(year) + "-" + str(month) + "-" + str(day)\
                 + " " + str(hour) + ":" + str(minute) + ":" + str(second) + " ]"
    entry = entry_time + " [" + module.upper() + "] " + message

    try:
        with open(filename, "a") as log_file:
            log_file.write(entry + "\n")
    except Exception as e:
        print(5, "[ERROR] failed to open file: " + str(e))

    print(entry)  # also prints the message to the console
    return


# send_email: sends an email using gmail
def send_email(to, subject, message):
    # get gmail information
    with open("settings/gmail", "a+") as f:
        f.seek(0)  # read from beginning of file
        lines = f.readlines()
        if len(lines) != 2:  # check if email file is well formed
            log("logs", "Email information not set, must be two lines email / password")
        else:
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = lines[0] # Sender email address
            receiver_email = to  # Receiver email address
            password = lines[1]
            message = "Subject: " + subject + "\n\n" + message

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
    return
