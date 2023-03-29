# Author: Alexander Marcoux
# Date: 20 February 2023
# Purpose: Solar System Extra Credit Body class
from cs1lib import *


class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b, file):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b
        self.pic = load_image(file)

    def update_position(self, timestep):
        # time step provided by driver (time between each frame)
        self.x = self.x + self.vx * timestep
        self.y = self.y + self.vy * timestep

    def update_velocity(self, ax, ay, timestep):
        self.vx = self.vx + ax * timestep
        self.vy = self.vy + ay * timestep

    def draw(self, cx, cy, pixels_per_meter):
        # note: measurements will be converted into pixels
        set_fill_color(self.r, self.g, self.b)
        # drawing planet shape
        draw_circle(self.x * pixels_per_meter + cx, self.y * pixels_per_meter + cy, self.pixel_radius)
        # adding real image of planet
        draw_image(self.pic, self.x * pixels_per_meter + cx - self.pixel_radius, self.y * pixels_per_meter + cy - self.pixel_radius)