# Author: Alexander Marcoux
# Date: 3 March 2023
# Purpose: vertex class for SA8

class Vertex:
    def __init__(self, vertex_name, adjacent_vertices, text):
        self.vertex_name = vertex_name
        self.adjacent_vertices = adjacent_vertices
        self.text = text

