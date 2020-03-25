from flask import Flask, render_template, request
import py.node_data


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", data=py.node_data.node_data)
    

# for nodes confirming with the master
@app.route("/register", methods=["GET"])
def register_get():
    node_information = request.args
    py.node_data.node_data[node_information["serial"]] = node_information
    return "success"


@app.route("/add-ip", methods=["GET"])
def add_ip_get():
    ip = request.args.get("ip")
    serial = request.args.get("serial")
    py.node_data.node_data[serial] = {"ip": ip}
    return "success"


# starts the Flask app (0.0.0.0 indicates being able to use it with its visible IP address instead of localhost only)
def start_server():
    app.run(host="0.0.0.0", port=80)

if __name__ == "__main__":
    start_server()
