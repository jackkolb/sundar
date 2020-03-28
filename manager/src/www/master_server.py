from flask import Flask, render_template, request, make_response, jsonify
import py.node_data
import py.networks


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", data=py.node_data.node_data)
    

# for nodes confirming with the master
@app.route("/register", methods=["GET"])
def register_get():
    node_information = request.args
    py.node_data.node_data[node_information["serial"]] = node_information
    return make_response(jsonify({"result": "success"}))


# for adding a node tracker from the website
@app.route("/add-node", methods=["GET"])
def add_ip_get():
    ip = request.args.get("ip")
    node_info = py.networks.get_node_information(ip)
    if node_info != {}:
        py.node_data.node_data[node_info["serial"]] = node_info
        return make_response(jsonify({"result": "success"}))
    else:
        return make_response(jsonify({"result": "failure"}))


# for removing a node tracker using the website
@app.route("/remove-serial", methods=["GET"])
def remove_ip_get():
    serial = request.args.get("serial")
    py.node_data.node_data.pop(serial, None)
    return make_response(jsonify({"result": "success"}))


# get all the node data, used by the website
@app.route("/nodes", methods=["GET"])
def node_info_get():
    response = make_response(jsonify(py.node_data.node_data))
    return response


@app.route("/set-sync", methods=["GET"])
def node_set_sync_get():
    timer = int(request.args.get("timer"))
    py.node_data.sync_timer = timer if timer >= 0 else 5
    return make_response(jsonify({"result": "success"}))


@app.route("/get-sync", methods=["GET"])
def node_get_sync_get():
    return str(py.node_data.sync_timer)


# starts the Flask app (0.0.0.0 indicates being able to use it with its visible IP address instead of localhost only)
def start_server():
    app.run(host="0.0.0.0", port=80)

if __name__ == "__main__":
    start_server()
