import threading
import src.main
import src.logs


if __name__ == "__main__":
    
    while True:
        reload(src.main)
        reload(src.logs)
        import src.main
        import src.logs
        main_thread = threading.Thread(target=src.main.main)
        src.logs.log("[LOADER] Starting Main Thread")
        main_thread.start()
        main_thread.join()
        src.logs.log("[LOADER] Main Thread Ended")
