from flask import Flask, render_template, request, jsonify
import information

app = Flask(__name__)

def get_key(key):
    with open("data/key", "r") as key_file:
        return key_file.read()

def updateData(file, value):
    with open("data/" + file, "w") as data_file:
        data_file.write(value)

@app.route("/")
def index():
    return render_template("index.html", data=information.load_information())

# used when applications ping whether the server is active
@app.route("/settings", methods=["GET"])
def settings_get():
    return jsonify(information.load_settings())

# used when applications retrieve the current server data
@app.route("/data", methods=["GET"])
def data_get():
    return jsonify(eval(information.load_data()))

@app.route("/logs", methods=["GET"])
def logs_get():
    return information.load_logs()

@app.route("/reset", methods=["GET"])
def reset_get():
    information.reset_logs()
    information.reset_data()
    

# used when applications set the data
@app.route("/update", methods=["GET"])
def data_set():
    valid_keys = ["active", "duration", "rate", "name", "flash", "flashdrive", "reset"]
    key = request.args.get("key")
    value = request.args.get("value")
    if key not in valid_keys:
        return "bad"
    # process update
    if key == "active" and value in ["true", "false"]:
        updateData("active", value)
    if key == "flashdrive" and value in ["true", "false"]:
        updateData("flashdrive", value)
        print(updated flash)
    elif key == "duration" and value.isdigit():
        updateData("duration", value)
    elif key == "rate" and value.isdigit():
        updateData("rate", value)
    elif key == "name":
        updateData("name", value)
    elif key == "reset" and value == "true":
        information.reset_data()
        information.reset_logs()
    elif key == "flashLED" and value == "true":
        information.flash_LED()


    return "good"


app.run(host="0.0.0.0")
