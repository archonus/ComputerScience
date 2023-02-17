from __future__ import annotations
from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass
from math import inf
from typing import List

class Graph(ABC):

    @property
    @abstractmethod
    def vertices(self):
        pass

    @abstractmethod
    def add_edge(self, vertex_from, vertex_to,weight):
        pass

    @abstractmethod
    def add_vertex(self, name):
        pass
    
    @abstractmethod
    def update_edge(self,vertex_from, vertex_to, weight):
        pass

    @abstractmethod
    def get_edge_weight(self, vertex_from, vertex_to):
        pass

    @abstractmethod
    def check_connected(self, vertex_from, vertex_to):
        pass

    def get_connected_vertices(self, vertex) -> List:
        connected = []
        n = len(self.vertices)
        for i in range(n):
            vertex_to = self.vertices[i]
            if self.check_connected(vertex,vertex_to):
                connected.append(vertex_to)            
        return connected

    def depth_first_traverse(self, start = None):
        if start is None:
            start = self.vertices[0]
        visited = [] # Should use set?
        stack = deque()
        stack.append(start)
        while len(stack) > 0:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
            for node in self.get_connected_vertices(current):
                if node not in visited:
                    stack.append(node)
        
        return visited

    def breadth_first_traverse(self, start = None):
        if start is None:
            start = self.vertices[0]
        visited = []
        queue = deque()
        queue.append(start)
        while len(queue) > 0:
            current = queue.popleft()
            if current not in visited:
                visited.append(current)
            for node in self.get_connected_vertices(current):
                if node not in visited:
                    queue.append(node)

        return visited

    def djikstra(self, start= None):
        if start is None:
            start = self.vertices[0]
        distances = {v : inf for v in self.vertices}
        back = {v : "" for v in self.vertices}
        distances[start] = 0
        visited = []
        queue = []
        queue.append(start)
        while len(queue) > 0:
            queue.sort(key= lambda v : distances[v])
            current = queue.pop(0) # Remove first item
            if current not in visited:
                visited.append(current)
            for v in self.get_connected_vertices(current):
                if v not in visited:
                    queue.append(v)
                    new_distance = distances[current] + self.get_edge_weight(current, v) # Check distance
                    if new_distance < distances[v]:
                        distances[v] = new_distance
                        back[v] = current # The new shortest distance and how to get there

        return distances, back



@dataclass
class Edge:
    to : str
    weight : int = 1

class AdjacencyListGraph(Graph):
    # Actually uses a dictionary instead of list

    def __init__(self, adj_list = None, vertices = None, directed = True):
        if adj_list:
            self.adj_list = adj_list
        elif vertices: # Nodes defined, but no edges
            self.adj_list = {k : [] for k in vertices}
        else: # Empty graph
            self.adj_list = {}
        self.directed = directed
    
    @property
    def vertices(self):
        return list(self.adj_list) # List of keys

    def add_vertex(self, name):
        if name not in self.adj_list:
            self.adj_list[name] = []
    
    def add_edge(self, vertex_from, vertex_to, weight = 1):
        self._add_edge(vertex_from,vertex_to,weight)
        if not self.directed:
            self._add_edge(vertex_to,vertex_from,weight) # Add an edge back again as well
            
    def _add_edge(self, vertex_from, vertex_to, weight):
        if self._get_edge(vertex_from,vertex_to):
            raise ValueError("Edge already exists")
        else:
            edge = Edge(vertex_to, weight)
            self.adj_list[vertex_from].append(edge)

    def _get_edge(self, vertex_from, vertex_to) -> Edge:
        edges = self.adj_list[vertex_from]
        for edge in edges:
            if edge.to == vertex_to:
                return edge
        return None

    def update_edge(self,vertex_from, vertext_to, weight):
        edge = self._get_edge(vertex_from,vertext_to)
        if edge: 
            edge.weight = weight
        else:
            raise ValueError("Edge does not exist")
        if not self.directed: # Change other way as well
            edge = self._get_edge(vertext_to, vertex_from)
            if edge: 
                edge.weight = weight
            else:
                raise ValueError("Edge does not exist")

    def get_edge_weight(self, vertex_from, vertex_to):
        edge = self._get_edge(vertex_from,vertex_to)
        if edge: 
            return edge.weight
        else: 
            raise ValueError("Edge does not exist")

    def check_connected(self, vertex_from, vertex_to):
        return self._get_edge(vertex_from,vertex_to) is not None

    def to_adj_matrix(self, directed = True) -> AdjacencyMatrixGraph:
        g = AdjacencyMatrixGraph(vertices=self.vertices, directed=directed)
        for vertex in self.adj_list:
            for edge in self.adj_list[vertex]:
                g.add_edge(vertex, edge.to, edge.weight)
        return g

    def depth_first_traverse(self, start = None):
        if start is None:
            start = self.vertices[0]
        visited = []
        self._recursive_depth_first(start, visited)
        return visited

    def _recursive_depth_first(self, current, visited):
        visited.append(current)
        for edge in self.adj_list[current]: # Checks all the edges from the current node
            if edge.to not in visited:
                self._recursive_depth_first(edge.to, visited)



