import multiprocessing
import threading
import src.gitcheck
import src.wifi_check
import src.sensors
import src.logs
import src.settings as sensor_settings
import RPi.GPIO as GPIO


def main():
    src.logs.log("[MAIN] Starting GitHub check thread")
    # launch git check thread -- checks if there are code updates, if there are it kills the program
    git_check_thread = threading.Thread(target=src.gitcheck.git_check_loop)
    git_check_thread.start()

    wifi_check_thread = threading.Thread(target=src.wifi_check.wifi_check_loop)
    wifi_check_thread.start()

    src.logs.log("[MAIN] Loading settings")
    settings = sensor_settings.retrieve_settings()

    # general loop: polls sensors, stores to logs, uploads at midnight
    while True:
        src.logs.log("[MAIN] Starting sensor process")
        sensor_process = multiprocessing.Process(target=src.sensors.sensor_manager, args=(settings,))
        sensor_process.start()

        sensor_process.join()  # wait for sensor thread to end, restart it if it does
        src.logs.log("[MAIN] Sensor thread stopped, restarting")
