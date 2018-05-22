import threading
import main
import logs


if __name__ == "__main__":
    main_thread = threading.Thread(target=main.main)

    while True:
        logs.log("[LOADER] Starting Main Thread")
        main_thread.start()
        logs.log("[LOADER]   success!")
        main_thread.join()
