# CS361-Microservice: Google Maps Interface

## Overview

This microservice provides the total route drive time in seconds and start and end addresses from a request with an origin and destination. To accomplish this Google Maps API is used on the backend by the microservice to lookup the total route time, and get full addresses based on the input destination. 


## Requests

Requests to the API can be made through GET requests to the PUTURLHERE URL. Requests are made in the format of PUTURLHERE/driving/:origin/:destination where "origin" and "destination" are names of locations driving from and driving to input by the requestor.

Note: For inputs with spaces such as "Pike Place Market", the spaces should be replaced with a "+" for example: "Pike+Place+Market"

Example request:

GET PUTURLHERE/driving/Pike+Place+Market/Space+Needle


## Responses

Responses will be in JSON format with 2 possible outcomes:

### Successful lookup

A successful query will generate a response code of 200 with the following JSON information:

- duration:         Total time of trip in seconds
- startingAddress:  Full address of origin location
- endingAddress:    Full address of destination location

Example response:

PUTEXAMPLERESPONSE HERE

### Unsuccessful lookup

An unsuccessful lookup will generate a response code of 404 with the following JSON information:

- Error:          Reason for lookup failure as the error code from Google Maps API

A couple of reasons for unsuccessful lookup are either a location does not exist or there is no route between them. Here are a couple of examples for unsuccessful lookups:

Example 1 Request:


Example 1 Reponse:

Example 2 GET request:


Example 2 Response:

