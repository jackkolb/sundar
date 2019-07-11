from flask import Flask, render_template, request

app = Flask(__name__)

data = {}

def load_nodes():
    global data
    with open("nodes.data", "r") as nodes_data:
        data = nodes_data.read()
    return data

def write_nodes():
    global data
    with open("nodes.data", "w") as nodes_data:
        nodes_data.write(data)

@app.route("/")
def index():
    return render_template("index.html", data=load_nodes())

@app.route("/update", methods=["GET"])
def update_get():
    return "This method is only accessible via POST"

@app.route("/update", methods=["POST"])
def update_post():
    global data
    result = "invalid"
    print("!")
    node_name = request.form["node-name"]
    node_key = request.form["node-key"]
    node_settings = request.form["node-settings"]
    node_life = request.form["node-life"]
    node_data = request.form["node-data"]
    print(node_name + "\n" + node_key + "\n" + node_settings + "\n" + node_data)
    

    if node_key == data[node_name]["node-key"]:
        data[node_name]["settings"] = node_settings
        data[node_name]["life"] = node_life
        data[node_name]["data"] = node_data
        result = "valid"
        write_nodes()
    
    return "Node Updated"

load_nodes()
app.run()
