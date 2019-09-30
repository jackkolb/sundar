# node_server.py: runs a Flask server to handle interfacing with the node

from flask import Flask, render_template, request, jsonify, send_file, make_response
import www.node.information
import logging
import os
import py.logs

app = Flask(__name__)  # the overall Flask app

# sets logging to only show errors (not logging each individual request)
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

# the index route, returns the base html page with the server information
@app.route("/")
def index():
    return render_template("index.html", data=www.node.information.load_information())

# download logs
@app.route("/download-log", methods=["GET"])
def download_log_get():
    log_file_names = www.node.information.load_all_logs()
    log_file_index = int(request.args.get("id"))
    response = make_response(send_file("../../../logs/" + log_file_names[log_file_index], as_attachment=True, attachment_filename=log_file_names[log_file_index]))
    response.headers["Cache-Control"] = ["no-cache", "must-revalidate"]
    response.headers["Expires"] = "Sat, 26 Jul 1997 05:00:00 GMT"
    return response

# the logs route, returns items to download from logs
@app.route("/logs")
def logs_get():
    return render_template("logs.html", logs=www.node.information.load_all_logs())

# retrieves the last server logs
@app.route("/last-log", methods=["GET"])
def lastlog_get():
    files = os.listdir("logs")
    files.sort()
    response = make_response(send_file("../../../logs/" + files[-1]))
    response.headers["Cache-Control"] = ["no-cache", "must-revalidate"]
    response.headers["Expires"] = "Sat, 26 Jul 1997 05:00:00 GMT"
    return response

# download logs
@app.route("/download-data", methods=["GET"])
def download_data_get():
    data_file_names = www.node.information.load_all_data()
    data_file_index = int(request.args.get("id"))
    response = make_response(send_file("../../../data/" + data_file_names[data_file_index], as_attachment=True, attachment_filename=data_file_names[data_file_index]))
    response.headers["Cache-Control"] = ["no-cache", "must-revalidate"]
    response.headers["Expires"] = "Sat, 26 Jul 1997 05:00:00 GMT"
    return response

# the logs route, returns items to download from logs
@app.route("/data")
def data_get():
    return render_template("data.html", data=www.node.information.load_all_data())

# retrieves the last server accelerometer data
@app.route("/last-data", methods=["GET"])
def lastdata_get():
    files = os.listdir("data/raw")
    files.sort()
    response = make_response(send_file("../../../data/raw/" + files[-1]))
    response.headers["Cache-Control"] = ["no-cache", "must-revalidate"]
    response.headers["Expires"] = "Sat, 26 Jul 1997 05:00:00 GMT"
    return response

# retrieves server settings
@app.route("/settings", methods=["GET"])
def settings_get():
    response = make_response(jsonify(www.node.information.load_settings()))
    return response

# retrieves the current server history
@app.route("/history", methods=["GET"])
def history_get():
    response = make_response(send_file("../../../data/classifier.data"))
    response.headers["Cache-Control"] = ["no-cache", "must-revalidate"]
    response.headers["Expires"] = "Sat, 26 Jul 1997 05:00:00 GMT"
    return response

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
    app.run(host="0.0.0.0", port=80)
