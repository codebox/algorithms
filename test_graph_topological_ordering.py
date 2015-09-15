import unittest
from graph_search import Graph
from graph_topological_ordering import find_topological_order

class TestGraphTopologicalOrdering(unittest.TestCase):

    def check_labels(self, graph, smaller, larger):
        self.assertTrue(graph.get_node(smaller).label < graph.get_node(larger).label)

    def test_1(self):
        graph = Graph([[0,1],[0,2],[1,3],[2,3]], True)
        find_topological_order(graph)

        self.check_labels(graph, 0, 1)
        self.check_labels(graph, 0, 2)
        self.check_labels(graph, 1, 3)
        self.check_labels(graph, 2, 3)

    def test_2(self):
        graph = Graph([[0,1],[1,2],[1,3],[2,4],[3,5]], True)
        find_topological_order(graph)

        self.check_labels(graph, 0, 1)
        self.check_labels(graph, 1, 2)
        self.check_labels(graph, 1, 3)
        self.check_labels(graph, 2, 4)
        self.check_labels(graph, 3, 5)

if __name__ == '__main__':
    unittest.main()
