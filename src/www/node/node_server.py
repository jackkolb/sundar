from flask import Flask, render_template, request, jsonify
import www.node.information

app = Flask(__name__)

def get_key(key):
    with open("data/key", "r") as key_file:
        return key_file.read()

def updateSettings(file, value):
    with open("settings/" + file, "w") as data_file:
        data_file.write(value)

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
        updateSettings("active", value)
    elif key == "flashdrive" and value in ["true", "false"]:
        updateSettings("flashdrive", value)
    elif key == "duration" and value.isdigit():
        updateSettings("duration", value)
    elif key == "rate" and value.isdigit():
        updateSettings("rate", value)
    elif key == "name":
        updateSettings("name", value)
    elif key == "reset" and value == "true":
        www.node.information.reset_data()
        www.node.information.reset_logs()
    elif key == "flashLED" and value == "true":
        www.node.information.flash_LED()

    return "good"

def main():
    app.run(host="0.0.0.0")
