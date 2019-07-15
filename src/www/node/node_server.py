from flask import Flask, render_template, request, jsonify
import www.node.information
import logging

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route("/")
def index():
    return render_template("index.html", data=www.node.information.load_information())

# used when applications ping whether the server is active and retrieve settings
@app.route("/settings", methods=["GET"])
def settings_get():
    return jsonify(www.node.information.load_settings())

# used when applications retrieve the current server data
@app.route("/data", methods=["GET"])
def data_get():
    return jsonify(eval(www.node.information.load_data()))

@app.route("/logs", methods=["GET"])
def logs_get():
    return www.node.information.load_logs()

@app.route("/reset", methods=["GET"])
def reset_get():
    www.node.information.reset_logs()
    www.node.information.reset_data()
    

# used when applications set the data
@app.route("/update", methods=["GET"])
def data_set():
    valid_keys = ["active", "duration", "rate", "name", "flashLED", "flashdrive", "reset"]
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

def start_server():
    app.run(host="0.0.0.0")
