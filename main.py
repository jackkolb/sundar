import threading
import gitcheck

def main():
    print("Woo!")
    # launch git check thread -- checks if there are code updates, if there are it kills the program
    git_check_thread = threading.Thread(target=gitcheck.git_check_loop)
    git_check_thread.start()
    print("started")
    return