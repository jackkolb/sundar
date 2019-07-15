import multiprocessing, importlib
import py.main, py.logs

if __name__ == "__main__":
        
    while True:
        importlib.reload(py.main)
        importlib.reload(py.logs)
        import py.main
        import py.logs

        main_thread = multiprocessing.Process(target=py.main.main)
        py.logs.log("loader", "Starting Main Process")
        main_thread.start()
        main_thread.join()
        py.logs.log("loader", "Main Process Ended")
