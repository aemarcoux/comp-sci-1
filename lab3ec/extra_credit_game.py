# Author: Alexander Marcoux
# Date: 2 March 2023
# Purpose: Guess the continent game
from cs1lib import *
from city import City
from random import *

growing = True

# loading the image
img = load_image("earth.jpeg")

# window size = image size
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 360

# x and y to center of screen
CX = WINDOW_WIDTH // 2
CY = WINDOW_HEIGHT // 2

# number of cities
N = 50

# frame rate
RATE = 10

# number of frames
frames = 1

# radius of dots
RAD = 3

# variables for city info
i = 0
continent = None

# North America
NA_LAT_BOTTOM = 7.5  # North
NA_LAT_TOP = 84.1
NA_LONG_LEFT = -169.5  # West
NA_LONG_RIGHT = -25.5

# South America
SA_LAT_BOTTOM = -55.9
SA_LAT_TOP = 12.2
SA_LONG_LEFT = -81.3
SA_LONG_RIGHT = -35

# Europe
EU_LAT_BOTTOM = 35.9
EU_LAT_TOP = 71.2
EU_LONG_LEFT = -25.2
EU_LONG_RIGHT = 65.6

# Asia
A_LAT_BOTTOM = 5.5
A_LAT_TOP = 77.2
A_LONG_LEFT = 26.6
A_LONG_RIGHT = 169.5
2

# Africa
AF_LAT_BOTTOM = -37
AF_LAT_TOP = 37
AF_LONG_LEFT = -17.5
AF_LONG_RIGHT = 51.5

# Australia
AUS_LAT_BOTTOM = -44.1
AUS_LAT_TOP = -9.2
AUS_LONG_LEFT = 112.9
AUS_LONG_RIGHT = 153.6
# Antarctica is excluded (im not a bully, i promise)

# box parameters (for user choices)
NA_BOX_LEFT = 20
NA_BOX_RIGHT = 120
NA_BOX_BOTTOM = 325
NA_BOX_TOP = 300

SA_BOX_LEFT = 135
SA_BOX_RIGHT = 255
SA_BOX_BOTTOM = 325
SA_BOX_TOP = 300

A_BOX_LEFT = 250
A_BOX_RIGHT = 350
A_BOX_BOTTOM = 325
A_BOX_TOP = 300

AF_BOX_LEFT = 365
AF_BOX_RIGHT = 465
AF_BOX_BOTTOM = 325
AF_BOX_TOP = 300

AUS_BOX_LEFT = 480
AUS_BOX_RIGHT = 580
AUS_BOX_BOTTOM = 325
AUS_BOX_TOP = 300

EU_BOX_LEFT = 595
EU_BOX_RIGHT = 695
EU_BOX_BOTTOM = 325
EU_BOX_TOP = 300

# key pressed variables
na_pressed = False
sa_pressed = False
a_pressed = False
af_pressed = False
aus_pressed = False
eu_pressed = False
correct = False
qpressed = False
ppressed = False

score = 0


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


def keydown(key):
    global qpressed, ppressed

    if key == "q":
        qpressed = True

    if key == "p":
        ppressed = True


def when_pressed():
    global qpressed

    if qpressed:
        cs1_quit()

# defining the city list
cities_pop = parse("cities_population.txt")


def which_continent():
    global continent

    if NA_LONG_LEFT < cities_pop[i][3] < NA_LONG_RIGHT and NA_LAT_BOTTOM < cities_pop[i][2] < NA_LAT_TOP:
        continent = "North America"

    elif SA_LONG_LEFT < cities_pop[i][3] < SA_LONG_RIGHT and SA_LAT_BOTTOM < cities_pop[i][2] < SA_LAT_TOP:
        continent = "South America"

    elif EU_LONG_LEFT < cities_pop[i][3] < EU_LONG_RIGHT and EU_LAT_BOTTOM < cities_pop[i][2] < EU_LAT_TOP:
        continent = "Europe"

    elif A_LONG_LEFT < cities_pop[i][3] < A_LONG_RIGHT and A_LAT_BOTTOM < cities_pop[i][2] < A_LAT_TOP:
        continent = "Asia"

    elif AF_LONG_LEFT < cities_pop[i][3] < AF_LONG_RIGHT and AF_LAT_BOTTOM < cities_pop[i][2] < AF_LAT_TOP:
        continent = "Africa"

    elif AUS_LONG_LEFT < cities_pop[i][3] < AUS_LONG_RIGHT and AUS_LAT_BOTTOM < cities_pop[i][2] < AUS_LAT_TOP:
        continent = "Australia"


def draw_choices_and_score():
    enable_stroke()
    set_stroke_color(1, 1, 1)
    set_fill_color(0, 0.5, 0)

    # North America
    draw_rectangle(20, 300, 100, 25)
    set_font("Palatino")
    set_font_size(12)
    draw_text("North America", 30, 317)

    # South America
    draw_rectangle(135, 300, 100, 25)
    draw_text("South America", 145, 317)

    # Asia
    draw_rectangle(250, 300, 100, 25)
    draw_text("Asia", 285, 317)

    # Africa
    draw_rectangle(365, 300, 100, 25)
    draw_text("Africa", 395, 317)

    # Australia
    draw_rectangle(480, 300, 100, 25)
    draw_text("Australia", 505, 317)

    # Europe
    draw_rectangle(595, 300, 100, 25)
    draw_text("Europe", 625, 317)

    # adding the score
    set_stroke_color(0.8, 0, 0)
    set_font_size(20)
    draw_text("Score: " + str(score), 20, 25)


