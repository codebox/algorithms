import unittest
from prims_minimum_spanning_tree import min_spanning_tree, Node, Edge, Graph

class TestPrimsMinimumSpanningTree(unittest.TestCase):

    def test_simple(self):
        g = Graph([[1,2,1], [1,4,3], [1,3,4], [2,4,2], [3,4,5]])
        self.assertEqual(map(str, min_spanning_tree(g)), ['1-2 1', '2-4 2', '1-3 4'])