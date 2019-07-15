import subprocess
import threading
import py.logs
import py.settings
import RPi.GPIO as GPIO
import os
import py.poll.lcd
import py.poll.led
import py.poll.location
import py.poll.gitcheck
import py.poll.webserver

def main():
    GPIO.setmode(GPIO.BCM)
    py.logs.log("[MAIN] Starting GitHub check thread")

    # launch git check thread -- checks if there are code updates, if there are it kills the program
    git_check_thread = threading.Thread(target=py.poll.gitcheck.git_check_loop)
    git_check_thread.start()

    # start LCD thread
    py.logs.log("[MAIN] Starting LCD thread")
    lcd_thread = threading.Thread(target=py.poll.lcd.start_lcd)
    lcd_thread.start()

    # start LED thread
    py.logs.log("[MAIN] Starting LED thread")
    led_thread = threading.Thread(target=py.poll.led.start_led)
    led_thread.start()

    # start webserver manager thread
    py.logs.log("[MAIN] Starting Webserver Manager thread")
    #webserver_thread = threading.Thread(target=py.poll.webserver.manage_webserver)
    #webserver_thread.start()

    # start location determination thread
    py.logs.log("[MAIN] Starting output location thread")
    location_thread = threading.Thread(target=py.poll.location.manage_output_location)
    location_thread.start()


    # general loop: launch collection script, when it dies relaunch it
    while True:
        try:
            with open("settings/active", "r") as collection_flag:
                status = collection_flag.readline()
        except:
            status == "false"
        if status == "true":
            destination = py.poll.location.get_output_location()
            if destination == "none":
                destination = "data/"
            accelerometer_destination = destination + "accelerometer.data"
            py.logs.log("[MAIN] Starting accelerometer collection: " + accelerometer_destination)
            sensor_process = subprocess.Popen(["./src/c/collect.o", py.settings.get_duration(), py.settings.get_rate(), accelerometer_destination])
            sensor_process.wait()  # wait for sensor thread to end, restart it if it does
            py.logs.log("[MAIN] Collection complete")
            py.logs.log("[MAIN] Starting classification")
            classifier_destination = destination + "classifier.data"
            # RUN CLASSIFICATION FUNCTION HERE
            py.logs.log("[MAIN] Classification completed")

        if py.poll.gitcheck.check_flag_file() == "RESET":
            os._exit(1)
