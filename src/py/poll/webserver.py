# Manages the webserver: moves data from the data/ location
# to the webserver, and retrieves webserver settings that
# manage collection

import urllib3
import requests
import time
try:
    import src.py.poll.led
except:
    try:
        import py.poll.led
    except:
        try:
            import poll.led
        except:
            try:
                import led
            except:
                try:
                    print(":(")
                    #import .led
                except:
                    pass



# Manages the webserver, interacting via POST requests 
def manage_webserver():
    while True:
        # update webserver's data
        r = requests.post("http://0.0.0.0:5000/data", json={"data": get_data()})

        # read settings from webserver
        r = requests.get("http://0.0.0.0:5000/settings")
        print(r)
        set_active(r.json()["active"])
        set_rate(r.json()["rate"])
        set_duration(r.json()["duration"])
        set_flash(r.json()["flash"])
        set_flashdrive(r.json()["flashdrive"])

        # sleep
        time.sleep()


# functions to get and set information
# reads data from data file
def get_data():
    with open("data/classifier.data", "r") as data_file:
        data = data_file.read()
    return data

# writes active state
def set_active(status):
    with open("settings/active", "w") as active_flag:
        active_flag.write(status)

# writes rate frequency
def set_rate(status):
    with open("settings/rate", "w") as rate_flag:
        rate_flag.write(status)

# writes duration time
def set_duration(status):
    with open("settings/duration", "w") as duration_flag:
        duration_flag.write(status)

# writes the flashdrive status
def set_flashdrive(status):
    with open("settings/flashdrive", "w") as flashdrive_flag:
        flashdrive_flag.write(status)

# checks if should flash the LEDs
def set_flash(status):
    if status == "true":
        with open("flags/LED", "r") as LED_flag:
            LED_flag.write("true")