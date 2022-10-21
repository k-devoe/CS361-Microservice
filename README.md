# CS361-Microservice: Google Maps Interface

## Overview

This microservice provides the total route drive time in seconds and start and end addresses from a request with an origin and destination. To accomplish this Google Maps API is used on the backend by the microservice to lookup the total route time, and get full addresses based on the input destination. 


## Requests

Requests to the API can be made through GET requests to the https://cs361-mapsapi.wl.r.appspot.com URL. Requests are made in the format of https://cs361-mapsapi.wl.r.appspot.com/driving/:origin/:destination where "origin" and "destination" are names of locations driving from and driving to input by the requestor.

Note: For inputs with spaces such as "Pike Place Market", the spaces should be replaced with a "+" for example: "Pike+Place+Market"

Example request:

GET https://cs361-mapsapi.wl.r.appspot.com/driving/Pike+Place+Market/Space+Needle


## Responses

Responses will be in JSON format with 2 possible outcomes:

### Successful lookup

A successful query will generate a response code of 200 with the following JSON information:

- duration:         Total time of trip in seconds  
- startingAddress:  Full address of origin location  
- endingAddress:    Full address of destination location  

Example response:  

{  
    "duration": 403,  
    "endingAddress": "400 Broad St, Seattle, WA 98109, USA",  
    "startingAddress": "Pike Place Market, Seattle, WA, USA"  
}  

### Unsuccessful lookup

An unsuccessful lookup will generate a response code of 404 with the following JSON information:

- Error: Reason for lookup failure as the error code from Google Maps API

A couple of reasons for unsuccessful lookup are either a location does not exist or there is no route between them. Here are a couple of examples for unsuccessful lookups and responses:

Example 1 of a bad request. Using a location that does not exist (None):  
GET: https://cs361-mapsapi.wl.r.appspot.com/driving/None/Space+Needle  
Response Code: 404  
Example 1 Reponse:  
{  
    "Error": "NOT_FOUND"  
}  

Example 2 of a bad request. Using a location that does not have a route to the destination (Seattle to Hawaii by car):  
GET: https://cs361-mapsapi.wl.r.appspot.com/driving/Space+Needle/Hawaii  
Response Code: 404  
Example 2 Response:  
{  
    "Error": "ZERO_RESULTS"  
}  

