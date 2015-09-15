from graph_search import Node, Graph

current_label = None

def find_topological_order(graph):
    global current_label
    current_label = graph.get_node_count()

    def depth_first_search(graph, start_node):
        def search(graph, node):
            global current_label
            node.visited = True
            for neighbour in node.neighbours:
                if not neighbour.visited:
                    search(graph, neighbour)

            node.label = current_label
            current_label -= 1

        return search(graph, start_node)

    for node in graph.get_nodes():
        if not node.visited:
            depth_first_search(graph, node)
