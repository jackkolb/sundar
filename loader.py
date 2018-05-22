import threading
import src.main
import src.logs


if __name__ == "__main__":
    main_thread = threading.Thread(target=src.main.main)

    while True:
        src.logs.log("[LOADER] Starting Main Thread")
        main_thread.start()
        main_thread.join()
