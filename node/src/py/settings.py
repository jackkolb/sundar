# settings.py: contains functions for the node settings

import os  # used to check if file paths exist

# get_duration: gets the sampling duration
def get_duration():
    with open("settings/duration", "r") as duration_file:
        duration = duration_file.read()
    return duration


# get_rate: sets the sampling rate
def get_rate():
    with open("settings/rate", "r") as rate_file:
        rate = rate_file.read()
    return rate


# get_flashdrive: gets the flashdrive toggle (whether the data is written to a connected flashdrive)
def get_flashdrive():
    with open("settings/flashdrive", "r") as flashdrive_file:
        if flashdrive_file.read() == "true":
            return True
        else:
            return False


# get_serial: gets the serial # of the device
def get_serial():
    with open("/proc/cpuinfo", "r") as cpu_info_file:
        lines = cpu_info_file.readlines()
        serial = [x for x in lines if "Serial" in x][0].split(":")[1][1:-1]
    return serial


# check_settings: checks the existence of the settings files/flags, if they don't exist they are generated
def check_settings():
    # check settings files
    if not os.path.exists("settings/active"):
        with open("settings/active", "w") as f:
            f.write("false")
    if not os.path.exists("settings/delay"):
        with open("settings/active", "w") as f:
            f.write("60")
    if not os.path.exists("settings/duration"):
        with open("settings/active", "w") as f:
            f.write("20")
    if not os.path.exists("settings/flashdrive"):
        with open("settings/active", "w") as f:
            f.write("false")
    if not os.path.exists("settings/name"):
        with open("settings/active", "w") as f:
            f.write("Unnamed")
    if not os.path.exists("settings/rate"):
        with open("settings/active", "w") as f:
            f.write("1000")
    if not os.path.exists("settings/speck"):
        with open("settings/active", "w") as f:
            f.write("")

    # check flag files
    if not os.path.exists("flags/collection"):
        with open("settings/collection", "w") as f:
            f.write("false")
    if not os.path.exists("flags/damage"):
        with open("settings/collection", "w") as f:
            f.write("5")
    if not os.path.exists("flags/destination"):
        with open("settings/collection", "w") as f:
            f.write("data/")
    if not os.path.exists("flags/git_flag"):
        with open("settings/collection", "w") as f:
            f.write("GOOD")
    if not os.path.exists("flags/LED"):
        with open("settings/collection", "w") as f:
            f.write("false")

    # the email system handles the gmail setting (in py.logs)
