import multiprocessing, importlib
import py.main, py.logs

if __name__ == "__main__":
        
    while True:
        importlib.reload(py.main)
        importlib.reload(py.logs)
        import py.main
        import py.logs
        import www.node.node_server

        webserver_thread = multiprocessing.Process(target=www.node.node_server.main)
        webserver_thread.start()

        main_thread = multiprocessing.Process(target=py.main.main)
        py.logs.log("[LOADER] Starting Main Process")
        main_thread.start()
        main_thread.join()
        webserver_thread.terminate()
        py.logs.log("[LOADER] Main Process Ended")
