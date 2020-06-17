# buttons.py: contains functions for two buttons that can be used on the device
# currently these buttons are NOT used

import RPi.GPIO as GPIO  # used for GPIO input, to read the button state
import time  # used to make a time delay between polling

# Two buttons: collection, and power to LCD
# The power to LCD btton doesn't need to be polled, as
# it is directly linked to the power supply of the LCD

BUTTON_PIN = 1  # Board: 1

# swap_flag: switches the collect flag between COLLECT and IDLE
def swap_flag():
    with open("flags/collect", "rw") as collection_flag:
        status = collection_flag.readline()
        if status == "COLLECT":
            status = "IDLE"
        else:
            status = "COLLECT"
        collection_flag.write(status)


# poll_collection_button: polls the collection button, when pressed it swaps the collection flag
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
        
