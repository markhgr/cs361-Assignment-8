
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

def get_time_delta(start_iso, end_iso):
    """
    Converts ISO 8601 date strings to python datetime objects.
    Then subtracts the start datetime object from the end
    datetime object and returns the resulting timedelta object,
    representing how much time has passed from start to finish.
    """

    # convert the start and end times to python's datetime format
    start_datetime = datetime.fromisoformat(start_iso)
    end_datetime = datetime.fromisoformat(end_iso)

    # get the difference by subtracting the start time from the end time.
    # this is is assuming that the end timestamp always occurs after the first timestamp.
    # will need to be improved with error checking.
    time_delta = start_datetime - end_datetime

    return time_delta

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def main():
    if request.method == 'POST':
        # get the start and end times as returned in ISO format from the html
        start_time_iso = request.form['start_time']
        end_time_iso = request.form['end_time']

        time_delta = get_time_delta(start_time_iso, end_time_iso)

        return render_template('app.html', message = "Time elapsed: ", time_elapsed = time_delta)
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