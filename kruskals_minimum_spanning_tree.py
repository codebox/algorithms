from union_find import UnionFind

'''
Kruskal's Minimum Spanning Tree
-----------------------------
Computes the minimum spanning tree of a connected, undirected graph using the Union-Find data structure to give O(m log n) running time
'''
def min_spanning_tree(g):
    tree_edges = []
    edges_by_cost = g.edges[:]
    edges_by_cost.sort(key=lambda e : e.cost)

    # initially each node is in its own group
    initial_groups = map(lambda n : [n], g.nodes)
    uf = UnionFind(initial_groups)

    def edge_creates_cycle(edge):
        return uf.find(edge.node1) == uf.find(edge.node2)

    for edge in edges_by_cost:
        if not edge_creates_cycle(edge):
            tree_edges.append(edge)
            uf.union(edge.node1, edge.node2)

    return tree_edges


class Edge:
    def __init__(self, node1, node2, cost):
        self.node1 = node1
        self.node2 = node2
        self.cost  = cost

    def __str__(self):
        return "{}-{} {}".format(self.node1, self.node2, self.cost)


class Graph:
    def __init__(self, l):
        self.edges = []
        self.nodes = set()

        for e in l:
            self.edges.append(Edge(e[0], e[1], e[2]))
            self.nodes.add(e[0])
            self.nodes.add(e[1])
