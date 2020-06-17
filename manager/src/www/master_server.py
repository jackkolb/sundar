# master_server.py: the manager webserver, has routes for displaying the webpage,
# adding nodes to sync with, and retrieving node information

from flask import Flask, render_template, request, make_response, jsonify  # used for the webserver
import py.node_data  # used to store/read node data
import py.networks  # used to get speck information
import py.logs  # used for logs

app = Flask(__name__)

# index route: displays the central HTML page interface
@app.route("/")
def index():
    return render_template("index.html", data=py.node_data.node_data)
    

# register route: used by nodes confirming with the master
@app.route("/register", methods=["GET"])
def register_get():
    node_information = request.args  # extract the node information from the GET request
    py.node_data.node_data[node_information["serial"]] = node_information
    return make_response(jsonify({"result": "success"}))


# add-node route: used by the website interface to add a node
@app.route("/add-node", methods=["GET"])
def add_ip_get():
    ip = request.args.get("ip")  # extract the "ip" field from the GET request
    node_info = py.networks.get_node_information(ip)  # get the node information by pinging the given IP
    if node_info != {}:  # if the node responded with information, add it to the registry
        py.node_data.node_data[node_info["serial"]] = node_info
        py.logs.log("server", "Added node at ip " + ip)
        return make_response(jsonify({"result": "success"}))
    else:  # otherwise, failed to connect to or add the node
        py.logs.log("server", "Failed to add node at ip " + ip)
        return make_response(jsonify({"result": "failure"}))


# remove-serial route: used by the website to remove a node tracker
@app.route("/remove-serial", methods=["GET"])
def remove_ip_get():
    serial = request.args.get("serial")  # extract the "serial" field from the GET request
    py.node_data.node_data.pop(serial, None)  # remove that node from the nodes
    return make_response(jsonify({"result": "success"}))


# nodes route: used by the website to get all the node data
@app.route("/nodes", methods=["GET"])
def node_info_get():
    # takes the nodes data, turns it into a JSON format, and sends it as a response
    response = make_response(jsonify(py.node_data.node_data))  
    return response


# set-sync route: used by the website to set the sync timer period
@app.route("/set-sync", methods=["GET"])
def node_set_sync_get():
    timer = int(request.args.get("timer"))  # extract the "timer" field from the GET request as a INTEGER
    py.node_data.sync_timer = timer if timer >= 0 else 5  # if a valid time is given, use it, otherwise default to 5
    return make_response(jsonify({"result": "success"}))


# get-sync route: used by the website to get the sync timer period
@app.route("/get-sync", methods=["GET"])
def node_get_sync_get():
    return str(py.node_data.sync_timer)  # responds with the sync timer period


# start_server: starts the Flask app (0.0.0.0 indicates being able to use it with its public facing IP address instead of localhost only)
def start_server():
    app.run(host="0.0.0.0", port=80)


# when the script starts, start the webserver
if __name__ == "__main__":
    start_server()
