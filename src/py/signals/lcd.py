import time
from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time
import socket
import subprocess

lcd = "PLACEHOLDER"

wifi_name = "no wifi"
wifi_counter = 0

disk_usage_previous = ""

char_wifi = "\x00"
char_no_wifi = "\x01"
char_collecting = "\x02"
char_not_collecting = "\x03"

charflag = "*"

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

def charflag_flip():
    global charflag
    if charflag == "-":
        charflag = "*"
    else:
        charflag = "-"

def collection_file():
    name = "INITIAL"
    try:
        with open("./settings/out_file", "r") as out_file:
            name = out_file.readline()
    except Exception:
        name = "empty"
    return name


def get_disk_usage():
    p = subprocess.Popen("df", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    usage = [x for x in str(output).split("\\n")[1].split(" ") if "%" in x][0]
    return usage


def init_lcd():
    global lcd
    lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24])
    lcd.clear()

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

    # display collection information
    out_file = collection_file()
    if out_file != "" and out_file != "empty":
        lcd.cursor_pos = (1, 0)
        lcd.write_string(char_collecting + " " + out_file) # collecting
    else:
        lcd.cursor_pos = (1, 0)
        lcd.write_string("\x03" + " " + "           ") # not collecting

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

if __name__ == "__main__":
    init_lcd()
    custom_chars()
    while True:
        update()
        time.sleep(.25)
