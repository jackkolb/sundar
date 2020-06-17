# led.py: manages the LEDs. To start the module, run start_led()

# NOTE: the v1.1 iteration of the PCB does NOT have a multicolored LED!!! But the code is set up for one

import time  # used to set time delays
import RPi.GPIO as GPIO  # used to get GPIO pins
import py.logs  # used for logging

# board pins for each LED
LED_DAMAGE_PIN_R = 17  # Board: 11
LED_DAMAGE_PIN_G = 27  # Board: 13
LED_DAMAGE_PIN_B = 22  # Board: 15

# leds_green: turn the LED green
def leds_green():
    GPIO.output(LED_DAMAGE_PIN_R, 0)
    GPIO.output(LED_DAMAGE_PIN_G, 1)
    GPIO.output(LED_DAMAGE_PIN_B, 0)


# leds_yellow: turn the LED yellow
def leds_yellow():
    GPIO.output(LED_DAMAGE_PIN_R, 1)
    GPIO.output(LED_DAMAGE_PIN_G, 1)
    GPIO.output(LED_DAMAGE_PIN_B, 0)


# leds_red: turn the LED red
def leds_red():
    GPIO.output(LED_DAMAGE_PIN_R, 1)
    GPIO.output(LED_DAMAGE_PIN_G, 0)
    GPIO.output(LED_DAMAGE_PIN_B, 0)


# leds_blue: turn the LED blue
def leds_blue():
    GPIO.output(LED_DAMAGE_PIN_R, 0)
    GPIO.output(LED_DAMAGE_PIN_G, 0)
    GPIO.output(LED_DAMAGE_PIN_B, 1)


# leds_off: turn the LED off
def leds_off():
    GPIO.output(LED_DAMAGE_PIN_R, 0)
    GPIO.output(LED_DAMAGE_PIN_G, 0)
    GPIO.output(LED_DAMAGE_PIN_B, 0)


# start_led: reads from the damage flag, turns on the appropriate LED
def start_led():
    GPIO.setwarnings(False)
    GPIO.setup(LED_DAMAGE_PIN_R, GPIO.OUT)
    GPIO.setup(LED_DAMAGE_PIN_G, GPIO.OUT)
    GPIO.setup(LED_DAMAGE_PIN_B, GPIO.OUT)

    # loops to read the damage flag and turn on the corresponding LED
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


# flash_blue_led: flashes the LED blue
def flash_blue_led():
    py.logs.log("led", "Flashing blue LEDs")
    for i in range(10):
        leds_blue()
        time.sleep(.2)
        leds_off()
        time.sleep(.2)
    return