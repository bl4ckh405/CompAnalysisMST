from points import Point


class Graph:
    #Represents a weighted graph.
    
    def __init__(self):
        #Initialize an empty graph
        self.vertices = []
        self.edges = []
    
    def add_vertex(self, point):
        #Add a vertex (Point) to the graph.
        
        if point not in self.vertices:
            self.vertices.append(point)
    
    def add_edge(self, point1, point2, weight):

        # Ensure both vertices are in the graph
        self.add_vertex(point1)
        self.add_vertex(point2)
        
        # Add edge (avoid duplicates by checking if edge already exists)
        edge = (point1, point2, weight)
        reverse_edge = (point2, point1, weight)
        
        if edge not in self.edges and reverse_edge not in self.edges:
            self.edges.append(edge)
    
    def build_from_points(self, points, max_distance=20):

        # Add all points as vertices
        for point in points:
            self.add_vertex(point)
        
        # Find neighbors and create edges
        for point in points:
            neighbors = point.find_neighbors(points, max_distance)
            for neighbor, distance in neighbors:
                self.add_edge(point, neighbor, distance)
    
    def get_edge_count(self):
        
        #Get the number of edges in the graph.
        

        return len(self.edges)
    
    def get_vertex_count(self):
        #Get the number of vertices in the graph.
        
        return len(self.vertices)
    
    def get_sorted_edges(self):
        #Get edges sorted by weight (for MST algorithms).
        
        return sorted(self.edges, key=lambda edge: edge[2])
    
    def __repr__(self):
        #String representation of the graph.
        
        return f"Graph(vertices={len(self.vertices)}, edges={len(self.edges)})"
