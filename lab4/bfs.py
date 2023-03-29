# Author: Alexander Marcoux
# Date: 8 March 2023
# Purpose: bfs class for lab 4
from collections import *


def bfs(start_vertex, goal_vertex):
    # initializing an empty dict to hold backpointers
    backpointer = {}
    # initialize the frontier queue
    frontier = deque([start_vertex])
    # adding start vertex key to backpointer with a value of None
    backpointer[start_vertex] = None

    # while frontier is not empty
    while len(frontier) != 0:
        # removing and storing the first vertex
        x = frontier.popleft()

        # checking the adjacent vertices
        for adj_v in x.adj_list:
            # if adj_v has not been visited, add to backpointer dict and frontier
            if adj_v not in backpointer:
                frontier.append(adj_v)
                backpointer[adj_v] = x

        # if our goal has been visited, break
        if goal_vertex in backpointer:
            break

    # when we select goal, initialize an empty path
    goal_val = goal_vertex
    path = []

    while goal_val != None:
        # append to the empty path
        path.append(goal_val)
        goal_val = backpointer[goal_val]

    # return the path list
    return path
