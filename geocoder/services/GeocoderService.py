import json

from geocoder.services.GoogleMapsGeocoder import GoogleMapsGeocoder

class GeocoderService:

    def __init__(self):
        self.primaryGeocoder = GoogleMapsGeocoder()

    def geocode(self, address):
        result = None

        print(address)

        result = self.primaryGeocoder.geocode(address);

        if(result):
            return json.dumps({'lat':result.lat,'long':result.long})
