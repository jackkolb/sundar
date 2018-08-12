import subprocess
import time
import sys
import src.logs


# checks for new code every 10 minutes, if there is an update, pull it and restart processes
def git_check_loop():
    while True:
        result = str(subprocess.Popen("git pull", shell=True, stdout=subprocess.PIPE).stdout.read())
        result = result[2:-3]

        if result == "Already up to date.":  # latest remote commit matches current
            pass

        else:  # new code on GitHub
            src.logs.log("[Git Check] New build found on GitHub, resetting")
            sys.exit()  # exits the program (including the thread)

        time.sleep(60 * 10)  # waits 10 minutes
