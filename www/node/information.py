# wrappers to various information units

def load_life():
    with open("data/life", "r") as life_file:
        life = life_file.read()
    return life

def load_name():
    with open("data/name", "r") as name_file:
        name = name_file.read() 
    return name

def load_active():
    try:
        with open("data/active", "r") as active_file:
            active = active_file.read()
    except:
        active = "ERROR LOAD_ACTIVE()"
    return active

def set_active(settings):
    with open("data/active", "w") as active_file:
        active_file.write(state)
    return "good"

def load_data():
    with open("data/data", "r") as data_file:
        data = data_file.read()
    return data

def set_data(data):
    with open("data/data", "w") as data_file:
        data_file.write(data)
    return "good"

def load_rate():
    with open("data/rate", "r") as rate_file:
        rate = rate_file.read()
    return rate

def load_duration():
    with open("data/duration", "r") as duration_file:
        duration = duration_file.read()
    return duration


def load_information():
    information = {
        "life": load_life(),
        "name": load_name(),
        "active": load_active(),
        "data": load_data()
    }
    return information


def load_settings():
    settings = {
        "active": load_active(),
        "rate": load_rate(),
        "duration": load_duration()
    }
    return settings