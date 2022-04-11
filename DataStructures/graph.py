from typing import List

class AdjacencyListGraph:
    # Actually uses a dictionary instead of list
    class Edge:
        def __init__(self, to, weight = 1):
            self.to = to
            self.weight = weight
        def __repr__(self) -> str:
            return "{"+f"to:'{self.to}', weight:{self.weight}" + "}"

    def __init__(self, adj_list = None, nodes = None):
        if adj_list:
            self.adj_list = adj_list
        elif nodes: # Nodes defined, but no edges
            self.adj_list = {k : [] for k in nodes}
        else: # Empty graph
            self.adj_list = {}
    
    def add_vertex(self, name):
        if name not in self.adj_list:
            self.adj_list[name] = []
    
    def add_edge(self, vertex_from, vertex_to, weight = 1):
        edges = self.adj_list[vertex_from]
        if vertex_to not in [e.to for e in edges]:
            edge = AdjacencyListGraph.Edge(vertex_to, weight)
            edges.append(edge)
        else:
            raise ValueError("Edge already exists")

    def update_edge(self,vertex_from, vertext_to, weight):
        edges = self.adj_list[vertex_from]

class AdjacencyMatrixGraph:
    def __init__(self, vertices : List = None, adj_matrix = None):
        self.vertices = vertices[:] if vertices else [] # Should really be a deep copy
        self._count = len(self.vertices)
        self.adj_matrix = adj_matrix if adj_matrix else [[0 for i in range(self._count)] for j in range(self._count)] # Create matrix if the matrix not provided
    
    def add_edge(self, vertex_from, vertex_to, weight = 1):
        self.update_edge(vertex_from,vertex_to,weight)

    def add_vertex(self,name):
        self.vertices.append(name)
        for row in self.adj_matrix:
            row.append(0) # Add another entry to each row (add a column)   
        self.adj_matrix.append([0 for i in range(len(self.vertices))])

    def add_vertices(self, *args):
        for name in args:
            self.add_vertex(name)

    def update_edge(self, vertex_from, vertex_to, weight):
        index_from = self.vertices.index(vertex_from)
        index_to = self.vertices.index(vertex_to)
        self.adj_matrix[index_from][index_to] = weight

    def edge_weight(self, vertex_from, vertex_to):
        index_from = self.vertices.index(vertex_from)
        index_to = self.vertices.index(vertex_to)
        return self.adj_matrix[index_from][index_to]

    def check_connected(self, vertex_from, vertex_to):
        return self.edge_weight(vertex_from,vertex_to) != 0
    
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
    # g = AdjacencyMatrixGraph()
    # print(g.adj_matrix)
    # g.add_vertices("A","B","C")
    # g.add_edge("A","B")
    # print(g.adj_matrix)

    g = AdjacencyListGraph(nodes = ["A","B","C"])
    print(g.adj_list)
    g.add_edge("A","B")
    print(g.adj_list)