# settings.py: contains functions for setting device information used by the settings

# get_serial: gets the device's serial number
def get_serial():
    with open("/proc/cpuinfo", "r") as cpu_info_file:
        lines = cpu_info_file.readlines()
        try:
            serial = [x for x in lines if "Serial" in x][0].split(":")[1][1:-1]
        except:
            return "NOSERIAL"
    return serial
