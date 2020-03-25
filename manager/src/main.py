# Manager script, manages everything
import py.node_data
import py.gitcheck
import py.logs
import py.networks
import py.settings
import www.master_server
import json
import threading
import time


def main():
    # start git check thread: checks if there are code updates, if there are it sets a flag to restart the program
    py.logs.log("main", "Starting GitHub check thread")
    git_check_thread = threading.Thread(target=py.gitcheck.git_check_loop)
    git_check_thread.start()

    # read the node data file
    py.node_data.read_node_data()

    # start node data autosave thread
    autosave_thread = threading.Thread(target=py.node_data.autosave_loop)
    autosave_thread.start()

    # start webserver thread: a webserver to control the device remotely
    py.logs.log("main", "Starting Webserver thread")
    webserver_thread = threading.Thread(target=www.master_server.start_server)
    webserver_thread.start()

    

    # wait until connected to WiFi
    ip = None
    while ip == None:
        ip, name = py.networks.get_ip_address()
    
    # output IP address to logs
    ip, name = py.networks.get_ip_address()
    py.logs.log("main", "WIFI Name: " + name)
    py.logs.log("main", "IP Address: " + ip)

    # send email to manager email
    serial = py.settings.get_serial()
    py.logs.send_email("sundarlabucr@gmail.com", "Manager Registration for S\\N " + serial, "Activation of manager on network " + name + " at IP " + ip)
    py.logs.log("main", "Sent activation email")

    # general loop, scans for nodes and updates register
    while True:
        py.logs.log("main", "Scanning network")
        
        # for each scanned ip, get its node information
        scanned_nodes = {}
        for node in py.node_data.node_data.keys():
            ip = py.node_data.node_data[node]["ip"]
            scanned_node_data = py.networks.get_node_information(ip)
            if scanned_node_data != {}:
                scanned_nodes[scanned_node_data["serial"]] = scanned_node_data
                scanned_nodes[scanned_node_data["serial"]]["last_contact"] = str(int(time.time()))

        # write the current json to the file
        py.node_data.sync_data(scanned_nodes)

        py.logs.log("main", "Updated node data with " + str(len(scanned_nodes.keys())) + " nodes")
        time.sleep(5)
        

if __name__ == "__main__":
    main()
