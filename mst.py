class UnionFind:
    #Union-Find (Disjoint Set) data structure for cycle detection.

    def __init__(self, vertices):

        # Each vertex starts in its own set
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}
    
    def find(self, vertex):

        if self.parent[vertex] != vertex:
            # Path compression: make vertex point directly to root
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    
    def union(self, vertex1, vertex2):
        
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        
        if root1 == root2:
            return False  # Already in the same set (would create cycle)
        
        # Union by rank: attach smaller tree under larger tree
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
        
        return True


def kruskal_mst(graph):
    
    mst_edges = []
    
    # Sort edges by weight
    sorted_edges = graph.get_sorted_edges()
    
    # Initialize Union-Find
    uf = UnionFind(graph.vertices)
    
    # Process edges in order of increasing weight
    for point1, point2, weight in sorted_edges:
        # Check if adding this edge would create a cycle
        if uf.union(point1, point2):
            # No cycle, add to MST
            mst_edges.append((point1, point2, weight))
            
            # MST is complete when we have (n-1) edges for n vertices
            if len(mst_edges) == len(graph.vertices) - 1:
                break
    
    return mst_edges


def calculate_mst_weight(mst_edges):
    
    return sum(weight for _, _, weight in mst_edges)


def verify_mst(mst_edges, vertex_count):
    
    expected_edges = vertex_count - 1
    actual_edges = len(mst_edges)
    
    if actual_edges != expected_edges:
        return False, f"MST should have {expected_edges} edges but has {actual_edges}"
    
    return True, "MST is valid"
