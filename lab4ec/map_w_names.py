# Author: Alexander Marcoux
# Date: 6 March 2023
# Purpose: drawing the dartmouth graph with the names of the vertices and animated bfs-- extra credit
from vertex import *
from load_graph import load_graph
from bfs import bfs

# window parameters
WINDOW_WIDTH = 1012
WINDOW_HEIGHT = 811

vertex_dict = load_graph("dartmouth_graph.txt")

# vertex constants
VERTEX_RAD = 7

# mouse variables
x = 0
y = 0
xm = 0
ym = 0
mouse_pressed = False

# initializing start and goal
start_vertex = None
goal_vertex = None


# tracking mouse movement
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

    # opening map and drawing background
    map = load_image("dartmouth_map.png")
    draw_image(map, 0, 0)

    # drawing all vertices and edges
    for location in vertex_dict:
        vertex_dict[location].draw_vertex(0, 0, 1)  # blue
        vertex_dict[location].draw_all_edges(0, 0, 1)

    # establishing start and goal vertices
    for location in vertex_dict:
        if vertex_dict[location].is_mouse_within(x, y):
            start_vertex = vertex_dict[location]
            start_vertex.draw_vertex(1, 0, 0)
            start_vertex.write_name(1, 0, 0)

        if start_vertex != None and vertex_dict[location].is_mouse_within(xm, ym):
            goal_vertex = vertex_dict[location]
            goal_vertex.draw_vertex(1, 0, 0)

    i = 0
    # if a start and goal have been chosen
    # animating the bfs by differentiating between vertices
    if start_vertex != None and goal_vertex != None:

        path = bfs(start_vertex, goal_vertex)

        while i < (len(path) - 1):
            path[i].draw_edge(path[i + 1], 0.1, 0.1, 0.1)
            path[i].draw_vertex(1, 1, 0)  # middle vertices = yellow
            path[i].write_name(1, 0, 0)
            i += 1

        start_vertex.draw_vertex(1, 1, 1)  # start vertex = white
        goal_vertex.draw_vertex(0, 1, 0)  # goal vertex = green


start_graphics(draw_map, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, mouse_press=clicked, mouse_move=mouse_move)