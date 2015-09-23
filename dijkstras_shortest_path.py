def find_shortest_path_basic(graph, start_node_id):
    start_node = graph.get_node(start_node_id)
    explored = set([start_node])
    start_node.distance = 0
    start_node.path = []
    edges_to_unexplored = start_node.outgoing

    while len(explored) < len(graph.get_nodes()):
        min_score = min_node = None
        for edge in edges_to_unexplored:
            node  = edge.end
            score = edge.start.distance + edge.length
            if not min_node or (score < min_score):
                min_node = node
                min_score = score

        explored.add(min_node)
        min_node.distance = min_score

        edges_to_unexplored.extend(min_node.outgoing)
        for edge in edges_to_unexplored:
            if edge.end in explored:
                edges_to_unexplored.remove(edge)

class Node:
    def __init__(self, id):
        self.id = id
        self.outgoing = [] 

class Edge:
    def __init__(self, start, end, length):
        self.start = start
        self.end   = end
        self.length = length

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
            node1.outgoing.append(Edge(node1, node2, e[2]))

    def get_nodes(self):
        return self.nodes.values()[:]

    def get_node(self, id):
        return self.nodes.get(id)
