import subprocess
import threading
import logs
import settings as sensor_settings
import RPi.GPIO as GPIO
import os
import poll.lcd
import poll.led
import poll.location
import poll.gitcheck

def main():
    GPIO.setmode(GPIO.BCM)
    logs.log("[MAIN] Starting GitHub check thread")

    # launch git check thread -- checks if there are code updates, if there are it kills the program
    git_check_thread = threading.Thread(target=poll.gitcheck.git_check_loop)
    git_check_thread.start()

    # load settings
    logs.log("[MAIN] Loading settings")
    settings = sensor_settings.retrieve_settings()

    # start LCD thread
    logs.log("[MAIN] Starting LCD thread")
    lcd_thread = threading.Thread(target=poll.lcd.start_lcd)
    lcd_thread.start()

    # start LED thread
    logs.log("[MAIN] Starting LED thread")
    lcd_thread = threading.Thread(target=poll.led.start_led)
    lcd_thread.start()

    # start location determination thread
    logs.log("[MAIN] Starting output location thread")
    location_thread = threading.Thread(target=poll.location.set_output_location)
    location_thread.start()

    duration = 20
    rate = 1000

    # general loop: launch collection script, when it dies relaunch it
    while True:
        with open("flags/collection", "r") as collection_flag:
            status = collection_flag.readline()
            if status == "COLLECT":
                destination = poll.location.get_output_location()
                if destination == "none":
                    destination = "data/raw_data.txt"
                logs.log("[MAIN] Starting accelerometer collection")
                sensor_process = subprocess.Popen(["./src/c/collect.o", str(duration), str(rate), destination])
                sensor_process.wait()  # wait for sensor thread to end, restart it if it does
                logs.log("[MAIN] Collection complete")
        if poll.gitcheck.check_flag_file() == "RESET":
            os._exit(1)
