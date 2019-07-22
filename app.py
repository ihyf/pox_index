import os
from flask import Flask, render_template
from flask import request, jsonify, send_from_directory, abort

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/download_file/<filename>')
def download_filename(filename):
    if request.method == "GET":
        if os.path.isfile(os.path.join('static/files', filename)):
            return send_from_directory('static/files', filename, as_attachment=True)
        abort(404)


@app.route('/download')
def download():
    if request.method == "GET":
        if os.path.isfile(os.path.join('static/files', "pox_wallet.apk")):
            return send_from_directory('static/files', "pox_wallet.apk", as_attachment=True)
        abort(404)


if __name__ == "__main__":
    app.run(port=9000, host="0.0.0.0", debug=False)
