# Author: Alexander Marcoux
# Date: 6 March 2023
# Purpose: a game to learn the location of buildings on campus -- extra credit
from vertex import *
from load_graph import load_graph
from bfs import bfs
from random import randint
from math import *

# window parameters
WINDOW_WIDTH = 1012
WINDOW_HEIGHT = 811

vertex_dict = load_graph("dartmouth_graph.txt")

# vertex constant
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

# choosing a random vertex from the list of locations as the end goal
vertex_list = []
for vertex in vertex_dict:
    vertex_list.append(vertex)

r = randint(0, len(vertex_list) - 1)
end_name = vertex_list[r]

# arbitrarily chose kemeny and carson to calculate the approximate conversion rate (distance found using googlemaps)
# kemeny = 499, 333
# carson = 495, 413
p_dist = sqrt((499 - 495)**2 + (313 - 413)**2)
conversion_rate = 286 / p_dist  # ft per pixel

# func to calculate distance in ft btwn vertices
def calculate_distance(vertex, another_vertex):
    distance = sqrt((another_vertex.x - vertex.x)**2 + (another_vertex.y - vertex.y)**2)
    return int(distance * conversion_rate)  # now in ft


# tracking coordinates of mouse
def clicked(mx, my):
    global mouse_pressed, x, y
    mouse_pressed = True
    x = mx
    y = my

def mouse_move(x, y):
    global xm, ym
    xm = x
    ym = y

def released(x, y):
    global mouse_pressed
    mouse_pressed = False


# box containing instructions
def draw_end():
    enable_stroke()
    set_stroke_width(1)
    set_stroke_color(0, 0, 0) # Black
    set_fill_color(1, 0.8, 0)
    set_font_italic()

    draw_rectangle(20, 10, 340, 120)
    draw_text("Find and click '" + str(end_name) + "' on the map!", 40, 30)
    draw_text("Click any vertex to start.", 40, 60)
    draw_text("The path will be green when correct.", 40, 90)
    draw_text("Clicking the location will render a new goal.", 40, 120)

# main func
def draw_map():
    global start_vertex, goal_vertex, r, end_name

    # loading the background
    map = load_image("dartmouth_map.png")
    draw_image(map, 0, 0)

    # drawing all vertices
    for location in vertex_dict:
        vertex_dict[location].draw_vertex(0, 0, 1)
        vertex_dict[location].draw_all_edges(0, 0, 1)

    # establishing start and goal vertex
    for location in vertex_dict:
        if vertex_dict[location].is_mouse_within(x, y):
            start_vertex = vertex_dict[location]
            start_vertex.draw_vertex(1, 0, 0)

        if start_vertex != None and vertex_dict[location].is_mouse_within(xm, ym):
            goal_vertex = vertex_dict[location]
            goal_vertex.draw_vertex(1, 0, 0)

    # modifying end goal
    end_goal = vertex_dict[end_name]

    # choosing a random vertex as the end goal
    if mouse_pressed and end_goal.is_mouse_within(xm, ym):
        r = randint(0, len(vertex_list) - 1)
        end_name = vertex_list[r]

    i = 0
    # if a start and goal have been chosen
    if start_vertex != None and goal_vertex != None and goal_vertex != end_goal:
        # using bfs to draw edges reflecting the shortest path
        path = bfs(start_vertex, goal_vertex)

        while i < (len(path) - 1):
            path[i].draw_edge(path[i + 1], 1, 0, 0)  # red
            path[i].draw_vertex(1, 0, 0)
            i += 1

    # calling bfs twice to check the path of the end goal
    t = 0
    if start_vertex != None and goal_vertex != None and goal_vertex == end_goal:

        path = bfs(start_vertex, end_goal)
        start_vertex.draw_vertex(0, 1, 0)

        # if end goal is reached, vertices and edges are green, signifying correct
        while t < (len(path) - 1):
            path[t].draw_edge(path[t + 1], 0, 1, 0)
            path[t].draw_vertex(0, 1, 0)
            t += 1

    # if end goal is pressed, new goal is generated and printed
    if mouse_pressed and end_goal.is_mouse_within(xm, ym):
        r = randint(0, len(vertex_list) - 1)
        end_name = vertex_list[r]

    draw_end()

    # drawing bow to contain distance calculated
    if start_vertex != None:
        enable_stroke()
        set_stroke_width(1)
        set_stroke_color(0, 0, 0)  # Black
        set_fill_color(1, 0.8, 0)
        set_font_italic()

        draw_rectangle(5, 780, 485, 20)
        draw_text("The distance between " + str(start_vertex.name) + " and " + str(end_name) + " is ~" + str(
        calculate_distance(start_vertex, end_goal)) + " feet", 7, 795)


start_graphics(draw_map, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, mouse_press=clicked, mouse_release=released, mouse_move=mouse_move)