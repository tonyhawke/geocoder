import config
import signal
import time

from geocoder.util.server import GeocoderServer

server = GeocoderServer(config.server['name'],config.server['port'])

def shutdownHandler(signum, frame):
    print("Geocoder stopped")
    exit()
    
signal.signal(signal.SIGINT, shutdownHandler)

server.start()
