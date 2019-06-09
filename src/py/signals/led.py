import time
import RPi.GPIO as GPIO

LED_DAMAGE_PIN_R = 17  # Board: 11
LED_DAMAGE_PIN_G = 27  # Board: 13
LED_DAMAGE_PIN_B = 22  # Board: 15

def leds_green():
    GPIO.output(LED_DAMAGE_PIN_R, 0)
    GPIO.output(LED_DAMAGE_PIN_G, 1)
    GPIO.output(LED_DAMAGE_PIN_B, 0)

def leds_yellow():
    GPIO.output(LED_DAMAGE_PIN_R, 1)
    GPIO.output(LED_DAMAGE_PIN_G, 1)
    GPIO.output(LED_DAMAGE_PIN_B, 0)

def leds_red():
    GPIO.output(LED_DAMAGE_PIN_R, 1)
    GPIO.output(LED_DAMAGE_PIN_G, 0)
    GPIO.output(LED_DAMAGE_PIN_B, 0)

def start_led():
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

        time.sleep(30)
