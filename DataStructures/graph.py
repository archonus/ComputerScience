from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

class Graph(ABC):

    @abstractmethod
    def add_edge(self, vertex_from, vertex_to,weight):
        pass

    @abstractmethod
    def add_vertex(self, name):
        pass
    
    @abstractmethod
    def update_edge(self,vertex_from, vertext_to, weight):
        pass

    @abstractmethod
    def get_edge_weight(self, vertex_from, vertex_to):
        pass

    @abstractmethod
    def check_connected(self, vertex_from, vertex_to):
        pass

class AdjacencyListGraph(Graph):
    # Actually uses a dictionary instead of list
    @dataclass
    class Edge:
        to : str
        weight : int = 1

    def __init__(self, adj_list = None, vertices = None):
        if adj_list:
            self.adj_list = adj_list
        elif vertices: # Nodes defined, but no edges
            self.adj_list = {k : [] for k in vertices}
        else: # Empty graph
            self.adj_list = {}
    
    @property
    def vertices(self):
        return list(self.adj_list)

    def add_vertex(self, name):
        if name not in self.adj_list:
            self.adj_list[name] = []
    
    def add_edge(self, vertex_from, vertex_to, weight = 1):
        edges = self.adj_list[vertex_from]
        if self._get_edge(vertex_from,vertex_to):
            raise ValueError("Edge already exists")
        else:
            edge = AdjacencyListGraph.Edge(vertex_to, weight)
            edges.append(edge)

    def _get_edge(self, vertex_from, vertex_to):
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

    def get_edge_weight(self, vertex_from, vertext_to):
        edge = self._get_edge(vertex_from,vertext_to)
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


class AdjacencyMatrixGraph(Graph):
    def __init__(self, vertices : List = None, adj_matrix = None, directed = True):
        self.vertices = vertices[:] if vertices else [] # Should really be a deep copy
        n = len(self.vertices)
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
    
    def add_edge(self, vertex_from, vertex_to, weight = 1):
        self.update_edge(vertex_from,vertex_to,weight)

    def add_vertex(self,name):
        if name in self.vertices:
            raise ValueError("Vertex already exists")
        self.vertices.append(name)
        for row in self.adj_matrix:
            row.append(0) # Add another entry to each row (add a column) 
        if self.directed:  
            self.adj_matrix.append([0 for i in range(len(self.vertices))])
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
            index_from = self.vertices.index(vertex_from)
            index_to = self.vertices.index(vertex_to)
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
        return self.get_edge_weight(vertex_from,vertex_to) != 0

    def to_adj_list(self) -> AdjacencyListGraph:
        g = AdjacencyListGraph(vertices=self.vertices)
        n = len(self.vertices)
        for i in range(n): # Iterate through all the vertices
            vertex_from = self.vertices[i]
            if self.directed:
                for j in range(n):
                    if self.adj_matrix[i][j] != 0:
                        vertex_to = self.vertices[j]
                        g.add_edge(vertex_from,vertex_to, self.adj_matrix[i][j])
            else: # Undirected graph
                for j in range(n - i): # Reduced number of iterations
                    if self.adj_matrix[i][j] != 0:
                        vertex_to = self.vertices[i + j + 1]
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

    g = AdjacencyMatrixGraph(vertices=["A","B","C","D"], directed=True)
    g.add_edge("A","B")
    g.add_edge("C","A")
    g.add_edge("D","C")
    g.add_vertex("E")
    g.add_edge("E","B")
    print(g.adj_matrix)
    print(g.to_adj_list().adj_list)
    print(g.to_adj_list().to_adj_matrix().adj_matrix)