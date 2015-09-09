import random
import operator

def find_minimum_cut(graph, iterations):
    best = []

    class Edge:
        def __init__(self, l):
            self.p1 = l[0]
            self.p2 = l[1]

        def __str__(self):
            return "{}-{}".format(self.p1, self.p2)

    class VirtualNode:
        def __init__(self, n):
            self.nodes = [n]
            self.internal_edges = []
            self.external_edges = []

        def __is_edge_internal(self, edge):
            return edge.p1 in self.nodes and edge.p2 in self.nodes

        def __is_edge_external(self, edge):
            return not self.__is_edge_internal(edge)

        def merge(self, other):
            self.nodes += other.nodes

            self.internal_edges += other.internal_edges
            self.internal_edges += filter(self.__is_edge_internal, other.external_edges)

            self.external_edges += filter(self.__is_edge_external, other.external_edges)
            self.external_edges = filter(lambda e : e not in self.internal_edges, self.external_edges)

    class VirtualGraph:
        def __init__(self, graph):
            self.v_nodes = []
            nodes = set(reduce(operator.add, graph)) # find distinct nodes in graph
            for node in nodes:
                self.v_nodes.append(VirtualNode(node))

            for e in graph:
                edge = Edge(e)
                for v_node in self.v_nodes:
                    if edge.p1 in v_node.nodes or edge.p2 in v_node.nodes:
                        v_node.external_edges.append(edge)

        def get_nodes(self):
            return self.v_nodes

        def contract(self):
            n1, n2 = random.sample(self.v_nodes, 2)
            n1.merge(n2)
            self.v_nodes.remove(n2)

    def random_contraction(graph):
        v_graph = VirtualGraph(graph)
        
        while len(v_graph.get_nodes()) > 2:
            v_graph.contract()

        result = v_graph.get_nodes()[0].external_edges
        return map(lambda e : sorted([e.p1, e.p2]), result)

    for i in range(iterations):
        result = random_contraction(graph)

        if len(best) == 0 or len(result) < len(best):
            best = result

    def compare_edges(e1, e2):
        if e1[0] < e2[0]:
            return -1
        elif e1[0] > e2[0]:
            return 1
        elif e1[1] < e2[1]:
            return -1
        elif e1[1] > e2[1]:
            return 1
        else:
            return 0

    best.sort(compare_edges)

    return best