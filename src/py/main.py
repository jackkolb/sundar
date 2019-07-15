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
import www.node.node_server
import shutil
import datetime

def main():
    GPIO.setmode(GPIO.BCM)
    py.logs.log("main", "Starting GitHub check thread")

    # launch git check thread -- checks if there are code updates, if there are it kills the program
    git_check_thread = threading.Thread(target=py.poll.gitcheck.git_check_loop)
    git_check_thread.start()

    # start LCD thread
    py.logs.log("main", "Starting LCD thread")
    lcd_thread = threading.Thread(target=py.poll.lcd.start_lcd)
    lcd_thread.start()

    # start LED thread
    py.logs.log("main", "Starting LED thread")
    led_thread = threading.Thread(target=py.poll.led.start_led)
    led_thread.start()

    # start webserver manager thread
    py.logs.log("main", "Starting Webserver thread")
    webserver_thread = threading.Thread(target=www.node.node_server.start_server)
    webserver_thread.start()

    # start location determination thread
    py.logs.log("main", "Starting output location thread")
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
            py.logs.log("main", "Starting accelerometer collection: " + accelerometer_destination)
            sensor_process = subprocess.Popen(["./src/c/collect.o", py.settings.get_duration(), py.settings.get_rate(), accelerometer_destination])
            sensor_process.wait()  # wait for sensor thread to end, restart it if it does
            py.logs.log("main", "Collection complete")
            py.logs.log("main", "Starting classification")
            classifier_destination = destination + "classifier.data"
            # RUN CLASSIFICATION FUNCTION HERE

            # move accelerometer data to storage
            shutil.move("data/accelerometer.data", "data/raw/accelerometer_" + datetime.datetime.now().strftime("%Y_%m_%d_%h_%H_%M") + ".data")
            py.logs.log("main", "Classification completed")

        if py.poll.gitcheck.check_flag_file() == "RESET":
            os._exit(1)
