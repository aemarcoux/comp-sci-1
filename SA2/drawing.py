# Author: Alexander Marcoux
# Date: 1/13/2023
# Purpose: illustrating/recreating the "corduroy" children's book cover

from cs1lib import *

# the variables "x, y, and radius" will be used for the remainder of
# the code as reference points. Specifically, these coordinates
# are the center coordinates for the bear's head
x = 200
y = 150
radius = 30
title = "Corduroy"
name = "By Alexander Marcoux"

# the following is a series of functions that set the stroke/fill in certain colors
def set_fill_light_brown():
    set_fill_color(0.73, 0.6, 0.48)

# wood/coffee color
def set_fill_body():
    set_fill_color(0.64, 0.45, 0.28)

# slightly darker brown
def set_stroke_shell():
    set_stroke_color(0.43, 0.30, 0.22)

def set_fill_red():
    set_fill_color(0.80, 0, 0)

def set_fill_forest_green():
    set_fill_color(0, 0.56, 0.28)

def set_stroke_forest_green():
    set_stroke_color(0, 0.56, 0.28)

def set_stroke_yellow():
    set_stroke_color(1, 1, 0)

def set_fill_yellow():
    set_fill_color(1, 1, 0)

def set_stroke_black():
    set_stroke_color(0, 0, 0)

def set_fill_black():
    set_fill_color(0, 0, 0)

def set_fill_white():
    set_fill_color(1, 1, 1)

def set_background_red():
    set_clear_color(0.80, 0, 0)
    clear()

# the following functions draw different aspects of the final cover
def draw_button(x, y, radius):
    set_stroke_black()
    set_fill_white()
    draw_circle(x, y, radius)

def draw_background():
    set_background_red()

    # adding the black lines and button to the background
    set_stroke_black()
    set_fill_red()
    set_stroke_width(2)
    draw_ellipse(x - 100, y + 200, radius * 5, radius * 3)
    draw_ellipse(x + 100, y + 190, radius * 5, radius * 3)
    disable_stroke()
    # covering bottom section of ellipses with red rectangle
    draw_rectangle(x - 200, y + 150, 400, 100)

    # adding button to background
    enable_stroke()
    set_stroke_black()
    set_stroke_width(1)
    back_button_radius = radius // 4
    draw_button(x + 75, y + 150, back_button_radius)

def draw_eye(x, y, radius):

    # white circle
    set_stroke_black()
    set_stroke_width(1)
    set_fill_white()
    draw_circle(x, y, radius)

    # black circle
    black_radius = radius / 1.3
    set_fill_black()
    draw_circle(x + 1, y + 2, black_radius)

def draw_overalls():
    set_stroke_black()
    set_fill_forest_green()

    # top half of overalls
    draw_polygon([[x - 46, y + 65], [x + 28, y + 65], [x + 23, y + 100], [x - 48, y + 100]])

    # bottom half of overalls
    draw_polygon([[x - 48, y + 100], [x + 23, y + 100], [x + 20, y + 150], [x - 45, y + 150]])

    # forest green line on the intersection between the halves
    set_stroke_forest_green()
    set_stroke_width(3)
    draw_line(x - 46, y + 100, x + 21, y + 100)

    # lines to separate legs
    set_stroke_black()
    set_stroke_width(1)
    draw_line(x - 10, y + 150, x - 13, y + 110)
    draw_line(x - 11, y + 145, x - 7, y + 105)

    # right strap (can only include right as the left strap must go over the left arm
    # can find "left strap" in body of draw_cover
    draw_polygon([[x + 8, y + 75], [x + 18, y + 75], [x + 20, y + 32], [x + 10, y + 32]])
    button_radius = radius / 9
    draw_button(x + 13, y + 68, button_radius)

def draw_head():
    # adding the right ear
    enable_stroke()
    set_fill_body()
    set_stroke_shell()
    draw_ellipse(x + 25, y - 10, radius - 5, radius - 10)

    # adding inner-ear
    set_fill_light_brown()
    draw_ellipse(x + 25, y - 10, radius - 10, radius - 15)

    # adding the left ear
    set_fill_body()
    set_stroke_shell()
    draw_ellipse(x - 19, y - 12, radius - 7, radius - 5)

    # adding the inner-ear
    set_fill_light_brown()
    draw_ellipse(x - 19, y - 12, radius - 12, radius - 10)

    # making the head
    set_fill_body()
    enable_stroke()
    set_stroke_shell()
    draw_ellipse(x, y, radius + 5, radius + 3)

    # adding the left eye
    lx = int(x - 5)
    ly = int(y)
    eye_size = int(radius * 0.2)
    draw_eye(lx, ly, eye_size)

    # adding the right eye
    rx = int(x + 20)
    ry = int(y + 3)
    eye_size = int(radius * 0.2)
    draw_eye(rx, ry, eye_size)

    # adding the mouth/nose
    set_stroke_shell()
    set_fill_light_brown()
    draw_ellipse(x + 8, y + 23, radius * 0.5, radius * 0.4)

    # lines for the mouth
    set_stroke_black()
    draw_line(x - 1, y + 25, x + 13, y + 28)
    draw_line(x + 13, y + 28, x + 20, y + 25)
    draw_line(x + 13, y + 28, x + 11, y + 22)

    # nose connected to mouth
    set_fill_black()
    draw_triangle(x + 11, y + 21, x + 5, y + 16, x + 16, y + 16)

def draw_cover():
    # adding the background
    draw_background()

    # adding the right arm
    disable_stroke()
    set_fill_body()
    draw_polygon([[x + 18, y + 35], [x + 23, y + 65], [x + 45, y + 80], [x + 45, y + 55]])
    draw_polygon([[x + 45, y + 55], [x + 45, y + 80], [x + 65, y + 85], [x + 65, y + 65]])
    draw_ellipse(x + 65, y + 75, radius * 0.2, radius * 0.3)

    # adding the body
    set_fill_body()
    enable_stroke()
    set_stroke_shell()
    draw_ellipse(x - 12, y + 75, radius * 1.3, radius * 2)

    # adding the feet
    set_stroke_shell()
    set_fill_body()
    draw_ellipse(x + 3, y + 153, radius / 1.8, radius / 2.5)
    draw_ellipse(x - 27, y + 155, radius / 1.8, radius / 2.5)

    # adding the overalls (minus the left strap)
    draw_overalls()

    # adding the left arm
    disable_stroke()
    set_fill_body()
    draw_polygon([[x - 30, y + 20], [x - 30, y + 50], [x - 50, y + 60], [x - 50, y + 35]])
    draw_ellipse(x - 47, y + 65, radius * 0.5, radius)

    # left strap on overalls to go over the left arm
    enable_stroke()
    set_stroke_black()
    set_fill_forest_green()
    draw_polygon([[x - 20, y + 50], [x - 30, y + 50], [x - 38, y + 24], [x - 28, y + 20]])
    draw_line(x - 27, y + 40, x - 26, y + 44)

    # adding the head
    draw_head()

    # writing title - "corduroy"
    set_font_normal()
    set_font("Palatino")
    set_font_size(80)
    set_stroke_yellow()
    set_fill_yellow()
    draw_text(title, x - 175, y - 70)

    # writing my name
    set_font_italic()
    set_font_size(16)
    set_stroke_black()
    draw_text(name, x + 40, y + 230)

start_graphics(draw_cover)




