import threading
import gitcheck
import time
import datetime

def main():
    print("Woo!")
    # launch git check thread -- checks if there are code updates, if there are it kills the program
    git_check_thread = threading.Thread(target=gitcheck.git_check_loop)
    git_check_thread.start()
    print("started")

    # general loop: polls sensors, stores to logs, uploads at midnight
    while True:
        current_time = datetime.datetime.now()


        time.sleep(5)



    return
