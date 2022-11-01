
"""
Flask app that takes two timestamps and returns the difference in time between them.
All timestamps are assumed to be in UTC.
Used the following tutorial by Anthony Herbert for help with accepting JSON objects
that are part of POST requests.
https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

"""
from flask import Flask, render_template, request
import json  # used to open timestamp arrays
import time  # used to calculate time difference

app = Flask(__name__)


@app.route("/calculate_time", methods = ['POST'])
def main():
    #time_request = request.get_json()
    # get the name submitted from the text box
    if request.method == 'POST':
        # will turn True if input is invalid
        errors = False
        print("TEST")
    return render_template('app.html')