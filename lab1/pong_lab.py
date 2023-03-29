# Author: Alexander Marcoux
# Date: 4 February 2023
# Purpose: Final Version of Pong
from cs1lib import *

# defining constants for walls and paddles
WINDOW_LEFT_X = 0
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WINDOW_BASE = 0
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 80
LEFT_PAD_X = 0
LEFT_PAD_Y = 0
RIGHT_PAD_X = 380
RIGHT_PAD_Y = 320
PADDLE_SPEED = 7

# globals for keys pressed
apressed = False
zpressed = False
kpressed = False
mpressed = False
qpressed = False
space_pressed = False

# constants and globals for the ball
INITIAL_BALL_X = 200
INITIAL_BALL_Y = 200
BALL_X = 200
BALL_Y = 200
INITIAL_VELO_X = 3
INITIAL_VELO_Y = 1
CONTACT_VERT_WALL = False
CONTACT_HOR_WALL = False
CONTACT_LEFT_PADDLE = False
CONTACT_RIGHT_PADDLE = False
velo_x = 3
velo_y = 1
RADIUS = 10


def init_position():
    # baby blue
    set_clear_color(0.54, 0.81, 0.94)
    clear()

    # white
    set_fill_color(1, 1, 1)
    set_stroke_color(1, 1, 1)

    # drawing the initial circle
    draw_circle(BALL_X, BALL_Y, RADIUS)

    # initial position of left paddle
    set_stroke_color(1, 1, 1)
    set_fill_color(1, 1, 1)
    draw_rectangle(LEFT_PAD_X, LEFT_PAD_Y, PADDLE_WIDTH, PADDLE_HEIGHT)

    # initial position of the right paddle
    draw_rectangle(RIGHT_PAD_X, RIGHT_PAD_Y, PADDLE_WIDTH, PADDLE_HEIGHT)


def collision():
    global BALL_X, BALL_Y, velo_x, velo_y, CONTACT_VERT_WALL, \
        CONTACT_HOR_WALL, CONTACT_LEFT_PADDLE, CONTACT_RIGHT_PADDLE, \
        RADIUS, WINDOW_WIDTH, PADDLE_HEIGHT, PADDLE_WIDTH, \
        RIGHT_PAD_Y, LEFT_PAD_Y, space_pressed, \
        CONTACT_VERT_WALL

    # space pressed starts the game
    if space_pressed:
        BALL_X = BALL_X + velo_x
        BALL_Y = BALL_Y - velo_y

    # now creating checkpoints if the ball hits a paddle/wall
    if BALL_X - RADIUS <= PADDLE_WIDTH and LEFT_PAD_Y < BALL_Y < LEFT_PAD_Y + PADDLE_HEIGHT:
        CONTACT_LEFT_PADDLE = True

    if BALL_X + RADIUS >= WINDOW_WIDTH - PADDLE_WIDTH and RIGHT_PAD_Y < BALL_Y < RIGHT_PAD_Y + PADDLE_HEIGHT:
        CONTACT_RIGHT_PADDLE = True

    if BALL_Y - RADIUS < WINDOW_BASE or BALL_Y + RADIUS > WINDOW_WIDTH:
        CONTACT_HOR_WALL = True

    if BALL_X + RADIUS > WINDOW_WIDTH or BALL_X - RADIUS < WINDOW_LEFT_X:
        CONTACT_VERT_WALL = True

    if CONTACT_VERT_WALL:
        reset()

    if CONTACT_LEFT_PADDLE:
        velo_x = velo_x * -1

        BALL_X = BALL_X + 5 + velo_x # the 5 pixels added/subtracted to avoid "snaking"
        BALL_Y = BALL_Y - velo_y

        CONTACT_LEFT_PADDLE = False

    if CONTACT_RIGHT_PADDLE:
        velo_x = velo_x * -1

        BALL_X = BALL_X - 5 + velo_x  # the 5 pixels added/subtracted to avoid "snaking"
        BALL_Y = BALL_Y - velo_y

        CONTACT_RIGHT_PADDLE = False

    if CONTACT_HOR_WALL:
        velo_y = velo_y * -1
        BALL_Y = BALL_Y - velo_y

        CONTACT_HOR_WALL = False


# function for when the ball hits the vert. wall
def reset():
    global velo_x, velo_y, BALL_X, BALL_Y, RADIUS, INITIAL_BALL_X, \
        INITIAL_BALL_Y, space_pressed, CONTACT_VERT_WALL

    # setting the balls measurements back to initial values
    BALL_X = INITIAL_BALL_X
    BALL_Y = INITIAL_BALL_Y

    velo_x = INITIAL_VELO_X
    velo_y = INITIAL_VELO_Y

    space_pressed = False
    CONTACT_VERT_WALL = False


def keydown(key):
    global apressed, zpressed, kpressed, mpressed, space_pressed, qpressed

    if key == "a":
        apressed = True

    elif key == "z":
        zpressed = True

    elif key == "k":
        kpressed = True

    elif key == "m":
        mpressed = True

    elif key == " ":
        space_pressed = True

    elif key == "q":
        qpressed = True


# if a key is released, the paddle no longer moves
def keyup(key):
    global zpressed, apressed, kpressed, mpressed

    if key == "z":
        zpressed = False

    elif key == "a":
        apressed = False

    elif key == "k":
        kpressed = False

    elif key == "m":
        mpressed = False


# outlining behavior when certain keys are pressed
def when_pressed():
    global LEFT_PAD_Y, RIGHT_PAD_Y

    if zpressed and LEFT_PAD_Y <= WINDOW_WIDTH - PADDLE_HEIGHT:
        LEFT_PAD_Y += PADDLE_SPEED

    if apressed and LEFT_PAD_Y >= WINDOW_LEFT_X:
        LEFT_PAD_Y -= PADDLE_SPEED

    if mpressed and RIGHT_PAD_Y <= WINDOW_WIDTH - PADDLE_HEIGHT:
        RIGHT_PAD_Y += PADDLE_SPEED

    if kpressed and RIGHT_PAD_Y >= WINDOW_LEFT_X:
        RIGHT_PAD_Y -= PADDLE_SPEED

    if qpressed:
        cs1_quit()


# parent function being called by 'start_graphics'
def play_pong():

    init_position()

    when_pressed()

    collision()

start_graphics(play_pong, key_press=keydown, key_release=keyup)
