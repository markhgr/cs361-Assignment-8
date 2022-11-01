
"""
Flask app that takes two timestamps and returns the difference in time between them.
All timestamps are assumed to be in UTC.
Used the following tutorial by Anthony Herbert for help with accepting JSON objects
that are part of POST requests.
https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

"""
from flask import Flask, render_template, request
import json  # used to open timestamp arrays
from datetime import datetime  # used to calculate time difference

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def main():
    if request.method == 'POST':
        # get the start and end times as returned in ISO format from the html
        start_iso = request.form['start_time']
        end_time = request.form['end_time']
        # convert the start and end times to python's datetime format
        start_time = datetime.fromisoformat(start_time)
        end_time = datetime.fromisoformat(end_time)

        return render_template('app.html', start_time = start_time, end_time = end_time)
    return render_template('app.html')

@app.route("/calculate_time", methods = ['POST'])
def process_request():
    time_request = request.get_json()
    # get the name submitted from the text box
    if request.method == 'POST':
        # will turn True if input is invalid
        errors = False
        print("TEST")
    return render_template('app.html')