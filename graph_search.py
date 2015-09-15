from Queue import Queue

def breadth_first_search(graph, start_node_id):
    start_node = graph.get_node(start_node_id)
    start_node.visited = 1
    visit_index = 2

    q = Queue()
    q.put(start_node)

    while not q.empty():
        node = q.get()
        for neighbour in node.neighbours:
            if not neighbour.visited:
                neighbour.visited = visit_index
                visit_index += 1
                q.put(neighbour)

def connected_components(graph):
    result = []
    for node_id in graph.get_node_ids():
        node = graph.get_node(node_id)
        if node.visited == False:
            result.append(node)
            breadth_first_search(graph, node.id)
    return result

def depth_first_search(graph, start_node_id):
    def search(graph, node_id):
        node = graph.get_node(node_id)
        node.visited = search.visit_index
        search.visit_index += 1
        for neighbour in node.neighbours:
            if not neighbour.visited:
                search(graph, neighbour.id)

    search.visit_index = 1

    return search(graph, start_node_id)


class Node:
    def __init__(self, id):
        self.id = id
        self.label = None
        self.visited = False
        self.neighbours = [] 

class Graph:
    def __init__(self, l, is_directed=False):
        self.nodes = {}

        def add_node_if_required(id):
            if not self.nodes.has_key(id):
                self.nodes[id] = Node(id)
            return self.nodes[id]

        for e in l:
            node1 = add_node_if_required(e[0])
            node2 = add_node_if_required(e[1])
            node1.neighbours.append(node2)
            if not is_directed:
                node2.neighbours.append(node1)

    def get_node_count(self):
        return len(self.nodes)

    def get_node_ids(self):
        return self.nodes.keys()[:]

    def get_nodes(self):
        return self.nodes.values()[:]

    def get_node(self, id):
        return self.nodes[id]

    def get_outgoing(self, from_id):
        return self.nodes[from_id].neighbours[:]
