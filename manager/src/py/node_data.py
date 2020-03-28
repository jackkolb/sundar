import time
import json
import py.logs

node_data = {}
sync_timer = 5

def read_node_data():
    global node_data
    global sync_timer
    node_data = json.loads(open('data/nodes/nodes.data').read().replace("'", '"'))
    sync_timer = int(open('data/settings/sync_delay').read())
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
        with open("data/nodes/sync_timer", "w") as f:
            f.write(str(sync_timer))
        py.logs.log("autosave", "Saved node data and sync timer")
        time.sleep(60)