class AdjacencyMatrixGraph(Graph):
    def __init__(self, vertices : List = None, adj_matrix = None, directed = True):
        self._vertices = vertices[:] if vertices else [] # Should really be a deep copy
        n = len(self._vertices)
        self.directed = directed
        if adj_matrix is not None:
            self.adj_matrix = adj_matrix
        elif directed:
            self.adj_matrix = [[0 for i in range(n)] for j in range(n)]
        else: # Undirected uses less space
            if n <= 1:
                self.adj_matrix = []
            else:
                self.adj_matrix = [[0 for i in range(n - j - 1)] for j in range(n)]

    @property
    def vertices(self):
        return self._vertices
    
    def add_edge(self, vertex_from, vertex_to, weight = 1):
        self.update_edge(vertex_from,vertex_to,weight)

    def add_vertex(self,name):
        if name in self._vertices:
            raise ValueError("Vertex already exists")
        self._vertices.append(name)
        for row in self.adj_matrix:
            row.append(0) # Add another entry to each row (add a column) 
        if self.directed:  
            self.adj_matrix.append([0 for i in range(len(self._vertices))])
        else:
            self.adj_matrix.append([])

    def add_vertices(self, *args):
        for name in args:
            self.add_vertex(name)

    def update_edge(self, vertex_from, vertex_to, weight):
        i, j = self._get_edge_indices(vertex_from,vertex_to)
        self.adj_matrix[i][j] = weight

    def get_edge_weight(self, vertex_from, vertex_to):
        i, j = self._get_edge_indices(vertex_from, vertex_to)
        return self.adj_matrix[i][j]

    def _get_edge_indices(self, vertex_from, vertex_to):
            """Returns a tuple identifying the edge between vertex_from and vertex_to"""
            index_from = self._vertices.index(vertex_from)
            index_to = self._vertices.index(vertex_to)
            if self.directed:
                return index_from, index_to
            else:
                if index_from == index_to:
                    raise ValueError("Vertex cannot be connected to itself in undirected graph")
                elif index_from < index_to:
                    return index_from, index_to - index_from - 1 # -1 because of zero-indexing
                else:
                    return index_to, index_from - index_to - 1

    def check_connected(self, vertex_from, vertex_to):
        try:
            connected = self.get_edge_weight(vertex_from,vertex_to) != 0
        except ValueError:
            connected = False
        return connected

    def to_adj_list(self, directed = True) -> AdjacencyListGraph:
        g = AdjacencyListGraph(vertices=self._vertices, directed=directed)
        n = len(self._vertices)
        for i in range(n): # Iterate through all the vertices
            vertex_from = self._vertices[i]
            if self.directed:
                for j in range(n):
                    if self.adj_matrix[i][j] != 0:
                        vertex_to = self._vertices[j]
                        g.add_edge(vertex_from,vertex_to, self.adj_matrix[i][j])
            else: # Undirected graph
                for j in range(n - i - 1): # Reduced number of iterations
                    if self.adj_matrix[i][j] != 0:
                        vertex_to = self._vertices[i + j + 1]
                        g.add_edge(vertex_from,vertex_to, self.adj_matrix[i][j])
        return g


if __name__ == "__main__":

    # g = AdjacencyListGraph(vertices = ["A","B","C","D"])
    # print(g.adj_list)
    # g.add_edge("A","B")
    # g.add_edge("A","C")
    # g.add_vertex("E")
    # g.add_edge("B","E")
    # g.add_edge("E","C")
    # g.update_edge("A","B",2)
    # print(g.adj_list)

    g = AdjacencyMatrixGraph(vertices=["A","B","C","D","E"], directed=False)
    g.add_edge("A","B",7)
    g.add_edge("A","D",3)
    g.add_edge("B","D",2)
    g.add_edge("B","C",3)
    g.add_edge("C","E",1)
    g.add_edge("C","D",4)
    g.add_edge("E","D",7)
    g.add_edge("B","E",6)
    print(g.depth_first_traverse())
    print(g.djikstra())