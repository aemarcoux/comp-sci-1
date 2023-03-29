# Author: Alexander Marcoux
# Date: 20 February 2023
# Purpose: Extra Credit Game for Solar System

from cs1lib import *
from ecbody import Body
from ecsystem import System
from math import *
from random import *

# window constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
WINDOW_BASE = 0
WINDOW_LEFT = 0

# conversion constants
TIME_SCALE = 3.0e6         # real seconds per simulation second
INITIAL_TIME_SCALE = 3.0e6
PIXELS_PER_METER = 10 / 1e10  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

# spaceship constants
SPACESHIP_VY = 4
SPACESHIP_VX = 4
INITIAL_BODY_X = 400
INITIAL_BODY_Y = 780
BODY_X = 400
BODY_Y = 780
BODY_WIDTH = 8
BODY_HEIGHT = 16
SECURITY = 3  # adding 3 pixels to ensure contact is detected

# star constant
STAR_RADIUS = 1

# meteor constant
METEOR_X = randint(0, 800)
METEOR_Y = 0
METEOR_VX = randint(-3, 3)
METEOR_VY = randint(5, 8)
METEOR_RADIUS = 10

# key pressed variables
space_pressed = False
apressed = False
dpressed = False
qpressed = False
ppressed = False

# game variables
top_reached = False
score = 0
contact = False
growing = False
sz = 16

# function that creates stars in random positions
def stars():
    i = 0
    set_stroke_color(1, 1, 1)  # white
    # creating 25 stars
    while i <= 25:
        draw_circle(randint(WINDOW_BASE, WINDOW_WIDTH), randint(WINDOW_BASE, WINDOW_HEIGHT), STAR_RADIUS)
        i = i + 1

# creating the spaceship
def spaceship():

    enable_stroke()

    # body of the spaceship
    set_stroke_color(0, 0, 0)  # black
    set_fill_color(54/256, 69/256, 79/256)  # charcoal
    draw_rectangle(BODY_X, BODY_Y, BODY_WIDTH, BODY_HEIGHT)

    # tip
    set_fill_color(1, 0, 0)
    draw_triangle(BODY_X - 2, BODY_Y, BODY_X + 10, BODY_Y, BODY_X + 4, BODY_Y - int(sqrt(48)))

    # thruster/fins
    set_fill_color(1, 94/256, 5/256)
    draw_triangle(BODY_X, BODY_Y + BODY_HEIGHT, BODY_X + 8, BODY_Y + BODY_HEIGHT, BODY_X + 4, BODY_Y + 24)
    set_fill_color(1, 0, 0)
    draw_triangle(BODY_X, BODY_Y + 8, BODY_X, BODY_Y + BODY_HEIGHT, BODY_X - 6, BODY_Y + 22)
    draw_triangle(BODY_X + 8, BODY_Y + 8, BODY_X + 8, BODY_Y + BODY_HEIGHT, BODY_X + 14, BODY_Y + 22)

    # adding the score
    set_font("Palatino")
    set_font_size(24)
    set_stroke_color(1, 0, 0)
    draw_text("score: " + str(score), 10, 20)

def keydown(key):
    global space_pressed, apressed, dpressed, qpressed, ppressed

    if key == " ":
        space_pressed = True

    elif key == "a":
        apressed = True

    elif key == "d":
        dpressed = True

    elif key == "q":
        qpressed = True

    elif key == "p":
        ppressed = True

def keyup(key):
    global apressed, dpressed

    if key == "a":
        apressed = False

    elif key == "d":
        dpressed = False

def when_pressed():
    global BODY_Y, BODY_X, contact

    if space_pressed:
        BODY_Y -= SPACESHIP_VY
        contact = False
        # rectangle to cover the "boom text"
        set_fill_color(0, 0, 0)
        draw_rectangle(320, 90, 80, 60)

    if dpressed:
        BODY_X += SPACESHIP_VX

    if apressed:
        BODY_X -= SPACESHIP_VX

    if qpressed:
        cs1_quit()  # quits screen

def collision():
    global top_reached, contact

    if BODY_Y - int(sqrt(48)) < WINDOW_BASE:
        top_reached = True

    if top_reached:
        add_score()

    if WINDOW_WIDTH / 2 + sun.x * PIXELS_PER_METER - sun.pixel_radius <= BODY_X <= \
            WINDOW_WIDTH / 2 + sun.x * PIXELS_PER_METER + sun.pixel_radius and \
            WINDOW_WIDTH / 2 + sun.y * PIXELS_PER_METER - sun.pixel_radius <= BODY_Y <= \
            WINDOW_WIDTH / 2 + sun.y * PIXELS_PER_METER + sun.pixel_radius:

        contact = True

    if WINDOW_WIDTH / 2 + mercury.x * PIXELS_PER_METER - mercury.pixel_radius - SECURITY <= BODY_X <= \
            WINDOW_WIDTH / 2 + mercury.x * PIXELS_PER_METER + mercury.pixel_radius + SECURITY and \
            WINDOW_WIDTH / 2 + mercury.y * PIXELS_PER_METER - mercury.pixel_radius - SECURITY <= BODY_Y <= \
            WINDOW_WIDTH / 2 + mercury.y * PIXELS_PER_METER + mercury.pixel_radius + SECURITY:

        contact = True

    if WINDOW_WIDTH / 2 + venus.x * PIXELS_PER_METER - venus.pixel_radius - SECURITY <= BODY_X <= \
            WINDOW_WIDTH / 2 + venus.x * PIXELS_PER_METER + venus.pixel_radius + SECURITY and \
            WINDOW_WIDTH / 2 + venus.y * PIXELS_PER_METER - venus.pixel_radius - SECURITY <= BODY_Y <= \
            WINDOW_WIDTH / 2 + venus.y * PIXELS_PER_METER + venus.pixel_radius - SECURITY:

        contact = True

    if WINDOW_WIDTH / 2 + earth.x * PIXELS_PER_METER - earth.pixel_radius - SECURITY <= BODY_X <= \
            WINDOW_WIDTH / 2 + earth.x * PIXELS_PER_METER + earth.pixel_radius + SECURITY and \
            WINDOW_WIDTH / 2 + earth.y * PIXELS_PER_METER - earth.pixel_radius - SECURITY <= BODY_Y <= \
            WINDOW_WIDTH / 2 + earth.y * PIXELS_PER_METER + earth.pixel_radius + SECURITY:

        contact = True

    if WINDOW_WIDTH // 2 + mars.x * PIXELS_PER_METER - mars.pixel_radius - SECURITY <= BODY_X <= \
            WINDOW_WIDTH / 2 + mars.x * PIXELS_PER_METER + mars.pixel_radius + SECURITY and \
            WINDOW_WIDTH / 2 + mars.y * PIXELS_PER_METER - mars.pixel_radius - SECURITY <= BODY_Y <= \
            WINDOW_WIDTH / 2 + mars.y * PIXELS_PER_METER + mars.pixel_radius + SECURITY:

        contact = True

    if METEOR_X - METEOR_RADIUS <= BODY_X <= METEOR_X + METEOR_RADIUS and METEOR_Y - METEOR_RADIUS <= BODY_Y <= METEOR_Y + METEOR_RADIUS:

        contact = True

    if contact:
        boom()

