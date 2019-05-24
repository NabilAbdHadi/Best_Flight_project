import gmplot
from geopy import *
import requests
import json
import googlemaps
import math
import numpy as np
from itertools import tee


def coordinate(input):
    major_city_address = {}
    geolocator = Nominatim(user_agent="Best Flight")
    for index, city in enumerate(input):
        location = geolocator.geocode(city, language='en')
        major_city_address[city] = [location.latitude, location.longitude]
    return major_city_address


# plot map using gmplot
def plotMap(input):
    for key, value in input.items():
        print(key, value)
        gmap = gmplot.GoogleMapPlotter(value[0], value[1], 18)
        gmap.draw("map%s.html" % key)


def distance(input):
    disMat = {}
    """gmaps = googlemaps.Client(key='AIzaSyBYAQcMFPMWlwctq82tQkqoB_-X_TdbprA')  # something wrong
    for i, Origin in enumerate(input):
        for j, Destination in enumerate(input):
            my_dist = gmaps.distance_matrix(Origin, Destination)['rows'][0]['elements'][0]
            print(i, j)
            print(my_dist)"""
    print(disMat)
    for keyO, valueO in input.items():
        disMat[keyO] = []
        for keyD, valueD in input.items():
            x = valueD[0] - valueO[0]
            y = valueD[1] - valueO[1]
            my_dist = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
            disMat[keyO].append(my_dist)
            print(my_dist)

    return disMat


# Kuala lumpur as the reference place
major_city = ["Kuala Lumpur", "New York City", "Istanbul", "Beijing", "Manila", "Berlin"]

coor = coordinate(major_city)
print(coor)
Dis = distance(coor)
print(Dis)
# plotMap(coor)
# distanceCalc(coor)
