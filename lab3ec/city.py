# Author: Alexander Marcoux
# Date: 1 March 2023
# Purpose: City class for lab--3
from cs1lib import *
from random import *

# parameters used for converting latitude and longitude
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 360


class City:
    def __init__(self, country_code, name, region, population, latitude, longitude):
        self.country_code = country_code
        self.name = name
        self.region = region
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        # returns name, population, latitude, longitude
        return self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)

    def draw(self, cx, cy, rad):
        # converting latitude and longitude into pixels
        px = int((self.longitude + 180) / cx * WINDOW_WIDTH)
        py = int((90 - self.latitude) / cy * WINDOW_HEIGHT)

        # drawing the circle with the scaled measurements
        draw_circle(px, py, rad)