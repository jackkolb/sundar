# main.py: manager script, controls the various scripts of the manager system
import py.node_data  # used to read/write to the node data storage object
import py.gitcheck  # used to periodically connect to GitHub to sync the codebase
import py.logs  # used for logging
import py.networks  # used to connect to nodes for syncing, and connect to Specks to get nodes' IP addresses
import py.settings  # used to read/write settings
import www.master_server  # used to run the master server
import threading  # used to run multiple scripts simultaneously
import time  # used for time delays

# main: starts the module threads and syncs nodes periodically
def main():
    # start git check thread: checks if there are code updates, if there are it sets a flag to restart the program
    py.logs.log("main", "Starting GitHub check thread")
    git_check_thread = threading.Thread(target=py.gitcheck.git_check_loop)
    git_check_thread.start()

    # read the node data file
    py.node_data.read_node_data()

    # start node data autosave thread
    py.logs.log("main", "Starting node data autosave loop")
    autosave_thread = threading.Thread(target=py.node_data.autosave_loop)
    autosave_thread.start()

    # start webserver thread: a webserver to control the device remotely
    py.logs.log("main", "Starting Webserver thread")
    webserver_thread = threading.Thread(target=www.master_server.start_server)
    webserver_thread.start()

    # pause until connected to WiFi
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
        py.logs.log("main", "Scanning node network")
        
        # for each scanned ip, get its node information
        scanned_nodes = {}
        try:
            # for each node, use the known IP address to get the data and check the serial numbers
            # if the scan doesn't work, check Speck and update the node
            for node in py.node_data.node_data.keys():
                ip = py.node_data.node_data[node]["ip"]
                scanned_node_data = py.networks.get_node_information(ip)
                if scanned_node_data != {}:
                    scanned_nodes[scanned_node_data["serial"]] = scanned_node_data
                    scanned_nodes[scanned_node_data["serial"]]["last_contact"] = str(int(time.time()))
                elif "speck" in py.node_data.node_data[node].keys():
                    speck = py.node_data.node_data[node]["speck"].split(" ")
                    ip = py.networks.get_speck(speck[0], speck[1])
                    if ip != "FAIL":
                        py.node_data.node_data[node]["ip"] = ip
                        py.logs.log("main", "Updated ip for node " + node)
                else:
                    py.logs.log("main", "Failed to contact node at ip " + ip)
        except:  # if something fails, it is likely because a node tracker was deleted while this scan was taking place
            py.logs.log("main", "Dictionary probably changed during iteration, likely because a node tracker was deleted")

        # write the scanned node json data to the file
        py.node_data.sync_data(scanned_nodes)
        py.logs.log("main", "Updated node data with " + str(len(scanned_nodes.keys())) + " nodes")

        # delay for the set sync timer period
        time.sleep(py.node_data.sync_timer)
        

# start the main script
if __name__ == "__main__":
    main()
