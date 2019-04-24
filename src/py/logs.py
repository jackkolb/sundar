import datetime


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


# appends a message to the day's log file
def log(message):
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

    entry_time = "[ " + str(year) + "-" + str(month) + "-" + str(day)\
                 + " " + str(hour) + ":" + str(minute) + ":" + str(second) + " ]"
    entry = entry_time + " " + message + "\n"

    try:
        filename = "logs/" + "_log_" + "pi" "_" + str(year) + "_" + str(month) + "_" + str(day)
        with open(filename, "a") as log_file:
            log_file.write(entry)
    except Exception as e:
        print(5, "[ERROR] failed to open file: " + str(e))

    print(entry[:-1])
    return
