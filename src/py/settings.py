def get_duration():
    with open("flags/duration", "r") as duration_file:
        duration = duration_file.read()
    return duration

def get_rate():
    with open("flags/rate", "r") as rate_file:
        rate = rate_file.read()
    return rate