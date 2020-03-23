# loader.py: a small script that manages the system: it simply keeps the main process running. It is expected that this file will never be changed.

import multiprocessing, importlib
import py.main, py.logs

if __name__ == "__main__":
    # infinite loop to keep the main process alive
    while True:
        # reloads the main.py and logs.py script (in case they were changed)
        importlib.reload(py.main)
        importlib.reload(py.logs)
        
        main_thread = multiprocessing.Process(target=py.main.main)
        py.logs.log("loader", "Starting Main Process")
        main_thread.start()  # starts the main process
        main_thread.join()  # waits for the main process to end
        py.logs.log("loader", "Main Process Ended")
