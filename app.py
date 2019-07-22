#!/usr/bin/python3
""" Demonstrating Flask, using APScheduler. """

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """ Function for test purposes. """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=9000)