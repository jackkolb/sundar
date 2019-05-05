import subprocess
import threading
import gitcheck
import wifi_check
import logs
import settings as sensor_settings
import RPi.GPIO as GPIO
import sys

def main():
    logs.log("[MAIN] Starting GitHub check thread")
    # launch git check thread -- checks if there are code updates, if there are it kills the program
    git_check_thread = threading.Thread(target=gitcheck.git_check_loop)
    git_check_thread.start()

    wifi_check_thread = threading.Thread(target=wifi_check.wifi_check_loop)
    wifi_check_thread.start()

    logs.log("[MAIN] Loading settings")
    settings = sensor_settings.retrieve_settings()

    # general loop: launch collection script, when it dies relaunch it
    while True:
        logs.log("[MAIN] Starting sensor process")
        sensor_process = subprocess.Popen(["./src/c/collect.o", "data/dataaa.txtt"])
        sensor_process.wait()  # wait for sensor thread to end, restart it if it does
        logs.log("[MAIN] Sensor process stopped, restarting")
        if gitcheck.check_flag_file() == "RESET"
            sys.exit()
