from flask import Flask, render_template, request, jsonify
import information

app = Flask(__name__)

def get_key(key):
    with open("data/key", "r") as key_file:
        return key_file.read()

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
    return jsonify(information.load_data())

# used when applications set the data
@app.route("/data", methods=["POST"])
def data_set():
    information.set_data(request.form["data"])
    return "good"


app.run(host="0.0.0.0")
