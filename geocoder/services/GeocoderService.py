import json
import urllib.request
import urllib.parse

from geocoder.services.GoogleMapsGeocoder import GoogleMapsGeocoder
from geocoder.services.HEREGeocoder import HEREGeocoder
import config

class GeocoderService:

    def __init__(self):
        primaryName = config.geocoder['primary']
        secondaryName = config.geocoder['secondary']

        print("init GeocoderService, primary: "+primaryName+", secondary: "+secondaryName)

        self.primaryGeocoder = self.provider(primaryName)
        self.secondaryGeocoder = self.provider(secondaryName)

    def provider(self, name):
        if name == 'googlemaps':
            return GoogleMapsGeocoder()
        elif name == 'here':
            return HEREGeocoder()
        else:
            print("ERROR: unsupported gecoder + '"+name+"'")
            raise NotImplementedError("unsupported gecoder + '"+name+"'")


    def geocode(self, address):
        result = None

        print("Geocoding address: "+address)

        result = self._doGeocoding(address, self.primaryGeocoder)

        if(result):
            return json.dumps({'lat':result.lat,'long':result.long})
        else:
            print("Primary failed, falling back to secondary geocoder")
            result = self._doGeocoding(address, self.secondaryGeocoder)
            if(result):
                return json.dumps({'lat':result.lat,'long':result.long})
            else:
                return None


    def _doGeocoding(self, address, provider):
        """Returns a LatLong result if its found, or None if not found or there is an error"""

        parameters = provider.parameters(address)
        encoded_params = urllib.parse.urlencode(parameters)
        url = provider.url + encoded_params

        print("Geocode request to URL: "+url)

        req = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(req)

            print("Gecode returned code: "+str(response.status))

            if(response.status == 200):
                json_string = response.read().decode('utf-8')
                json_obj = json.loads(json_string)

                return provider.processResponse(json_obj)

        except urllib.error.HTTPError as e:
            print("ERROR: HTTPError, status codes: "+e.code+", reason: ''"+e.reason+"'")
        except urllib.error.URLError as e1:
            print("ERROR: URLError, reason: '"+e1.reason+"'")

        return None