def boom():
    global score, space_pressed, contact, BODY_X, BODY_Y, TIME_SCALE

    # message when contact is made
    enable_stroke()
    set_stroke_color(1, 0, 0)
    set_font_size(24)
    draw_text("boom!", 370, 100)
    set_font_size(12)
    draw_text("Press SPACE to restart", 350, 120)

    # resetting variables
    score = 0
    TIME_SCALE = INITIAL_TIME_SCALE
    BODY_X = INITIAL_BODY_X
    BODY_Y = INITIAL_BODY_Y
    space_pressed = False

def meteor():
    global METEOR_X, METEOR_Y, METEOR_VX, METEOR_VY

    # generating random meteors as obstacles
    set_stroke_color(0, 0, 0)
    set_fill_color(0.85, 0.85, 0.85)
    draw_circle(METEOR_X, METEOR_Y, 10)

    METEOR_X = METEOR_X + METEOR_VX
    METEOR_Y = METEOR_Y + METEOR_VY

    if WINDOW_WIDTH < METEOR_X < WINDOW_BASE or METEOR_Y > WINDOW_HEIGHT:
        METEOR_X = randint(WINDOW_BASE, WINDOW_HEIGHT)
        METEOR_Y = 0
        METEOR_VX = randint(-3, 3)
        METEOR_VY = randint(5, 8)

def add_score():
    global score, space_pressed, top_reached, BODY_X, BODY_Y, TIME_SCALE, contact

    # resetting the position of the spaceship, adding to the score, and speeding up the orbit
    BODY_X = INITIAL_BODY_X
    BODY_Y = INITIAL_BODY_Y
    score += 1
    TIME_SCALE *= 1.2

    contact = False
    space_pressed = False
    top_reached = False

def title_screen():
    global growing, sz

    set_clear_color(0, 0, 0)    # black background
    enable_stroke()
    clear()

    # add stars into background
    stars()

    # add title text
    set_font("Palatino")
    set_font_size(48)
    set_stroke_color(1, 0, 0)  # red
    draw_text("Welcome to the Solar System!", 100, 400)

    # pulsing 'p' to add emphasis
    if growing:
        sz = sz + 1
    else:
        sz = sz - 1

    set_stroke_color(1, 0, 0)  # red
    set_font_size(24)
    draw_text("Press", 270, 440)

    set_font_size(sz)
    draw_text("P", 340, 440)

    set_font_normal()
    set_font_size(24)
    draw_text("to start the game!", 370, 440)

    set_font_size(16)
    draw_text("When in game, hit SPACEBAR to begin; use 'a' and 'd' to navigate.", 175, 750)
    draw_text("Watch out for unforeseen obstacles!", 290, 770)

    draw_text("Have you ever played sharks and minnows??", 260, 470)
    draw_text("The rules of the game are simple: make it to the other side!", 210, 500)

    draw_text("An Alexander Marcoux Production:", 280, 50)

    # pulsing quantity
    if sz >= 24 or sz <= 8:
        growing = not growing

# container function
def main():

    disable_stroke()

    # Draw the system in its current state.
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)

    set_stroke_color(1, 1, 1)  # white
    meteor()
    when_pressed()
    collision()
    spaceship()
    stars()

# func called by start_graphics
def start_game():
    title_screen()

    if ppressed:
        clear()
        main()

# list of bodies in solar system
sun = Body(1.98892e30, 0, 0, 0, 0, 24, 1, 1, 0, "sun.jpg")
mercury = Body(0.33e24, 57.9e9, 0, 0, 47890, 6, 0.85, 0.85, 0.85, "mercury.jpg")
venus = Body(4.87e24, 108.2e9, 0, 0, 35040, 10, 1, 0.75, 0, "venus.jpg")
earth = Body(5.97e24, 149.6e9, 0, 0, 29790, 14, 0, 0, 1, "earth.jpg")
mars = Body(0.642e24, 227.9e9, 0, 0, 24140, 10, 1, 0, 0, "mars.jpg")
solar_system = System([sun, mercury, venus, earth, mars])


start_graphics(start_game, 2400, framerate=FRAMERATE, key_press=keydown, key_release=keyup, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)