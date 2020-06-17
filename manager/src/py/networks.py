# networks.py: contains several functions for communicating with nodes and Specks
import subprocess  # used for system calls
import requests  # used for network requests
import socket  # used for getting this device's IP address
import nmap  # used for scanning for connections
import os  # used for system calls in support of subprocess


# ping: a simple ping function
def ping(ip):
    return subprocess.call(['ping', ip, '-c', '1', '-W', '.1'], stdout=open(os.devnull, 'w')) == 0


# generate_scan_range: generates a range of IP address blocks to check given two IP address inputs (low/high)
def generate_scan_range(low, high):
    low_blocks = [int(x) for x in low.split(".")[:3]]
    high_blocks = [int(x) for x in high.split(".")[:3]]

    current_scan = low_blocks
    blocks = []

    while current_scan != high_blocks:
        blocks.append(list(current_scan))
        current_scan[2] += 1
        if current_scan[2] == 256:
            current_scan[2] == 0
            current_scan[1] += 1
        if current_scan[1] == 256:
            current_scan[1] == 0
    blocks.append(high_blocks)

    blocks = [".".join([str(x) for x in i]) + ".0/24" for i in blocks]
    return blocks


# get_node_information: pings a given node IP address for its data
def get_node_information(ip):
    try:
        print("pinging node")
        response = requests.get("http://" + ip + "/information", timeout=2)
        print("got info")
    except:
        response = "FAIL"

    if response == "FAIL":
        return {}
    elif response.status_code == 200:
        if "serial" in response.json().keys():
            return response.json()
        else:
            return {}
    else:
        return {}


# get_speck: uses a given speck id and key to get its content (the node's IP address)
def get_speck(id, key):
    try:
        response = requests.get("http://kolb.dev/speck?id=" + id + "&key=" + key).text
    except:
        response = "FAIL"
    return response


# get_ip_address: gets this device's IP address
def get_ip_address():
    ip_address = 'INITIAL'
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()

        p = subprocess.Popen("iwgetid", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        wifi_name = str(output).split('"')[1]
        
    except OSError:
        ip_address = "FAIL"
        wifi_name = "FAIL"
    return ip_address, wifi_name
