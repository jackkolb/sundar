import subprocess
import threading
import gitcheck
import wifi_check
import logs
import settings as sensor_settings
import RPi.GPIO as GPIO
import os
import signals.lcd

def main():
    GPIO.setmode(GPIO.BCM)
    logs.log("[MAIN] Starting GitHub check thread")
    # launch git check thread -- checks if there are code updates, if there are it kills the program
    git_check_thread = threading.Thread(target=gitcheck.git_check_loop)
    git_check_thread.start()

    wifi_check_thread = threading.Thread(target=wifi_check.wifi_check_loop)
    wifi_check_thread.start()

    logs.log("[MAIN] Loading settings")
    settings = sensor_settings.retrieve_settings()

    logs.log("[MAIN] Starting LCD")
    signals.lcd.start_lcd()

    # general loop: launch collection script, when it dies relaunch it
    while True:
        logs.log("[MAIN] Starting sensor process")
        sensor_process = subprocess.Popen(["./src/c/collect.o", "data/data.txt"])
        sensor_process.wait()  # wait for sensor thread to end, restart it if it does
        logs.log("[MAIN] Sensor process stopped, restarting")
        if gitcheck.check_flag_file() == "RESET":
            os._exit(1)
