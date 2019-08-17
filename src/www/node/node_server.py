# node_server.py: runs a Flask server to handle interfacing with the node

from flask import Flask, render_template, request, jsonify, send_file
import www.node.information
import logging
import os

app = Flask(__name__)  # the overall Flask app

# sets logging to only show errors (not logging each individual request)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# the index route, returns the base html page with the server information
@app.route("/")
def index():
    return render_template("index.html", data=www.node.information.load_information())

# retrieves server settings
@app.route("/settings", methods=["GET"])
def settings_get():
    return jsonify(www.node.information.load_settings())
"""
# retrieves the current server history
@app.route("/history", methods=["GET"])
def history_get():
    return send_file("../../../data/classifier.data")

# retrieves the current server accelerometer data
@app.route("/data", methods=["GET"])
def data_get():
    files = os.listdir("data/raw")
    files.sort()
    return send_file("../../../data/raw/" + files[-1])

# retrieves the current server logs
@app.route("/logs", methods=["GET"])
def logs_get():
    #files = os.listdir("logs")
    #files.sort()
    #print(files[-1])
    print("!!!!!")
    return #send_file("../../../logs/" + files[-1])
"""
# resets the server logs and classifier history
@app.route("/reset", methods=["GET"])
def reset_get():
    www.node.information.reset_logs()
    www.node.information.reset_data()
    
# updates a system setting, used by the buttons displayed on the webpage. This handles one setting change per request.
@app.route("/update", methods=["GET"])
def data_set():
    valid_keys = ["active", "duration", "rate", "name", "flashLED", "flashdrive", "reset"]  # prevents changing settings beyond the valid keys
    key = request.args.get("key")
    value = request.args.get("value")
    if key not in valid_keys:
        return "bad"
    # process update
    if key == "active" and value in ["true", "false"]:
        www.node.information.updateSettings("active", value)
    elif key == "flashdrive" and value in ["true", "false"]:
        www.node.information.updateSettings("flashdrive", value)
    elif key == "duration" and value.isdigit():
        www.node.information.updateSettings("duration", value)
    elif key == "rate" and value.isdigit():
        www.node.information.updateSettings("rate", value)
    elif key == "name":
        www.node.information.updateSettings("name", value)
    elif key == "reset" and value == "true":
        www.node.information.reset_data()
        www.node.information.reset_logs()
    elif key == "flashLED" and value == "true":
        www.node.information.flash_LED()

    return "good"

# starts the Flask app (0.0.0.0 indicates being able to use it with its visible IP address instead of localhost only)
def start_server():
    app.run(debug=True, host="0.0.0.0")
