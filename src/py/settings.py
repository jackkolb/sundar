def get_duration():
    with open("settings/duration", "r") as duration_file:
        duration = duration_file.read()
    return duration

def get_rate():
    with open("settings/rate", "r") as rate_file:
        rate = rate_file.read()
    return rate

def get_flashdrive():
    with open("settings/flashdrive", "r") as flashdrive_file:
        if flashdrive_file.read() == "true":
            return True
        else:
            return False

def get_serial():
    with open("/proc/cpuinfo", "r") as cpu_info_file:
        lines = cpu_info_file.readlines()
        serial = [x for x in lines if "Serial" in x][0].split(":")[1][1:-1]
    return serial