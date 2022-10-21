
from flask import Flask
import constants

app = Flask(__name__)

API_KEY = constants.API_KEY
MAPS_API_URL = "https://maps.googleapis.com/maps/api/directions/json?"

import requests


@app.route('/')
def root():
    return "Please navigate to /driving/origin/destination to use this API"\

@app.route('/driving/<origin>/<destination>')
def get_route(origin, destination):

    request_url = MAPS_API_URL + 'origin=' + origin + '&destination=' + destination + '&key=' + API_KEY

    content = requests.get(request_url).json()

    # Error handling when Maps API request is not successful
    if content["status"] != "OK":
        return ({"Error": content["status"]}, 404)

    # Case for a successful request
    output = {}
    output["duration"] = content["routes"][0]["legs"][0]["duration"]["value"]
    output["startingAddress"] = content["routes"][0]["legs"][0]["start_address"]
    output["endingAddress"] = content["routes"][0]["legs"][0]["end_address"]

    return (output, 200)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
