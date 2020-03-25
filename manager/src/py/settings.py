def get_serial():
    with open("/proc/cpuinfo", "r") as cpu_info_file:
        lines = cpu_info_file.readlines()
        try:
            serial = [x for x in lines if "Serial" in x][0].split(":")[1][1:-1]
        except:
            return "abcdefg"

    return serial