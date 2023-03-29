# Author: Alexander Marcoux
# Date: 1 March 2023
# Purpose: Visualizing "n" number of cities on a world map
from cs1lib import *
from city import City
from random import *

# used to make the cities grow and shrink in size
growing = True

# loading the image
img = load_image("world.png")

# window size = image size
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 360

# x and y to center of screen
CX = WINDOW_WIDTH // 2
CY = WINDOW_HEIGHT // 2

# number of desired cities
N = 50

# frame rate
RATE = 10

# number of cities currently drawing
num_cities = 1

# radius of dots/cities
RAD = 3


# function to parse through a file
def parse(filename):
    cities_list = open(filename, "r")

    # empty list which will be filled with parsed info
    cities = []

    for line in cities_list:
        line.strip()
        city_info = line.split(",")
        # add parsed info to empty list
        cities.append([city_info[0], int(city_info[1]), float(city_info[2]), float(city_info[3])])

    # closing the file we opened
    cities_list.close()
    return cities


# visualizing the parsed info
def draw_cities():
    global growing, RAD, num_cities
    # setting the image as the backdrop
    draw_image(img, 0, 0)

    # parsing world_cities file
    cities_pop = parse("cities_population.txt")

    i = 0
    while i < num_cities:  # will go from index 0 to 49 (50 cities)
        disable_stroke()
        set_fill_color(0.8, 0, 0)  # red

        # scaled coordinates
        px = int((cities_pop[i][3] + 180) / CX * WINDOW_WIDTH)
        py = int((90 - cities_pop[i][2]) / CY * WINDOW_HEIGHT)

        draw_circle(px, py, RAD)

        # increment the counter
        i += 1

    # we want num_cities to equal the number of desired cities
    if num_cities < N:
        num_cities += 1

    # radius will grow and shrink (animates the cities)
    if growing:
        RAD = RAD + 0.2
    else:
        RAD = RAD - 0.2

    if RAD >= 5 or RAD <= 2:
        growing = not growing


start_graphics(draw_cities, framerate=RATE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)