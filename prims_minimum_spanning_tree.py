'''
Prims's Minimum Spanning Tree
-----------------------------
Computes the minimum spanning tree of a connected, undirected graph
'''
def min_spanning_tree(g):
    covered_nodes   = set([g.get_nodes()[0]]) # we can start at any node, just pick the first one
    uncovered_nodes = set(g.get_nodes()[1:])
    tree_edges = []

    def edge_crosses_boundary(e):
        return len(filter(lambda n : n in covered_nodes, [e.node1, e.node2])) == 1

    def lowest_cost_edge(l):
        return min(l, key=lambda e: e.cost)

    def edge_covered(e):
        covered_nodes.add(e.node1)
        covered_nodes.add(e.node2)
        uncovered_nodes.discard(e.node1)
        uncovered_nodes.discard(e.node2)

    while len(uncovered_nodes):
        edges = []
        for n in covered_nodes:
            edges.extend(filter(edge_crosses_boundary, n.edges))

        next_edge = lowest_cost_edge(edges)
        edge_covered(next_edge)
        tree_edges.append(next_edge)

    return tree_edges

class Node:
    def __init__(self, id):
        self.id = id
        self.edges = []

class Edge:
    def __init__(self, node1, node2, cost):
        self.node1 = node1
        self.node2 = node2
        self.cost  = cost

    def __str__(self):
        return "{}-{} {}".format(self.node1.id, self.node2.id, self.cost)


class Graph:
    def __init__(self, l):
        self.nodes = {}

        def add_node_if_required(id):
            if not self.nodes.has_key(id):
                self.nodes[id] = Node(id)
            return self.nodes[id]

        for e in l:
            node1 = add_node_if_required(e[0])
            node2 = add_node_if_required(e[1])

            edge = Edge(node1, node2, e[2])

            node1.edges.append(edge)
            node2.edges.append(edge)

    def get_nodes(self):
        return self.nodes.values()

    def get_node(self, id):
        return self.nodes[id]
