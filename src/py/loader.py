import threading, importlib
import main, logs

if __name__ == "__main__":
        
    while True:
        importlib.reload(main)
        importlib.reload(logs)
        import main
        import logs
        main_thread = threading.Thread(target=main.main)
        logs.log("[LOADER] Starting Main Thread")
        main_thread.start()
        main_thread.join()
        logs.log("[LOADER] Main Thread Ended")
