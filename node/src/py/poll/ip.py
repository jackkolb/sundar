# ip.py: IP Module, updates the device's current IP address via Speck

import socket  # used to get the device's IP address
import requests  # used to send GET requests to Speck
import time  # used to add a time delay

# get_ip_address: gets the device's current IP address
def get_ip_address():
    ip_address = 'INITIAL'
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
    except OSError:
        ip_address = "FAIL"
    return ip_address


# get_speck_credentials: gets the speck credentials from the speck settings file
def get_speck_credentials():
    speck_id = ""
    speck_key = ""
    with open("settings/speck", "r") as speck_credentials:
        words = speck_credentials.readline().split(" ")
        if len(words) == 2:
            speck_id = words[0]
            speck_key = words[1]
    return speck_id, speck_key


# speck_create: create a new speck, writes the credentials to a settings file
def speck_create():
    url = "https://kolb.dev/speck"
    params = { "id": "new" }
    r = requests.get(url=url, params=params)
    data = r.text.split("\n")
    speck_id = data[2].split(" ")[1]
    speck_key = data[3].split(" ")[1]
    with open("settings/speck", "w") as speck_credentials:
        speck_credentials.write(speck_id + " " + speck_key)
    return speck_id, speck_key


# speck_read: read the speck IP address
def speck_read():
    url = "https://kolb.dev/speck"
    speck_id, speck_key = get_speck_credentials()  # if credentials do not exists, make a new speck
    if speck_id == "":
        speck_id, speck_key = speck_create()
    params = {
        "id": speck_id,
        "key": speck_key
    }
    r = requests.get(url=url, params=params)
    ip_address = r.text
    return ip_address


# speck_write: write the speck IP address
def speck_write(text):
    url = "https://kolb.dev/speck"
    speck_id, speck_key = get_speck_credentials()
    if speck_id == "":
        speck_id, speck_key = speck_create()
    params = {
        "id": speck_id,
        "key": speck_key,
        "data": text
    }
    r = requests.get(url=url, params=params)
    if r.text == "success":
        return True
    else:
        return False


# start_speck: continuously update IP address on the IP change
def start_speck():
    speck_ip = speck_read()
    while True:
        current_ip = get_ip_address()
        if current_ip != speck_ip:
            py.logs("SPECK", "updated speck IP address")
            speck_write(current_ip)
            time.sleep(5)
            speck_ip = current_ip
        time.sleep(30)