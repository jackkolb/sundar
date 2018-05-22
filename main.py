import multiprocessing
import threading
import gitcheck
import sensors
import logs
import settings as sensor_settings


def main():
    logs.log("[MAIN] Starting GitHub check thread")
    # launch git check thread -- checks if there are code updates, if there are it kills the program
    git_check_thread = threading.Thread(target=gitcheck.git_check_loop)
    git_check_thread.start()

    logs.log("[MAIN] Loading settings")
    settings = sensor_settings.retrieve_settings()

    # general loop: polls sensors, stores to logs, uploads at midnight
    while True:
        logs.log("[MAIN] Starting sensor process")
        sensor_process = multiprocessing.Process(target=sensors.sensor_manager, args=(settings,))
        sensor_process.start()

        sensor_process.join()  # wait for sensor thread to end, restart it if it does
        logs.log("[MAIN] Sensor thread stopped, restarting")
