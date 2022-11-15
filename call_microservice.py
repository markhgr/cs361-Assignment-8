"""
Contains function for calling Richard's node.js microservice
in order to obtain start and end times of runners.
"""
# allows python to send post requests
import requests
import json

runner_db = 'http://localhost:3000/store'

def call_microservice(f_name, l_name):
    """
    Calls Richard's microservice using the first and last names entered
    and submitted using the html form.
    """
    requests_session = requests.session()
    # read the data in the body of the POST response as JSON
    requests_session.headers.update({'Content-Type': 'application/json'})
    requests_session.headers.update({'charset':'utf-8'})
    # construct our POST request which will be converted to JSON
    name_search = [f_name, l_name]
    # try and send our search as a POST request to the microservice

    try:
        post_request = requests.post(runner_db, json=name_search)
        # load the results
        race_times = json.loads(post_request.text)
    except:
        # if there's an error then return an error
        race_times = "Error: runner not found"

    return race_times


