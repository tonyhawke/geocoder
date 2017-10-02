<p align="center">

  <h3 align="center">Geocoder</h3>

  <p align="center">
    A simple network service that can resolve the lat, lng coordinates for an address.
  </p>
</p>

<br>

## Table of contents

- [How to Run the Service](#how-to-run-the-service)
- [How to Use the Services API](#how-to-use-the-services-api)

## How to Run the Service

The Geocoder service requires Python 3.6+ with SSL certs installed (see 'notes' [here](https://www.python.org/downloads/release/python-360/))

- Download or Clone this repo
- Open config.py in an editor and update:
  - Server name and port (or leave defaults)
  - Add provider keys/codes for GoogleMaps and HERE
- Open a terminal and run: 'python geocoder.py' (or 'python3 geocoder.py')
- If you see 'Geocoder Server starting, name=localhost, port=8000' the service is now running successfully.
- To stop the service, simply terminate the process (cmd+c)


## How to Use the Services API

Once the server is running, the service is available via an API:

End point:

`GET http://localhost:8000/geocoder`

Query Parameters

|Name|Purpose|
|---|---|
|address|query string to look up|


Response
```json
{
  "lat": 37.7911924,
  "lng": -122.3981466
}
```

Example

`http://localhost:8000/geocode?address=1600%20Pensylvania%20Ave,%20Washington%20DC`
