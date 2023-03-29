# Author: Alexander Marcoux
# Date: 8 March 2023
# Purpose: plotting the dartmouth graph for lab 4
from vertex import *
from load_graph import load_graph
from bfs import bfs

# window parameters
WINDOW_WIDTH = 1012
WINDOW_HEIGHT = 811

# creating a dictionary
vertex_dict = load_graph("dartmouth_graph.txt")

# radius constant
VERTEX_RAD = 7

# mouse variables
x = 0
y = 0
xm = 0
ym = 0
mouse_pressed = False

# initializing start and goal vertex
start_vertex = None
goal_vertex = None


# tracking the coordinates of the mouse
def clicked(mx, my):
    global mouse_pressed, x, y
    mouse_pressed = True
    x = mx
    y = my


def mouse_move(x, y):
    global xm, ym
    xm = x
    ym = y


# main func
def draw_map():
    global start_vertex, goal_vertex, i

    # loading the map
    map = load_image("dartmouth_map.png")
    draw_image(map, 0, 0)

    # drawing each vertex
    for location in vertex_dict:
        vertex_dict[location].draw_vertex(0, 0, 1)  # blue
        vertex_dict[location].draw_all_edges(0, 0, 1)

    # initializing a start vertex and goal vertex (in red)
    for location in vertex_dict:
        if vertex_dict[location].is_mouse_within(x, y):
            start_vertex = vertex_dict[location]
            start_vertex.draw_vertex(1, 0, 0)  # red

        # using pythons built in mouse funcs to retrieve coordinates
        if start_vertex != None and vertex_dict[location].is_mouse_within(xm, ym):
            goal_vertex = vertex_dict[location]
            goal_vertex.draw_vertex(1, 0, 0)

    # if a start and goal have been chosen
    # bfs func to draw the edges between goal and start (in red)
    i = 0
    if start_vertex != None and goal_vertex != None:

        path = bfs(start_vertex, goal_vertex)

        # end of path will be the goal, beginning will be the start
        while i < (len(path) - 1):
            path[i].draw_edge(path[i + 1], 1, 0, 0)  # red
            path[i].draw_vertex(1, 0, 0)
            i += 1


start_graphics(draw_map, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, mouse_press=clicked, mouse_move=mouse_move)