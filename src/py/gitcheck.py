import subprocess
import time
import sys
import src.logs


def check_flag_file():
    data = "ERROR"
    with open("data/sys/git_flag", "r") as git_flag_file:
        data = git_flag_file.readline()
    
    if data == "ERROR":
        src.logs.log("[Git Check] Could not open file: data/sys/git_flag")
    if data == "RESET":
        with open("data/sys/git_flag", "w") as git_flag_file:
            git_flag_file.write("GOOD")
    return data
    
# checks for new code every 10 minutes, if there is an update, pull it and restart processes
def git_check_loop():
    while True:
        git_process = subprocess.Popen(["git","pull"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = git_process.communicate()
        result = str(out)
        result = result[2:-3]

        if result == "Already up-to-date.":  # latest remote commit matches current
            pass

        else:  # new code on GitHub
            print(result)
            src.logs.log("[Git Check] New build found on GitHub, changing flag")
            with open("data/sys/git_flag", "w") as git_flag_file:  # exits the program (including the thread)
                git_flag_file.write("RESET")
        time.sleep(30)  # waits 10 minutes