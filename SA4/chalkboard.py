# Author: Alexander Marcoux
# Date: 01/28/2023
# Embracing my inner picasso and drawing on a chalkboard

from cs1lib import *

# creating a function to draw lines from coords given by later funcs
def lines():
    global old_x, old_y, clear

    enable_stroke()
    set_stroke_color(r, g, b)
    set_stroke_width(2)
    draw_line(old_x, old_y, curr_x, curr_y)
    old_x = curr_x
    old_y = curr_y

def press(mx, my):
    # when mouse is pressed, the initial mouse coords are stored
    global draw, old_x, old_y
    old_x = mx
    old_y = my
    draw = True

def release(mx, my):
    global draw
    draw = False


def move(mx, my):
    # as mouse moves, new coordinates are stored
    global curr_x, curr_y
    curr_x = mx
    curr_y = my

# function for changing colors of chalk
def keydown(key):
    global r, g, b

    # red
    if key == "r":
        r = 1
        g = 0
        b = 0
    # blue
    elif key == "b":
        r = 0
        g = 0
        b = 1
    # green
    elif key == "g":
        r = 0
        g = 1
        b = 0
    # yellow
    elif key == "y":
        r = 1
        g = 1
        b = 0
    # white
    elif key == "w":
        r = 1
        g = 1
        b = 1
    # orange
    elif key == "o":
        r = 1
        g = 0.5
        b = 0

#the functionion to be called (combines the prev funcs)
def picasso():
    global background

    #calling the black background once then drawing the lines
    if background:
        set_clear_color(0, 0, 0)
        clear()

    if draw:
        background = False
        lines()

#starting values of white
r = 1
g = 1
b = 1
background = True
curr_x = 0
curr_y = 0
old_x = 0
old_y = 0
draw = False

start_graphics(picasso, mouse_move=move, mouse_press=press,
    mouse_release=release, key_press=keydown)