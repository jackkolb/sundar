# information.py: contains functions to read/write to data and settings files, and retrieve information
import py.logs as logs  # used for logging
import os  # used for file structure commands
import socket  # used for getting the device's IP address


# load_life: reads from the expected life remaining file
def load_life():
    with open("data/life", "r") as life_file:
        life = life_file.read()
    return life


# load_name: reads from the node name file
def load_name():
    with open("settings/name", "r") as name_file:
        name = name_file.read() 
    return name


# load_active: reads from the "is node actively running?" file
def load_active():
    try:
        with open("settings/active", "r") as active_file:
            active = active_file.read()
    except:
        active = "ERROR LOAD_ACTIVE()"
    return active


# load_history: reads from the classifier results file (shows damage level vs. time)
def load_history():
    with open("data/classifier.data", "r") as data_file:
        data = [x.split(" ") for x in data_file.read().split("\n")]
    return data


# set_data: writes the input as the classifier results file (overwrites everything)
def set_data(data):
    with open("data/classifier.data", "w") as data_file:
        data_file.write(data)
    return "good"


# load_rate: reads from the sampling rate file
def load_rate():
    with open("settings/rate", "r") as rate_file:
        rate = rate_file.read()
    return rate


# load_delay: reads from the sampling delay file
def load_delay():
    with open("settings/delay", "r") as rate_file:
        rate = rate_file.read()
    return rate


# load_duration: reads from the sampling duration file
def load_duration():
    with open("settings/duration", "r") as duration_file:
        duration = duration_file.read()
    return duration


# load_flashdrive: reads from the "write to flashdrive?" file
def load_flashdrive():
    with open("settings/flashdrive", "r") as flashdrive_file:
        state = flashdrive_file.read()
    return state


# load_speck: gets the value of the speck file
def load_speck():
    with open("settings/speck", "r") as speck_file:
        speck = speck_file.read()
    return speck


# load_all_logs: gets all the log file names
def load_all_logs():
    log_list = os.listdir("logs/")
    return log_list


# logs_logs: reads the log file
def load_logs():
    with open("logs/" + logs.generate_log_name(), "r") as logs_file:
        logs = logs_file.read()
    return logs


# load_serial: gets the device serial number
def load_serial():
    with open("/proc/cpuinfo", "r") as cpu_info_file:
        lines = cpu_info_file.readlines()
        serial = [x for x in lines if "Serial" in x][0].split(":")[1][1:-1]
        start_index = 0
        for i in range(len(serial)):
            if serial[i] != '0':
                start_index = i
                break
        serial = serial[i:]
    return serial


# load_ip: get the device LAN IP address
def load_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()        
    except OSError:
        ip_address = "FAIL"
    return ip_address


# reset_logs: clears the log file
def reset_logs():
    with open("data/logs", "w") as logs_file:
        logs_file.write("")


# reset_data: clears the data file
def reset_data():
    with open("data/classifier.data", "w") as data_file:
        data_file.write("")


# flash_LED: writes "true" to the Flash LED flag (the LED process reads this and flashes the LEDs)
def flash_LED():
    with open("flags/LED", "w") as led_file:
        led_file.write("true")


# reset_flash_LED: writes "false" to the Flash LED flag
def reset_flash_LED():
    with open("flags/LED", "w") as led_file:
        led_file.write("false")


# load_flash_led: reads the value of the Flash LED flag
def load_flash_led():
    with open("flags/LED", "r") as led_file:
        value = led_file.read()
        return value


# updateSettings: updates a settings file as per a given file and value (used so there aren't ~5 individual functions)
def updateSettings(file, value):
    with open("settings/" + file, "w") as data_file:
        data_file.write(value)
        logs.log("webserver", file.upper() + " setting has been set to " + value)


# load_information: loads information displayed to the webserver's viewer
def load_information():
    information = {
        "life": load_life(),
        "name": load_name(),
        "active": load_active(),
        "flashdrive": load_flashdrive(),
        "history": load_history(),
        "duration": load_duration(),
        "rate": load_rate(),
        "delay": load_delay(),
        "speck": load_speck(),
        "serial": load_serial(),
        "ip": load_ip()
    }
    return information


# load_settings: returns the settings as a dictionary object
def load_settings():
    settings = {
        "active": load_active(),
        "rate": load_rate(),
        "duration": load_duration(),
        "flashLED": load_flash_led(),
        "flashdrive": load_flashdrive(),
        "delay": load_delay(),
        "speck": load_speck()
    }
    reset_flash_LED()
    return settings


# gets_logs_filenames: gets all the log file names
def get_logs_filenames():
    log_list = os.listdir("logs/")
    log_list.sort()
    log_list.reverse()
    return log_list


# get_raw_data_filenames: gets all the raw data file names
def get_raw_data_filenames():
    data_list = os.listdir("data/raw/")
    data_list.sort()
    data_list.reverse()
    return data_list


# get_daily_data_filenames: gets all the daily data file names
def get_daily_data_filenames():
    data_list = os.listdir("data/daily/")
    data_list.sort()
    data_list.reverse()
    return data_list