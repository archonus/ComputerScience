from abc import ABC, abstractmethod
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
    class Edge:
        def __init__(self, to, weight = 1):
            self.to = to
            self.weight = weight
        def __repr__(self) -> str:
            return "{"+f"to:'{self.to}', weight:{self.weight}" + "}"

    def __init__(self, adj_list = None, vertices = None):
        if adj_list:
            self.adj_list = adj_list
        elif vertices: # Nodes defined, but no edges
            self.adj_list = {k : [] for k in vertices}
        else: # Empty graph
            self.adj_list = {}
    
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

    @classmethod
    def from_adj_matrix(cls,vertices, adj_matrix):
        adj_list= {}
        for i in range(len(vertices)):
            vertex = vertices[i]
            edges = []
            for j in range(len(vertices)):
                if adj_matrix[i][j] != 0:
                    edge = AdjacencyListGraph.Edge(vertices[j], adj_matrix[i][j])
                    edges.append(edge)
            adj_list[vertex] = edges
        return cls(adj_list)


class AdjacencyMatrixGraph(Graph):
    def __init__(self, vertices : List = None, adj_matrix = None, directed = True):
        self.vertices = vertices[:] if vertices else [] # Should really be a deep copy
        self._count = len(self.vertices)
        self.directed = directed
        if adj_matrix is not None:
            self.adj_matrix = adj_matrix
        elif directed:
            self.adj_matrix = [[0 for i in range(self._count)] for j in range(self._count)]
        else: # Undirected uses less space
            if self._count <= 1:
                self.adj_matrix = []
            else:
                self.adj_matrix = [[0 for i in range(self._count - j - 1)] for j in range(self._count)]
    
    def add_edge(self, vertex_from, vertex_to, weight = 1):
        self.update_edge(vertex_from,vertex_to,weight)

    def add_vertex(self,name):
        if name in self.vertices:
            raise ValueError("Vertex already exists")
        self.vertices.append(name)
        if self.directed:
            for row in self.adj_matrix:
                row.append(0) # Add another entry to each row (add a column)   
            self.adj_matrix.append([0 for i in range(len(self.vertices))])
        else:
            pass

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
    
    @classmethod
    def from_adj_list(cls, adj_list : dict):
        vertices = list(adj_list) #List of the keys
        adj_matrix = [[0 for i in range(len(vertices))] for j in range(len(vertices))] # n*n matrix
        for i in range(len(vertices)):
            vertex = vertices[i]
            edges = adj_list[vertex]
            for edge in edges:
                index = vertices.index(edge.to) #Index of the destination node
                adj_matrix[i][index] = edge.weight
        return cls(vertices, adj_matrix)


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
    # g2 = AdjacencyMatrixGraph.from_adj_list(g.adj_list)
    # g2.add_vertex("F")
    # g2.add_edge("B","F")
    # print(g2.adj_matrix)
    # g3 = AdjacencyListGraph.from_adj_matrix(g2.vertices, g2.adj_matrix)
    # print(g3.adj_list)

    g = AdjacencyMatrixGraph(vertices=["A","B","C","D"], directed=False)
    g.add_edge("A","B")
    g.add_edge("C","A")
    g.add_edge("D","C")
    print(g.adj_matrix)