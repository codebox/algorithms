import unittest
from dijkstras_shortest_path import Graph, find_shortest_path_basic

class TestDijkstrasShortestPath(unittest.TestCase):

    def test_simple(self):
        g=Graph([[0,1,1], [1,2,1], [2,3,1], [3,4,1]])
        find_shortest_path_basic(g, 0)
        self.assertEqual(g.get_node(0).distance, 0)
        self.assertEqual(g.get_node(1).distance, 1)
        self.assertEqual(g.get_node(2).distance, 2)
        self.assertEqual(g.get_node(3).distance, 3)
        self.assertEqual(g.get_node(4).distance, 4)

    def test_diamond(self):
        g=Graph([[0,1,1], [0,2,4], [1,2,2], [1,3,6], [2,3,3]])
        find_shortest_path_basic(g, 0)
        self.assertEqual(g.get_node(0).distance, 0)
        self.assertEqual(g.get_node(1).distance, 1)
        self.assertEqual(g.get_node(2).distance, 3)
        self.assertEqual(g.get_node(3).distance, 6)


if __name__ == '__main__':
    unittest.main()
