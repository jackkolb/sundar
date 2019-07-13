import subprocess
import threading
import logs
import settings
import RPi.GPIO as GPIO
import os
import poll.lcd
import poll.led
import poll.location
import poll.gitcheck
import poll.webserver

def main():
    GPIO.setmode(GPIO.BCM)
    logs.log("[MAIN] Starting GitHub check thread")

    # launch git check thread -- checks if there are code updates, if there are it kills the program
    git_check_thread = threading.Thread(target=poll.gitcheck.git_check_loop)
    git_check_thread.start()

    # start LCD thread
    logs.log("[MAIN] Starting LCD thread")
    lcd_thread = threading.Thread(target=poll.lcd.start_lcd)
    lcd_thread.start()

    # start LED thread
    logs.log("[MAIN] Starting LED thread")
    lcd_thread = threading.Thread(target=poll.led.start_led)
    lcd_thread.start()

    # start webserver manager thread
    logs.log("[MAIN] Starting Webserver Manager thread")
    webserver_thread = threading.Thread(target=poll.webserver.manage_webserver)
    webserver_thread.start()

    # start location determination thread
    logs.log("[MAIN] Starting output location thread")
    location_thread = threading.Thread(target=poll.location.manage_output_location)
    location_thread.start()

    # general loop: launch collection script, when it dies relaunch it
    while True:
        try:
            with open("settings/active", "r") as collection_flag:
                status = collection_flag.readline()
        except:
            status == "false"
        if status == "true":
            destination = poll.location.get_output_location()
            if destination == "none":
                destination = "data/"
            accelerometer_destination = destination + "accelerometer.data"
            logs.log("[MAIN] Starting accelerometer collection: " + settings.get_duration() + ", " + settings.get_rate())
            sensor_process = subprocess.Popen(["./src/c/collect.o", settings.get_duration(), settings.get_rate(), accelerometer_destination])
            sensor_process.wait()  # wait for sensor thread to end, restart it if it does
            logs.log("[MAIN] Collection complete")
            logs.log("[MAIN] Starting classification")
            classifier_destination = destination + "classifier.data"
            # RUN CLASSIFICATION FUNCTION HERE
            logs.log("[MAIN] Classification completed")

        if poll.gitcheck.check_flag_file() == "RESET":
            os._exit(1)
