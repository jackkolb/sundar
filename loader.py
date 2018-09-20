import threading



if __name__ == "__main__":
    main_thread = threading.Thread(target=src.main.main)

    while True:
    	import src.main
    	import src.logs

        src.logs.log("[LOADER] Starting Main Thread")
        main_thread.start()
        main_thread.join()
        src.logs.log("[LOADER] Main Thread Ended")
