from graph_search import Graph

'''
Implementation of Kosaraju's two-pass algorithm, which finds strongly connected components within a directed graph.
'''
t = 0
s = None
class GraphWithTS(Graph):
    def __init__(self, l, is_directed=False):
        Graph.__init__(self, l, is_directed)
        self.t = 0
        self.s = None

def find_strongly_connected_components(l):
    def depth_first_search(graph, start_node):
        def search(graph, node):
            global t, s
            node.visited = True
            node.s = s
            for neighbour in node.neighbours:
                if not neighbour.visited:
                    search(graph, neighbour)
            t += 1
            node.t = t

        return search(graph, start_node)

    r_l = map(lambda i: [i[1], i[0]], l)

    graph   = GraphWithTS(l, True)
    r_graph = GraphWithTS(r_l, True)

    def dfs_loop(graph):
        global s
        nodes = graph.get_nodes()
        nodes.sort(key=lambda n: n.label, reverse=True)

        for node in nodes:
            if not node.visited:
                s = node
                depth_first_search(graph, node)

    for n in r_graph.get_nodes():
        n.label = n.id

    dfs_loop(r_graph)

    for n in r_graph.get_nodes():
        graph.get_node(n.id).label = n.t

    dfs_loop(graph)
    result = {}
    for n in graph.get_nodes():
        leader = n.s.id
        if not result.has_key(leader):
            result[leader] = []
        result[leader].append(n.id)
    
    return result.values()
