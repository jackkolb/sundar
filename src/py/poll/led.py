"""
LED Module: manages the LEDs. To start the module, run start_led()
"""

import time
import RPi.GPIO as GPIO

LED_DAMAGE_PIN_R = 17  # Board: 11
LED_DAMAGE_PIN_G = 27  # Board: 13
LED_DAMAGE_PIN_B = 22  # Board: 15

# turn on the green LED
def leds_green():
    GPIO.output(LED_DAMAGE_PIN_R, 0)
    GPIO.output(LED_DAMAGE_PIN_G, 1)
    GPIO.output(LED_DAMAGE_PIN_B, 0)

# turn on the yellow LED
def leds_yellow():
    GPIO.output(LED_DAMAGE_PIN_R, 1)
    GPIO.output(LED_DAMAGE_PIN_G, 1)
    GPIO.output(LED_DAMAGE_PIN_B, 0)

# turn on the red LED
def leds_red():
    GPIO.output(LED_DAMAGE_PIN_R, 1)
    GPIO.output(LED_DAMAGE_PIN_G, 0)
    GPIO.output(LED_DAMAGE_PIN_B, 0)

# turns on the blue LED
def leds_blue():
    GPIO.output(LED_DAMAGE_PIN_R, 0)
    GPIO.output(LED_DAMAGE_PIN_G, 0)
    GPIO.output(LED_DAMAGE_PIN_B, 1)

def leds_off():
    GPIO.output(LED_DAMAGE_PIN_R, 0)
    GPIO.output(LED_DAMAGE_PIN_G, 0)
    GPIO.output(LED_DAMAGE_PIN_B, 0)

# LOOP: reads from the damage flag, turns on the appropriate LED
def start_led():
    GPIO.setwarnings(False)
    GPIO.setup(LED_DAMAGE_PIN_R, GPIO.OUT)
    GPIO.setup(LED_DAMAGE_PIN_G, GPIO.OUT)
    GPIO.setup(LED_DAMAGE_PIN_B, GPIO.OUT)

    while True:
        with open("flags/damage", "r") as damage_flag:
            status = damage_flag.readline()
        if status == "1" or status == "2":
            leds_green()
        if status == "3":
            leds_yellow()
        if status == "4" or status == "5":
            leds_red()
        
        # check LED flag in case flash was called
        modify_flag = False
        with open("flags/LED", "r+") as led_flag:
            value = led_flag.read()
            if value == "true":
                flash_blue_led()
                led_flag.write("false")

        time.sleep(1)

def flash_blue_led():
    for i in range(10):
        leds_blue()
        time.sleep(.2)
        leds_off()
        time.sleep(.2)
    return