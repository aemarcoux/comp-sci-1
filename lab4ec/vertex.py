# Author: Alexander Marcoux
# Date: 8 March 2023
# Purpose: vertex class for lab 4 extra credit
from cs1lib import *

# vertex constants
VERTEX_RAD = 7
EDGE_WIDTH = 3


class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.adj_list = []
        self.rad = VERTEX_RAD

    def __str__(self):
        adjacent_names = self.adj_list[0].name

        for vertex in self.adj_list:
            if vertex != self.adj_list[0]:
                # concatenating a string of adjacent vertex names
                adjacent_names = adjacent_names + ", " + vertex.name

        # returning the data in the form: "name; Location: x, y; Adjacent vertices: adjacent names"
        return self.name + "; Location: " + str(self.x) + ", " + str(self.y) + "; " + "Adjacent vertices: " + str(adjacent_names)

    def draw_vertex(self, r, g, b):
        disable_stroke()
        set_fill_color(r, g, b)

        draw_circle(self.x, self.y, self.rad)

    # used to draw one edge between two vertices
    def draw_edge(self, another_vertex, r, g, b):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_stroke_width(EDGE_WIDTH)

        draw_line(self.x, self.y, another_vertex.x, another_vertex.y)

    # used to draw edges between a vertex and all adjacent vertices
    def draw_all_edges(self, r, g, b):
        for vertex in self.adj_list:
            self.draw_edge(vertex, r, g, b)

    # checking if the mouse is withing the boundaries of a vertex
    def is_mouse_within(self, x, y):
        if self.x - VERTEX_RAD <= x <= self.x + VERTEX_RAD and self.y - VERTEX_RAD <= y <= self.y + VERTEX_RAD:
            return True
        else:
            return False

    # writing the name of each vertex
    def write_name(self, r, g, b):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_font_size(16)
        set_font_normal()

        draw_text(str(self.name), self.x + 10, self.y - 10)
