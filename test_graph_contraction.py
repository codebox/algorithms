import unittest
from graph_contraction import find_minimum_cut

class TestGraphContraction(unittest.TestCase):

    def check_result(self, graph, expected_min_cuts):
        result = find_minimum_cut(graph, 100)
        self.assertTrue(result in expected_min_cuts)

    def test_1(self):
        self.check_result([[0,1],[1,3],[2,3],[2,0],[1,2]], [[[0,1], [0,2]], [[1,3], [2,3]]])

    def test_2(self):
        self.check_result([[0,1]], [[[0,1]]])

    def test_3(self):
        self.check_result([[0,1], [0,2], [1,2]], [[[0,1], [0,2]], [[0,1],[1,2]], [[0,2], [1,2]]])

    def test_4(self):
        self.check_result([[0,2], [0,5], [1,4], [2,3], [3,4], [3,5], [4,5]], [[[1,4]]])

if __name__ == '__main__':
    unittest.main()
