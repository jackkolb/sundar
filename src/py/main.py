# main.py: starts the various threads (github check, lcd, webserver, etc) and then collects accelerometer data infinitely

import subprocess
import threading
import py.logs
import py.settings
import RPi.GPIO as GPIO
import os
import py.poll.ip
import py.poll.lcd
import py.poll.led
import py.poll.location
import py.poll.gitcheck
import www.node.node_server
import shutil
import datetime
import time

def main():
    GPIO.setmode(GPIO.BCM)  # sets the GPIO pins to BCM, used for the sensors etc to work

    # start git check thread: checks if there are code updates, if there are it sets a flag to restart the program
    py.logs.log("main", "Starting GitHub check thread")
    git_check_thread = threading.Thread(target=py.poll.gitcheck.git_check_loop)
    git_check_thread.start()

    # start LCD thread: displays wifi and collection information
    py.logs.log("main", "Starting LCD thread")
    lcd_thread = threading.Thread(target=py.poll.lcd.start_lcd)
    lcd_thread.start()
    
    # output IP address to console
    ip, name = py.poll.lcd.get_ip_address()
    py.logs.log("main", "WIFI Name: " + name)
    py.logs.log("main", "IP Address: " + ip)

    # start LED thread: an LED that shows the current damage and flashes on command (not currently implemented in hardware)
    py.logs.log("main", "Starting LED thread")
    led_thread = threading.Thread(target=py.poll.led.start_led)
    led_thread.start()

    # start webserver thread: a webserver to control the device remotely
    py.logs.log("main", "Starting Webserver thread")
    webserver_thread = threading.Thread(target=www.node.node_server.start_server)
    webserver_thread.start()

    # start location determination thread: determines where to write data (onboard or flashdrive, prioritize flashdrive)
    py.logs.log("main", "Starting output location thread")
    location_thread = threading.Thread(target=py.poll.location.manage_output_location)
    location_thread.start()

    # start IP track thread: uses https://kolb.dev/speck to update the IP address location
    py.logs.log("main", "Starting IP track thread")
    ip_thread = threading.Thread(target=py.poll.ip.start_speck)
    ip_thread.start()

    # set collection flag to false, collection flag used by the LCD display
    with open("flags/collection", "w") as collection_flag:
        collection_flag.write("false")

    # wait until connected to WiFi
    ip = None
    while ip == "FAIL" or ip == None:
        ip, name = py.poll.lcd.get_ip_address()

    py.logs.send_email("sundarlabucr@gmail.com", "Node Registration at " + ip, "Activation of node on network " + name + " at IP " + ip)
    py.logs.log("Sent activation email")

    capacity_filled = False  # bool for when the device is at max capacity

    # general loop: launches collection script, when it finishes relaunch it after a set delay
    while True:
        # first check if the node should be collecting ("active" flag set via the webserver)
        try:  
            with open("settings/active", "r") as collection_flag:
                status = collection_flag.readline()
        except:
            status == "false"

        # if the node should be collecting, collect!
        if status == "true":
            # check is storage used is 80%+
            if int(py.poll.lcd.get_disk_usage()[:-1]) > 70:
                print(py.poll.lcd.get_disk_usage())
                if not capacity_filled:
                    logs.send_email("sundarlabucr@gmail.com", "Node is at max capacity at " + ip, "The node on network " + name + " at IP " + ip + " is at max capacity.")
                    capacity_filled = True
                continue

            destination = py.poll.location.get_output_location()  # get the output location, default to the onboard "data/"
            if destination == "none":
                destination = "data/"
            accelerometer_destination = "./data/" + "accelerometer.data"  # creates the save path (ex: data/accelerometer.data)
            open(accelerometer_destination, 'w').close()  # creates the empty file
            py.logs.log("main", "Starting accelerometer collection: " + accelerometer_destination)
            # set collection flag to true
            with open("flags/collection", "w") as collection_flag:
                collection_flag.write("true")
            # the collect process is run and given the sampling duration, sampling rate, and output destination
            sensor_process = subprocess.Popen(["./src/c/collect.o", py.settings.get_duration(), py.settings.get_rate(), accelerometer_destination])  # starts the collection process
            sensor_process.wait()  # wait for collection to finish
            py.logs.log("main", "Collection complete")
            with open("flags/collection", "w") as collection_flag:
                collection_flag.write("false")
            py.logs.log("main", "Starting classification")
            classifier_destination = destination + "classifier.data"

            ### RUN CLASSIFICATION FUNCTION HERE ###

            # move accelerometer data to storage, formatted as accelerometer_year_month_day_hour_minute.data
            try:
                shutil.move("data/accelerometer.data", destination + "raw/accelerometer_" + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".data")
            except:
                py.logs.log("main", "Could not move accelerometer.data file")
                continue
            py.logs.log("main", "Classification completed")
            
            # delay the next collection by the set amount
            with open("settings/delay", "r") as delay_setting_file:
                sampling_delay = delay_setting_file.readline()
            time.sleep(sampling_delay)

        # check if the git flag indicated a reset
        if py.poll.gitcheck.check_flag_file() == "RESET":
            os._exit(1)
