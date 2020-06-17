# gitcheck.py: contains functions for syncing the codebase with GitHub

import subprocess  # used to run git commands
import time  # used to set a time delay
import py.logs  # used for logging

# check_flag_file: checks the git flag, returns its contents. If the flag is "RESET", writes it to "GOOD"
def check_flag_file():
    data = "ERROR"
    with open("flags/git_flag", "r") as git_flag_file:
        data = git_flag_file.readline()
    
    if data == "ERROR":
        py.logs.log("[Git Check] Could not open file: flags/git_flag")
    return data


# set_gitcheck_flag_good: set the git check flag to GOOD
def set_gitcheck_flag_good():
    with open("flags/git_flag", "w") as git_flag_file:
        git_flag_file.write("GOOD")
    return

    
# git_check_loop: checks for new code every 10 minutes, if there is an update, pull it and restart processes
def git_check_loop():
    while True:
        git_process = subprocess.Popen(["git","pull"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = git_process.communicate()
        result = str(out)
        result = result[2:-3]

        if "Updating" in result:  # new code on GitHub
            py.logs.log("Git", "New build found on GitHub, resetting at next cycle")
            with open("flags/git_flag", "w") as git_flag_file:  # exits the program (including the thread)
                git_flag_file.write("RESET")
        time.sleep(10)  # waits 10 seconds
    return
