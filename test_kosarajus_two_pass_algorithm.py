import unittest
from graph_search import Graph
from kosarajus_two_pass_algorithm import find_strongly_connected_components

class TestKosaraju(unittest.TestCase):

    def test_1(self):
        result = find_strongly_connected_components([[7,1],[4,7],[1,4],[9,7],[6,9],[3,6],[9,3],[8,6],[2,8],[5,2],[8,5]])

        self.assertEqual(3, len(result))

        component_sets = [set([1,4,7]), set([3,6,9]), set([2,5,8])]
        self.assertTrue(set(result[0]) in component_sets)
        self.assertTrue(set(result[1]) in component_sets)
        self.assertTrue(set(result[2]) in component_sets)

if __name__ == '__main__':
    unittest.main()
