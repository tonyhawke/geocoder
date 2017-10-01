import config
from geocoder.api.LatLong import LatLong

class GoogleMapsGeocoder:
    url = config.provider["googlemaps"]["url"]

    def parameters(self, address):
        return {
            "address":address,
            "key":config.provider["googlemaps"]["key"]
        }

    def processResponse(self, json_obj):
        results = json_obj["results"]
        if(results):
            result = results[0]
            if(result):
                geometry = result["geometry"]
                if(geometry):
                    location = geometry["location"]
                    if(location):
                        return LatLong(location["lat"],location["lng"])
        return None
