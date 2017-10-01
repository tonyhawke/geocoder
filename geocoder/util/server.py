from http.server import HTTPServer, SimpleHTTPRequestHandler

class GeocoderServer:
    """Encapsulated the http server instance"""

    def __init__(self, name, port):
        self.name = name
        self.port = port

    def start(self):
        print("Geocoder Server starting, name="+self.name+", port="+str(self.port))
        httpd = HTTPServer((self.name, self.port), SimpleHTTPRequestHandler)
        httpd.serve_forever()

        print("Geocoder Server started.")
