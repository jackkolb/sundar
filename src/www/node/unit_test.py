# node_server.py: runs a Flask server to handle interfacing with the node

from flask import Flask, render_template, request, jsonify, send_file, make_response
import os

app = Flask(__name__)  # the overall Flask app

# sets logging to only show errors (not logging each individual request)
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

# gets all the log file names
def load_all_logs():
    log_list = os.listdir("../../../logs/")
    return log_list

# download logs
@app.route("/download-log", methods=["GET"])
def download_log_get():
    log_file_names = load_all_logs()
    log_file_index = int(request.args.get("id"))
    response = make_response(send_file("../../../logs/" + log_file_names[log_file_index], as_attachment=True, attachment_filename=log_file_names[log_file_index]))
    response.headers["Cache-Control"] = ["no-cache", "must-revalidate"]
    response.headers["Expires"] = "Sat, 26 Jul 1997 05:00:00 GMT"
    return response

# the logs route, returns items to download from logs
@app.route("/logs")
def logs_get():
    return render_template("logs.html", logs=load_all_logs())

# starts the Flask app (0.0.0.0 indicates being able to use it with its visible IP address instead of localhost only)
def start_server():
    app.run(host="0.0.0.0", port=80)

start_server()