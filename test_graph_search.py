import unittest
from graph_search import breadth_first_search, Graph

class TestGraphSearch(unittest.TestCase):

    def test_simple_connected(self):
        g = Graph([[0,1],[1,2],[2,0]])
        breadth_first_search(g, 0)

        for i in range(3):
            self.assertTrue(g.get_node(i).visited)

    def test_parallel_edges(self):
        g = Graph([[0,1],[1,2],[1,2],[2,1],[0,1],[0,2]])
        breadth_first_search(g, 0)

        for i in range(3):
            self.assertTrue(g.get_node(i).visited)

    def test_self_edges(self):
        g = Graph([[0,0],[0,1],[1,1],[2,2],[2,0]])
        breadth_first_search(g, 0)

        for i in range(3):
            self.assertTrue(g.get_node(i).visited)

    def test_disconnected(self):
        g = Graph([[0,1],[2,3]])
        breadth_first_search(g, 0)

        for i in range(2):
            self.assertTrue(g.get_node(i).visited)

        for i in range(2,4):
            self.assertFalse(g.get_node(i).visited)

        breadth_first_search(g, 2)

        for i in range(2,4):
            self.assertTrue(g.get_node(i).visited)

if __name__ == '__main__':
    unittest.main()
