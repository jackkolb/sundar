import RPi.GPIO as GPIO
import time

# Two buttons: collection, and power to LCD
# The power to LCD btton doesn't need to be polled, as
# it is directly linked to the power supply of the LCD

BUTTON_PIN = 1 # Board: 1

def swap_flag():
    with open("flags/collect", "rw") as collection_flag:
        status = collection_flag.readline()
        if status == "COLLECT":
            status = "IDLE"
        else:
            status = "COLLECT"
        collection_flag.write(status)

def poll_collection_button():
    GPIO.setup(BUTTON_PIN, GPIO.IN)
    prior_collection = False
    while True:
        button_input = GPIO.input(BUTTON_PIN)
        if button_input:
            if prior_collection:
                swap_flag()
            prior_collection = True
        else:
            prior_collection = False

        time.sleep(1)
        
