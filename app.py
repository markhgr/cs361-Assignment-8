
"""
Flask app that takes two timestamps and returns the difference in time between them.
All timestamps are assumed to be in UTC.
Used the following tutorial by Anthony Herbert for help with accepting JSON objects
that are part of POST requests.
https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

"""
from flask import Flask, render_template, request
import json  # used to open timestamp arrays
import requests # used to query partner's microservice
from datetime import datetime  # used to calculate time difference
import dateutil.parser # used to read iso datetimes from JSON

# import our call_microservice function
from call_microservice import *

def get_time_delta(race_times):
    """
    Reads the JSON containing a runner's start and end
    marathon times formattted as ISO 8601 date strings
    and converts these to python datetime objects.
    Then subtracts the start datetime object from the end
    datetime object and returns the resulting timedelta object,
    representing how much time has passed from start to finish.
    """

    # convert the start and end times to python's datetime format
    start_datetime = dateutil.parser.parse(race_times[0])

    end_datetime = dateutil.parser.parse(race_times[1])

    # get the difference by subtracting the start time from the end time.
    # this is is assuming that the end timestamp always occurs after the first timestamp.
    # will need to be improved with error checking.
    time_delta = end_datetime - start_datetime

    return time_delta

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def main():
    if request.method == 'POST':
        # get the first and last name to query times from Richard's microservice
        f_name = request.form['fname']
        l_name = request.form['lname']
        # get the start and end times from the race from the microservice
        race_times = call_microservice(f_name, l_name)
        # try getting the time delta using our function
        print(race_times)
        try:
            time_delta = get_time_delta(race_times)
        except:
            # if it doesn't work then we can assume the name search did not succeed.
            print("ERORR")
            time_delta = "Error: runner not found"

        return render_template('app.html', message = "Time elapsed: ", time_elapsed = time_delta)
    return render_template('app.html')


@app.route("/calculate_time", methods = ['POST'])
def process_request():
    timestamps = request.get_json()

    # read the start and end times in ISO format
    start_time_iso = timestamps['start_time']
    end_time_iso = timestamps['end_time']
    
    time_delta = get_time_delta(start_time_iso, end_time_iso)
    # return the time difference in the body of the POST request

    results = f'time_delta:{time_delta}'
    results_json = json.dumps(results)

    return results
