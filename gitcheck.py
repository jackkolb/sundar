import subprocess


# checks for new code every 10 minutes, if there is an update, pull it and restart processes
def git_check_loop():
    while True:
        result = subprocess.Popen("echo hello", shell=True, stdout=subprocess.PIPE).stdout.read()
        print(result)


git_check_loop()