import multiprocessing, importlib
import main, logs

if __name__ == "__main__":
        
    while True:
        importlib.reload(main)
        importlib.reload(logs)
        import main
        import logs
        main_thread = multiprocessing.Process(target=main.main)
        logs.log("[LOADER] Starting Main Process")
        main_thread.start()
        main_thread.join()
        logs.log("[LOADER] Main Process Ended")