def clicked(mx, my):
    global na_pressed, sa_pressed, a_pressed, af_pressed, aus_pressed, eu_pressed

    # all values were calculated above and stored as global variables
    if NA_BOX_LEFT <= mx <= NA_BOX_RIGHT and NA_BOX_TOP <= my <= NA_BOX_BOTTOM:
        na_pressed = True

    if SA_BOX_LEFT <= mx <= SA_BOX_RIGHT and SA_BOX_TOP <= my <= SA_BOX_BOTTOM:
        sa_pressed = True

    if A_BOX_LEFT <= mx <= A_BOX_RIGHT and A_BOX_TOP <= my <= A_BOX_BOTTOM:
        a_pressed = True

    if AF_BOX_LEFT <= mx <= AF_BOX_RIGHT and AF_BOX_TOP <= my <= AF_BOX_BOTTOM:
        af_pressed = True

    if AUS_BOX_LEFT <= mx <= AUS_BOX_RIGHT and AUS_BOX_TOP <= my <= AUS_BOX_BOTTOM:
        aus_pressed = True

    if EU_BOX_LEFT <= mx <= EU_BOX_RIGHT and EU_BOX_TOP <= my <= EU_BOX_BOTTOM:
        eu_pressed = True


def is_answer_correct():
    global na_pressed, sa_pressed, a_pressed, af_pressed, aus_pressed, eu_pressed, i, score

    if na_pressed and continent == "North America":
        i = randint(0, len(cities_pop))
        score = score + 1
        na_pressed = False

    if sa_pressed and continent == "South America":
        i = randint(0, len(cities_pop))
        score = score + 1
        sa_pressed = False

    if a_pressed and continent == "Asia":
        i = randint(0, len(cities_pop))
        score = score + 1
        a_pressed = False

    if af_pressed and continent == "Africa":
        i = randint(0, len(cities_pop))
        score = score + 1
        af_pressed = False

    if aus_pressed and continent == "Australia":
        i = randint(0, len(cities_pop))
        score = score + 1
        aus_pressed = False

    if eu_pressed and continent == "Europe":
        i = randint(0, len(cities_pop))
        score = score + 1
        eu_pressed = False

    if na_pressed and continent != "North America":
        score = 0
        na_pressed = False

    if sa_pressed and continent != "South America":
        score = 0
        sa_pressed = False

    if a_pressed and continent != "Asia":
        score = 0
        a_pressed = False

    if af_pressed and continent != "Africa":
        score = 0
        af_pressed = False

    if aus_pressed and continent != "Australia":
        score = 0
        aus_pressed = False

    if eu_pressed and continent != "Europe":
        score = 0
        eu_pressed = False


def title_screen():

    set_clear_color(0, 0, 0)
    clear()

    globe = load_image("globe.jpeg")
    draw_image(globe, 375, 47)

    set_font_normal()
    set_font("Palatino")
    set_font_size(42)
    set_stroke_color(0, 0.8, 0)
    draw_text("Guess the C  " + "  ntinent.", 150, 80)

    set_font_italic()
    set_font_size(16)
    draw_text("an Alexander Marcoux production:", 240, 30)
    draw_text("press 'P' to start the game", 270, 110)

    draw_text("WARNING: I am a mere one-man dev team with limited resources and cannot ensure", 80, 180)
    draw_text("100 percent accuracy of continental borders, but I hope you enjoy regardless!!", 100, 200)
    draw_text("(some of the Asian/Australian islands are difficult to distinguish with a limited set of data)", 60, 220)
    set_font_normal()


def draw_cities():
    global growing, RAD
    # setting the image as the backdrop
    draw_image(img, 0, 0)

    when_pressed()
    is_answer_correct()

    disable_stroke()
    set_fill_color(0.8, 0, 0)  # green

    # scaled coordinates
    px = int((cities_pop[i][3] + 180) / CX * WINDOW_WIDTH)
    py = int((90 - cities_pop[i][2]) / CY * WINDOW_HEIGHT)

    draw_circle(px, py, RAD)

    enable_stroke()
    set_stroke_color(1, 1, 1)
    set_font_size(12)
    draw_text(str(cities_pop[i][0]), px + 10, py)

    which_continent()

    # radius will grow and shrink (animates the cities)
    if growing:
        RAD = RAD + 0.2
    else:
        RAD = RAD - 0.2

    if RAD >= 6 or RAD <= 3:
        growing = not growing

    draw_choices_and_score()


def main():

    title_screen()
    if ppressed:
        clear()
        draw_cities()

start_graphics(main, mouse_press=clicked, framerate=10, key_press=keydown, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)