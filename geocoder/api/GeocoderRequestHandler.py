from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from geocoder.services.GeocoderService import GeocoderService

class GeocoderRequestHandler(BaseHTTPRequestHandler):
    """Handle all requests"""

    def do_GET(self):
        url = urlparse(self.path)

        """Basic routing"""
        if url.path == "/geocode":
            parameters = parse_qs(url.query)
            address = self.getParameter("address", parameters)

            if address:
                result = GeocoderService().geocode(address)

                if(result):
                    self.send_response(200, 'OK')
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(bytes(result, 'UTF-8'))
                else :
                    self.send_error(404)
                    self.end_headers()
            else :
                self.send_error(400)
                self.end_headers()
        else:
            self.send_error(404)
            self.end_headers()

    def getParameter(self, name, parameters):
        if name not in parameters:
            return None

        if len(parameters[name]) != 1:
            return None

        return str(parameters[name][0])
