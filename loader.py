import threading
import subprocess

if __name__ == "__main__":
    main_thread = threading.Thread(target=src.main.main)

    while True:
        src.logs.log("[LOADER] Starting Main Thread")
        subprocess.check_call(["python3", "./src/main.py"], shell=True)
        src.logs.log("[LOADER] Main Thread Ended")
