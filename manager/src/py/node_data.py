# node_data.py: stores the node network data and has functions for reading, writing,
# and syncing to this data
import time  # used for the autosave loop delay
import json  # used to convert python dictionaries into JSON format
import py.logs  # used for logging

node_data = {}  # python dictionary for all the node data
sync_timer = 5  # the default sync delay timer


# read_node_data: reads the nodes.data file and the sync_delay file and replaces their corresponding variables
def read_node_data():
    # node_data and sync_timer are global variables 
    global node_data
    global sync_timer
    node_data = json.loads(open('data/nodes/nodes.data').read().replace("'", '"'))
    sync_timer = int(open('data/settings/sync_delay').read())
    return


# sync_data: takes in a node data network and syncs with (not replaces) the established node data network
def sync_data(new_node_data):
    global node_data
    for key in new_node_data.keys():
        node_data[key] = new_node_data[key]
    return


# autosave_loop: periodically writes the global node_data variable and the sync timer to files
def autosave_loop():
    global node_data
    while True:
        with open("data/nodes/nodes.data", "w") as f:
            f.write(str(node_data))
        with open("data/nodes/sync_timer", "w") as f:
            f.write(str(sync_timer))
        py.logs.log("autosave", "Saved node data and sync timer")
        time.sleep(60)