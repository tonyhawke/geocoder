import config
from geocoder.api.LatLong import LatLong

class HEREGeocoder:

    url = config.provider["here"]["url"]

    def parameters(self, address):
        return {
            'searchText':address,
            'app_id':config.provider["here"]["appId"],
            'app_code':config.provider["here"]["appCode"]
        }

    def processResponse(self, json_obj):
        response = json_obj["Response"]
        if(response):
            view = response["View"]
            if(view):
                results = view[0]["Result"]
                if(results):
                    location = results[0]["Location"]
                    if(location):
                        displayPosition = location["DisplayPosition"]
                        return LatLong(displayPosition["Latitude"],displayPosition["Longitude"])
        return None
