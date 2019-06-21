import subprocess
import time
import sys
import urllib.request
import RPi.GPIO as GPIO
import logs

wifi_check_led_pin = 8


# checks for new code every 10 minutes, if there is an update, pull it and restart processes
def wifi_check_loop():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(wifi_check_led_pin, GPIO.OUT)
    GPIO.output(wifi_check_led_pin, GPIO.LOW)

    result = "none"
    while True:
        old_result = result
        try:
            urllib.request.urlopen("http://www.ucr.edu")
            result = "good"
        except:
            result = "bad"

        if result == "bad" and old_result != result:  # wifi down
            logs.log("[WIFI] Wifi down")
            GPIO.output(wifi_check_led_pin, GPIO.LOW)
        if result == "good" and old_result != result:
            logs.log("[WIFI] Wifi up")
            GPIO.output(wifi_check_led_pin, GPIO.HIGH)
        time.sleep(3)  # waits 10 minutes