# Author: Alexander Marcoux
# Date: 2 March 2023
# Purpose: adventure class for my story

from vertex import Vertex


def parse_line(line):
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    text = section_split[2].strip()

    return vertex_name, adjacent, text


def load_story(filename):

    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:

        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)

            # print("vertex " + vertex_name)
            # print(" adjacent:  " + str(adjacent_vertices))
            # print(" text:  " + text)

        # using the Vertex class
        vertex_dict[vertex_name] = Vertex(vertex_name, adjacent_vertices, text)
        vertex_dict[vertex_name].adjacent_vertices = adjacent_vertices

    file.close()

    return vertex_dict


# loading the story from the txt file
story_dict = load_story("story.txt")


# creating a function to play the game
def playing(vertex_dict):

    # starts at the first vertex given
    current = vertex_dict['START']

    # if there is a choice
    while len(current.adjacent_vertices) != 0:
        print(current.text)

        # prompting the using with a choice and converting that letter into a numeric value
        choice = input("Which path will you choose?: ")
        choice = ord(choice) - ord("a")

        # if the choice is within the parameters/options, else will prompt the user to re-enter a choice
        if choice < len(current.adjacent_vertices):
            new = current.adjacent_vertices[choice]
            current = vertex_dict[new]
        else:
            print("invalid input")

    print(current.text)
    return


# calling the playing func
playing(story_dict)