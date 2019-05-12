import time
from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time
import socket

lcd = "PLACEHOLDER"

wifi = "off"
collecting = "no"

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
    except OSError:
        ip_address = "FAIL"
    return ip_address

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


def charflag_flip():
    global charflag
    if charflag == "-":
        charflag = "*"
    else:
        charflag = "-"


def init_lcd():
    global lcd
    lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24])


def update():
    ip = get_ip_address()
    if ip != "FAIL":        
        lcd.cursor_pos = (0, 0)
        lcd.write_string(char_wifi + " " + ip)
    else:
        lcd.cursor_pos = (0, 0)
        lcd.write_string(char_no_wifi + " " + "No WiFi!     ")

   
    if collecting == "yes":
        lcd.cursor_pos = (1, 0)
        lcd.write_string("\x02") # collecting
    else:   
        lcd.cursor_pos = (1, 0)
        lcd.write_string("\x03") # not collecting


    lcd.cursor_pos = (0, 15)
    lcd.write_string(charflag)
    charflag_flip()

if __name__ == "__main__":
    init_lcd()
    custom_chars()
    while True:
        update()
        time.sleep(.25)
