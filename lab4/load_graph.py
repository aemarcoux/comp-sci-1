# Author: Alexander Marcoux
# Date: 8 March 2023
# Purpose: load graph function for lab 4
from vertex import Vertex


def load_graph(filename):
    # initializing vertex dictionary
    vertex_dict = {}

    # opening list of dartmouth buildings
    dartmouth_graph = open(filename, "r")

    for line in dartmouth_graph:
        # splitting the info into components separated by ";"
        wlist = line.split(";")
        vertex_name = wlist[0].strip()

        # the coordinates are the last component when split
        coords = wlist[2].split(",")

        # storing x and y coordinates
        vx = coords[0].strip()
        vy = coords[1].strip()

        # passing in an empty list
        v = Vertex(vertex_name, vx, vy)
        vertex_dict[vertex_name] = v

    # closing the file
    dartmouth_graph.close()

    # opening the file again
    dartmouth_graph = open(filename, "r")

    for line in dartmouth_graph:
        wlist = line.split(";")
        vertex_name = wlist[0].strip()
        # getting the adjacent vertices to add to adj_list
        adj_name_list = wlist[1].split(",")

        # Remove white space and "\n"
        for i in range(len(adj_name_list)):
            adj_name_list[i] = adj_name_list[i].strip()

        # initializing an empty list
        adj_list = []

        for name in adj_name_list:
            adj_v = vertex_dict[name]
            adj_list.append(adj_v)

        # storing the dictionary values in keys
        curr_v = vertex_dict[vertex_name]
        curr_v.adj_list = adj_list

    # closing the file
    dartmouth_graph.close()

    return vertex_dict

load_graph("dartmouth_graph.txt")


