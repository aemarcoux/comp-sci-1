# Author: Alexander Marcoux
# Date: 4 February 2023
# Purpose: Extra-Credit Version of Pong
from cs1lib import *
from random import randint

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
score = 0



# constants for the title screen
PLAY_WINDOW_LEFT_X = 80
PLAY_WINDOW_RIGHT_X = 200
PLAY_WINDOW_TOP_Y = 150
PLAY_WINDOW_LOW_Y = 250
growing = True
sz = 24
m_pressed = False


def title_screen():
    global sz, growing, m_pressed

    set_clear_color(0.54, 0.81, 0.94) # baby blue
    clear()

    set_font("Palatino")
    set_font_size(48)
    set_stroke_color(1, 0, 0) # red
    draw_text("PONG.", 125, 150)

    # white circle to look like a ping pong ball
    set_stroke_color(1, 1, 1) # white
    set_fill_color(1, 1, 1)
    draw_circle(172, 133, 19)

    # pulsing 'play'
    if growing:
        sz = sz + 1
    else:
        sz = sz - 1

    set_stroke_color(1, 0, 0) # red
    set_font_size(24)
    draw_text("Click", 30, 220)

    set_font_italic()
    set_font_size(sz)
    draw_text("PLAY", 95, 220)

    set_font_normal()
    set_font_size(24)
    draw_text("to start the game!", 180, 220)

    set_font_size(16)
    draw_text("When in game, hit SPACEBAR to begin.", 55, 350)
    draw_text("Player 1: use 'a' and 'z' to move.", 90, 370)
    draw_text("Player 2: use 'k' and 'm' to move.", 90, 390)

    if sz >= 30 or sz <= 16:
        growing = not growing

def cloud_and_sun():

    set_stroke_color(1, 1, 1) # white
    set_fill_color(1, 1, 1)

    # cloud 1 (series of three ellipses with similar coords)
    draw_ellipse(95, 100, 40, 20)
    draw_ellipse(120, 80, 40, 20)
    draw_ellipse(150, 102, 40, 20)

    # cloud 2
    draw_ellipse(245, 200, 40, 20)
    draw_ellipse(270, 180, 40, 20)
    draw_ellipse(300, 202, 40, 20)

    # cloud 3
    draw_ellipse(145, 300, 40, 20)
    draw_ellipse(170, 280, 40, 20)
    draw_ellipse(200, 302, 40, 20)

    # sun
    set_stroke_color(1, 1, 0) # yellow
    set_fill_color(1, 1, 0)
    draw_circle(290, 0, 50)

def init_position():
    # baby blue
    set_clear_color(0.54, 0.81, 0.94) #baby blue
    clear()

    cloud_and_sun()

    set_fill_color(1, 0, 0) # red
    set_stroke_color(1, 0, 0)

    draw_circle(BALL_X, BALL_Y, RADIUS)

    # initial position of left paddle
    set_stroke_color(1, 1, 1) # white
    set_fill_color(1, 1, 1)
    draw_rectangle(LEFT_PAD_X, LEFT_PAD_Y, PADDLE_WIDTH, PADDLE_HEIGHT)

    # initial position of the right paddle
    draw_rectangle(RIGHT_PAD_X, RIGHT_PAD_Y, PADDLE_WIDTH, PADDLE_HEIGHT)

    # adding the score to the top of the screen
    set_font("Palatino")
    set_font_size(24)
    set_stroke_color(1, 0, 0)
    draw_text(str(score), 190, 30)

def collision():
    global BALL_X, BALL_Y, velo_x, velo_y, CONTACT_VERT_WALL, \
        CONTACT_HOR_WALL, CONTACT_LEFT_PADDLE, CONTACT_RIGHT_PADDLE, \
        RADIUS, WINDOW_WIDTH, PADDLE_HEIGHT, PADDLE_WIDTH, \
        RIGHT_PAD_Y, LEFT_PAD_Y, space_pressed, \
        CONTACT_VERT_WALL, score

    # space_pressed starts the movement of the ball
    if space_pressed:
        BALL_X = BALL_X + velo_x
        BALL_Y = BALL_Y - velo_y

    # series of checks for contact will wall/paddle
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

        if -8 < velo_x < 8:
            velo_x = velo_x * 1.1

        if -3 < velo_y < 3:
            velo_y = velo_y * 1.1

        BALL_X = BALL_X + 5 + velo_x # the 5 pixels added/subtracted to avoid "snaking"
        BALL_Y = BALL_Y - velo_y
        score = score + 1
        CONTACT_LEFT_PADDLE = False

    if CONTACT_RIGHT_PADDLE:
        velo_x = velo_x * -1

        if -8 < velo_x < 8:
            velo_x = velo_x * 1.1

        if -3 < velo_y < 3:
            velo_y = velo_y * 1.1

        BALL_X = BALL_X - 5 + velo_x # the 5 pixels added/subtracted to avoid "snaking"
        BALL_Y = BALL_Y - velo_y
        score = score + 1
        CONTACT_RIGHT_PADDLE = False

    if CONTACT_HOR_WALL:
        velo_y = velo_y * -1
        BALL_Y = BALL_Y - velo_y
        CONTACT_HOR_WALL = False

# function for when ball misses paddle
def reset():
    global velo_x, velo_y, BALL_X, BALL_Y, RADIUS, INITIAL_BALL_X, \
        INITIAL_BALL_Y, space_pressed, score, CONTACT_VERT_WALL, \
        INITIAL_VELO_X, INITIAL_VELO_Y

    BALL_X = INITIAL_BALL_X
    BALL_Y = INITIAL_BALL_Y
    score = 0

    # randomizes the direction of the ball after the game is over
    which_direction = randint(1, 4)
    if which_direction == 1:
        velo_x = INITIAL_VELO_X
        velo_y = INITIAL_VELO_Y
    elif which_direction == 2:
        velo_x = INITIAL_VELO_X
        velo_y = INITIAL_VELO_Y * -1
    elif which_direction == 3:
        velo_x = INITIAL_VELO_X * -1
        velo_y = INITIAL_VELO_Y
    else:
        velo_x = INITIAL_VELO_X * -1
        velo_y = INITIAL_VELO_Y * -1

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

# if a different key is released, the paddle no longer moves
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

def clicked(mx, my):
    global m_pressed

    if PLAY_WINDOW_LEFT_X <= mx <= PLAY_WINDOW_RIGHT_X and PLAY_WINDOW_TOP_Y <= my <= PLAY_WINDOW_LOW_Y:
        m_pressed = True
    else:
        m_pressed = False

# function for behavior when a certain key is pressed
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

def play_pong():
    global LEFT_PAD_Y, RIGHT_PAD_Y

    init_position()
    
    when_pressed()

    collision()

# final function to be called by start_graphics
def final_pong():
    title_screen()

    if m_pressed:
        clear()
        play_pong()

start_graphics(final_pong, key_press=keydown, key_release=keyup, mouse_press=clicked)