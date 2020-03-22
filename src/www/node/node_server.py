# node_server.py: runs a Flask server to handle interfacing with the node

from flask import Flask, render_template, request, jsonify, send_file, make_response
import www.node.information as info
import logging
import os
import py.logs
import zipfile
import shutil

app = Flask(__name__)  # the overall Flask app

# sets logging to only show errors (not logging each individual request)
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

# the index route, returns the base html page with the server information
@app.route("/")
def index():
    return render_template("index.html", data=info.load_information())

# download logs
@app.route("/download-log", methods=["GET"])
def download_log_get():
    log_file_names = info.load_all_logs()
    log_file_index = int(request.args.get("id"))
    response = make_response(send_file("../../../logs/" + log_file_names[log_file_index], as_attachment=True, attachment_filename=log_file_names[log_file_index]))
    response.headers["Cache-Control"] = ["no-cache", "must-revalidate"]
    response.headers["Expires"] = "Sat, 26 Jul 1997 05:00:00 GMT"
    return response

# the logs route, returns items to download from logs
@app.route("/logs")
def logs_get():
    return render_template("logs.html", logs=info.load_all_logs())

# retrieves the last server logs
@app.route("/last-log", methods=["GET"])
def lastlog_get():
    files = os.listdir("logs")
    files.sort()
    response = make_response(send_file("../../../logs/" + files[-1]))
    response.headers["Cache-Control"] = ["no-cache", "must-revalidate"]
    response.headers["Expires"] = "Sat, 26 Jul 1997 05:00:00 GMT"
    return response

# download a raw data file
@app.route("/download-raw-data", methods=["GET"])
def download_raw_data_get():
    data_file_names = info.get_raw_data_filenames()
    data_file_index = int(request.args.get("id"))
    response = make_response(send_file("../../../data/raw/" + data_file_names[data_file_index], as_attachment=True, attachment_filename=data_file_names[data_file_index]))
    response.headers["Cache-Control"] = ["no-cache", "must-revalidate"]
    response.headers["Expires"] = "Sat, 26 Jul 1997 05:00:00 GMT"
    return response

# download logs
@app.route("/download-daily-data", methods=["GET"])
def download_daily_data_get():
    data_file_names = info.get_daily_data_filenames()
    data_file_index = int(request.args.get("id"))
    response = make_response(send_file("../../../data/daily/" + data_file_names[data_file_index], as_attachment=True, attachment_filename=data_file_names[data_file_index]))
    response.headers["Cache-Control"] = ["no-cache", "must-revalidate"]
    response.headers["Expires"] = "Sat, 26 Jul 1997 05:00:00 GMT"
    return response

# download all data
@app.route("/download-all-data", methods=["GET"])
def download_all_data_get():
    # use the built-in zipfile to zip the data folder
    zipf = zipfile.ZipFile('sundarlab_data.zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk("./data/"):
        for file in files:
            zipf.write(os.path.join(root, file))
    zipf.close()

    response = make_response(send_file("sundarlab_data.zip", as_attachment=True, attachment_filename=data_file_names[data_file_index]))
    response.headers["Cache-Control"] = ["no-cache", "must-revalidate"]
    response.headers["Expires"] = "Sat, 26 Jul 1997 05:00:00 GMT"
    return 

# the logs route, returns items to download from logs
@app.route("/raw-data")
def raw_data_get():
    return render_template("raw_data.html", data=info.get_raw_data_filenames())


# the logs route, returns items to download from logs
@app.route("/daily-data")
def daily_data_get():
    return render_template("daily_data.html", data=info.get_daily_data_filenames())


# delete a file from the raw data directory
@app.route("/delete-raw-data")
def delete_raw_data():
    raw_data_filenames = info.get_raw_data_filenames()
    id_to_delete = int(request.args.get("id"))

    zero_point = request.args.get("zero")
    id_adjustment = raw_data_filenames.index(zero_point)

    this_directory = os.path.abspath(os.getcwd())
    os.remove(this_directory + "/data/raw/" + raw_data_filenames[id_to_delete + id_adjustment])
    return "success"


# delete a file from the daily data (zipped) directory
@app.route("/delete-daily-data")
def delete_daily_data():
    daily_data_filenames = info.get_daily_data_filenames()
    id_to_delete = int(request.args.get("id"))

    zero_point = request.args.get("zero")
    id_adjustment = raw_data_filenames.index(zero_point)

    this_directory = os.path.abspath(os.getcwd())
    os.remove(this_directory + "/data/daily/" + daily_data_filenames[id_to_delete + id_adjustment])
    return "success"


# retrieves the last server accelerometer data
@app.route("/last-data", methods=["GET"])
def last_data_get():
    files = os.listdir("data/raw")
    files.sort()
    response = make_response(send_file("../../../data/raw/" + files[-1]))
    response.headers["Cache-Control"] = ["no-cache", "must-revalidate"]
    response.headers["Expires"] = "Sat, 26 Jul 1997 05:00:00 GMT"
    return response

# retrieves server settings
@app.route("/settings", methods=["GET"])
def settings_get():
    response = make_response(jsonify(info.load_settings()))
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
    info.reset_logs()
    info.reset_data()


# restarts the device
@app.route("/restart", methods=["GET"])
def restart_node():
    py.logs.log("SERVER", "Restarting Node")
    os.system("reboot")
    
# updates a system setting, used by the buttons displayed on the webpage. This handles one setting change per request.
@app.route("/update", methods=["GET"])
def update_get():
    valid_keys = ["active", "duration", "rate", "delay", "name", "flashLED", "flashdrive", "reset"]  # prevents changing settings beyond the valid keys
    key = request.args.get("key")
    value = request.args.get("value")
    if key not in valid_keys:
        return "bad"
    # process update
    if key == "active" and value in ["true", "false"]:
        info.updateSettings("active", value)
    elif key == "flashdrive" and value in ["true", "false"]:
        info.updateSettings("flashdrive", value)
    elif key == "duration" and value.isdigit():
        info.updateSettings("duration", value)
    elif key == "rate" and value.isdigit():
        info.updateSettings("rate", value)
    elif key == "delay" and value.isdigit():
        info.updateSettings("delay", value)
    elif key == "name":
        info.updateSettings("name", value)
    elif key == "reset" and value == "true":
        info.reset_data()
        info.reset_logs()
    elif key == "flashLED" and value == "true":
        info.flash_LED()
    return "good"

# starts the Flask app (0.0.0.0 indicates being able to use it with its visible IP address instead of localhost only)
def start_server():
    app.run(host="0.0.0.0", port=80)

if __name__ == "__main__":
    start_server()