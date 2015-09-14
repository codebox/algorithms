import unittest
from graph_search import breadth_first_search, depth_first_search, connected_components, Graph

class TestGraphSearch(unittest.TestCase):
    def __get_visited_values(self, g, node_ids):
        return map(lambda id : g.get_node(id).visited, node_ids)

    def test_bfs_simple_connected(self):
        g = Graph([[0,1],[1,2],[2,0]])
        breadth_first_search(g, 0)

        for i in range(3):
            self.assertTrue(g.get_node(i).visited)

    def test_bfs_parallel_edges(self):
        g = Graph([[0,1],[1,2],[1,2],[2,1],[0,1],[0,2]])
        breadth_first_search(g, 0)

        for i in range(3):
            self.assertTrue(g.get_node(i).visited)

    def test_bfs_self_edges(self):
        g = Graph([[0,0],[0,1],[1,1],[2,2],[2,0]])
        breadth_first_search(g, 0)

        for i in range(3):
            self.assertTrue(g.get_node(i).visited)

    def test_bfs_disconnected(self):
        g = Graph([[0,1],[2,3]])
        breadth_first_search(g, 0)

        for i in range(2):
            self.assertTrue(g.get_node(i).visited)

        for i in range(2,4):
            self.assertFalse(g.get_node(i).visited)

        breadth_first_search(g, 2)

        for i in range(2,4):
            self.assertTrue(g.get_node(i).visited)

    def test_bfs_check_order(self):
        g = Graph([[0,1], [0,2], [1,3], [1,4], [2,5], [2,6]])
        breadth_first_search(g, 0)
        self.assertTrue(g.get_node(0).visited < min(self.__get_visited_values(g, [1,2])))
        self.assertTrue(g.get_node(1).visited < min(self.__get_visited_values(g, [3,4,5,6])))
        self.assertTrue(g.get_node(2).visited < min(self.__get_visited_values(g, [3,4,5,6])))

    def test_dfs_simple_connected(self):
        g = Graph([[0,1],[1,2],[2,0]])
        depth_first_search(g, 0)

        for i in range(3):
            self.assertTrue(g.get_node(i).visited)

    def test_dfs_parallel_edges(self):
        g = Graph([[0,1],[1,2],[1,2],[2,1],[0,1],[0,2]])
        depth_first_search(g, 0)

        for i in range(3):
            self.assertTrue(g.get_node(i).visited)

    def test_dfs_self_edges(self):
        g = Graph([[0,0],[0,1],[1,1],[2,2],[2,0]])
        depth_first_search(g, 0)

        for i in range(3):
            self.assertTrue(g.get_node(i).visited)

    def test_dfs_disconnected(self):
        g = Graph([[0,1],[2,3]])
        depth_first_search(g, 0)

        for i in range(2):
            self.assertTrue(g.get_node(i).visited)

        for i in range(2,4):
            self.assertFalse(g.get_node(i).visited)

        depth_first_search(g, 2)

        for i in range(2,4):
            self.assertTrue(g.get_node(i).visited)

    def test_dfs_check_order(self):
        g = Graph([[0,1], [0,2], [1,3], [1,4], [2,5], [2,6]])

        depth_first_search(g, 0)
        if g.get_node(1).visited < g.get_node(2).visited:
            self.assertTrue(g.get_node(3).visited < g.get_node(2).visited)
            self.assertTrue(g.get_node(4).visited < g.get_node(2).visited)
        else:
            self.assertTrue(g.get_node(5).visited < g.get_node(1).visited)
            self.assertTrue(g.get_node(6).visited < g.get_node(1).visited)

        self.assertTrue(g.get_node(0).visited < g.get_node(1).visited)
        self.assertTrue(g.get_node(0).visited < g.get_node(2).visited)
        self.assertTrue(g.get_node(1).visited < g.get_node(3).visited)
        self.assertTrue(g.get_node(1).visited < g.get_node(4).visited)
        self.assertTrue(g.get_node(2).visited < g.get_node(5).visited)
        self.assertTrue(g.get_node(2).visited < g.get_node(6).visited)
        
    def test_connected_components_fully_connected(self):
        graph = Graph([[0,1],[1,2],[2,0]])
        result = connected_components(graph)
        self.assertEqual(len(result), 1)
        self.assertTrue(result[0].id in [0,1,2])        

    def test_connected_components_disconnected(self):
        graph = Graph([[0,1],[1,2],[2,0],[3,4],[3,5],[3,6],[7,8]])
        result = connected_components(graph)
        self.assertEqual(len(result), 3)
        self.assertTrue(result[0].id in [0,1,2])
        self.assertTrue(result[1].id in [3,4,5,6])
        self.assertTrue(result[2].id in [7,8])

if __name__ == '__main__':
    unittest.main()
