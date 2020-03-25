"""
LCD Module: runs the LCD display. To start the module, run start_lcd()
"""

import time
from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time
import socket
import subprocess
import py.logs


lcd = "PLACEHOLDER"

wifi_name = "no wifi"
wifi_counter = 0

disk_usage_previous = ""

char_wifi = "\x00"
char_no_wifi = "\x01"
char_collecting = "\x02"
char_not_collecting = "\x03"

charflag = "*"

def dispip(ip):
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(6, GPIO.LOW)
    time.sleep(1)

    for c in ip:
        time.sleep(5)
        print(c)
        i = -1
        try:
            i = int(c)
        except:
            pass
        if i != -1:
            if i == 0:
                i = 11
            for x in range(i):
                GPIO.output(6, GPIO.HIGH)
                time.sleep(.25)
                GPIO.output(6, GPIO.LOW)
                time.sleep(.25)
 

# gets the Pi's current IP address
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
        wifi_name = str(output).split('"')[1] + "      "
        
    except OSError:
        ip_address = "FAIL"
        wifi_name = "FAIL"
    return ip_address, wifi_name

# used for the "active" indicator, changes the character
def charflag_flip():
    global charflag
    if charflag == "-":
        charflag = "*"
    else:
        charflag = "-"

# returns the device name
def device_name():
    name = "INITIAL"
    try:
        with open("./settings/name", "r") as name_file:
            name = name_file.readline()
    except Exception:
        name = "empty"
    return name

# gets the current disk full as a percent (ex: 39%)
def get_disk_usage():
    p = subprocess.Popen("df", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    usage = [x for x in str(output).split("\\n")[1].split(" ") if "%" in x][0]
    return usage

# initializes the LCD display
def lcd_init():
    global lcd
    pin_rs = 21 # Board: 40
    pin_e = 20  # Board: 38
    pins_data = [16, 26, 19, 13] # Board: 36, 37, 35, 33
    lcd = CharLCD(numbering_mode=GPIO.BCM, cols=16, rows=2, pin_rs=pin_rs, pin_rw=None, pin_e=pin_e, pins_data=pins_data)
    lcd.clear()

# updates the display with the latest information
def update():
    # display wifi information
    global wifi_counter, disk_usage_previous
    ip, wifi_name = get_ip_address()
    if ip != "FAIL":
        lcd.cursor_pos = (0, 0)
        if wifi_counter >= 0:
             lcd.write_string(char_wifi + " " + ip)
        else:
             lcd.write_string(char_wifi + " " + wifi_name)
        wifi_counter = wifi_counter + 1
        if wifi_counter >= 4:
            wifi_counter = -4
    else:
        lcd.cursor_pos = (0, 0)
        lcd.write_string(char_no_wifi + " " + "No WiFi!     ")

    #dispip(ip)  # blink the IP address

    # display device name
    with open("flags/collection", "r") as collection_flag_file:
        collection_flag = collection_flag_file.readline()
    name = device_name()
    lcd.cursor_pos = (1, 0)
    # write the collecting character
    if collection_flag == "true":
        lcd.write_string(char_collecting)
    else:
        lcd.write_string(char_not_collecting)
    # write the device name
    if len(name) > 10:
        name = name[:10]
    elif len(name) < 10:
        name = name + " " * (10 - len(name))
    lcd.write_string(" " + name)

    # display disk usage
    disk_usage = get_disk_usage()
    if disk_usage != disk_usage_previous:
        lcd.cursor_pos = (1, 13)
        lcd.write_string(disk_usage)
        disk_usage_previous = disk_usage

    # display activity indicator
    lcd.cursor_pos = (0, 15)
    lcd.write_string(charflag)
    charflag_flip()

# generates the custom characters
def custom_chars():
    wifi = (
        0b10001,
        0b10101,
        0b01010,
        0b00000,
        0b00001,
        0b00010,
        0b10100,
        0b01000
    )
    lcd.create_char(0, wifi)

    no_wifi = (
        0b10001,
        0b10101,
        0b01010,
        0b00000,
        0b00000,
        0b01010,
        0b00100,
        0b01010
    )
    lcd.create_char(1, no_wifi)

    collecting = (
        0b00110,
        0b01000,
        0b00110,
        0b00000,
        0b00001,
        0b00010,
        0b10100,
        0b01000
    )
    lcd.create_char(2, collecting)

    not_collecting = (
        0b00110,
        0b01000,
        0b00110,
        0b00000,
        0b00000,
        0b01010,
        0b00100,
        0b01010
    )
    lcd.create_char(3, not_collecting)

# starts the LCD module
def start_lcd():
    lcd_init()
    custom_chars()
    while True:
        update()
        time.sleep(.25)
    GPIO.cleanup()
    py.logs.log("lcd", "finished LCD module")
