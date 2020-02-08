import datetime
import smtplib, ssl


def send_email(to, subject, message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "sundarlabucr@gmail.com"  # Enter your address
    receiver_email = to  # Enter receiver address
    password = open("src/py/gmail_password", "r").read()
    message = "Subject: " + subject + "\n\n" + message

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


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


# uses the current date to determine the log file name
def generate_log_name():
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

    filename = "log_" + "pi" "_" + str(year) + "_" + str(month) + "_" + str(day)    
    return filename

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


# appends a message to the day's log file
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

    print(entry)
    return
