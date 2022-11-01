# cs361-Assignment-8
Code for microservice running on pythonanywhere

### CS361 Microservice by Mark Hager
Takes two timestamps in ISO 8601 format and calculates the delta between them
in order to determine how much time has elapsed.

**how to REQUEST data:**
send a POST request to http://hagermosu.pythonanywhere.com/calculate_time that has a JSON file in the body
of the request with two ISO 8601 UTC timestamps in the following format:
```
    { 
    "start_time" : "timestamp #1"
    "end_time"   : "timestamp #2
    }      
```
Results are returned in the body of the POST response.  

**how to RECEIVE data:**  Manually enter timestamps into the main page and press the submit button to submit a form containing the timestamps in a POST request. The results will then be displayed on the main page. 
