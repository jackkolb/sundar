import time
import json

node_data = {}

def read_node_data():
    global node_data
    node_data = json.loads(open('data/nodes/nodes.data').read().replace("'", '"'))
    return


def sync_data(new_node_data):
    global node_data
    for key in new_node_data.keys():
        node_data[key] = new_node_data[key]
    return


def autosave_loop():
    global node_data
    while True:
        with open("data/nodes/nodes.data", "w") as f:
            f.write(str(node_data))
        time.sleep(60)