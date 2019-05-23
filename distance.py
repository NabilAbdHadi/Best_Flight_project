import gmplot
from geopy import *


def coordinate(input):
    major_city_address = {}
    geolocator = Nominatim(user_agent="Best Flight")
    for index, city in enumerate(input):
        location = geolocator.geocode(city, language='en')
        major_city_address[city] = [location.latitude, location.longitude]

        #gmap = gmplot.GoogleMapPlotter.from_geocode(major_city_address[city])
        #print(gmap)
    return major_city_address

# Kuala lumpur as the reference place
major_city = ["Kuala Lumpur", "New York City", "Istanbul", "Beijing", "Manila", "Berlin"]
print(coordinate(major_city))
