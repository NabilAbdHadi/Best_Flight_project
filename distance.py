import gmplot
from geopy import *

def coordinate(input):
    major_city_address = {}
    geolocator = Nominatim(user_agent="Best Flight")
    for index, city in enumerate(input):
        location = geolocator.geocode(city, language='en')
        major_city_address[city] = [location.latitude, location.longitude]
    return major_city_address

#plot map using gmplot
def plotMap(input):
    for key,  value in input.items():
        print(key, value)
        gmap = gmplot.GoogleMapPlotter(value[0], value[1], 18)
        gmap.draw("map%s.html" %key)

# Kuala lumpur as the reference place
major_city = ["Kuala Lumpur", "New York City", "Istanbul", "Beijing", "Manila", "Berlin"]

coor = coordinate(major_city)

plotMap(coor)

