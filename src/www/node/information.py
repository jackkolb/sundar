# wrappers to various information units

def load_life():
    with open("data/life", "r") as life_file:
        life = life_file.read()
    return life

def load_name():
    with open("settings/name", "r") as name_file:
        name = name_file.read() 
    return name

def set_name(name):
    with open("settings/name", "w") as name_file:
        name_file.write(name)
    return "good"

def load_active():
    try:
        with open("settings/active", "r") as active_file:
            active = active_file.read()
    except:
        active = "ERROR LOAD_ACTIVE()"
    return active

def set_active(state):
    with open("settings/active", "w") as active_file:
        active_file.write(state)
    return "good"

def load_data():
    with open("data/classifier.data", "r") as data_file:
        data = data_file.read()
    return data

def set_data(data):
    with open("data/classifier.data", "w") as data_file:
        data_file.write(data)
    return "good"

def load_rate():
    with open("settings/rate", "r") as rate_file:
        rate = rate_file.read()
    return rate

def set_rate(rate):
    with open("settings/rate", "w") as rate_file:
        rate_file.write(rate)
    return "good"

def load_duration():
    with open("settings/duration", "r") as duration_file:
        duration = duration_file.read()
    return duration

def set_duration(data):
    with open("settings/duration", "w") as duration_file:
        duration_file.write(data)
    return "good"

def load_flashdrive():
    with open("settings/flashdrive", "r") as flashdrive_file:
        state = flashdrive_file.read()
    return state

def set_flashdrive(state):
    with open("settings/flashdrive", "w") as flashdrive_file:
        flashdrive_file.write(state)
    return "good"

def load_logs():
    with open("data/logs", "r") as logs_file:
        logs = logs_file.read()
    return logs

def reset_logs():
    with open("data/logs", "w") as logs_file:
        logs_file.write("")

def reset_data():
    with open("data/classifier.data", "w") as data_file:
        data_file.write("")

def flash_LED():
    with open("flags/LED", "w") as led_file:
        led_file.write("true")

def reset_flash_LED():
    with open("flags/LED", "w") as led_file:
        led_file.write("false")

def load_flash_led():
    with open("flags/LED", "r") as led_file:
        value = led_file.read()
        return value

def load_information():
    information = {
        "life": load_life(),
        "name": load_name(),
        "active": load_active(),
        "flashdrive": load_flashdrive(),
        "data": load_data(),
        "duration": load_duration(),
        "rate": load_rate()
    }
    return information

def load_settings():
    settings = {
        "active": load_active(),
        "rate": load_rate(),
        "duration": load_duration(),
        "flashLED": load_flash_led(),
        "flashdrive": load_flashdrive()
    }
    reset_flash_LED()
    return settings
