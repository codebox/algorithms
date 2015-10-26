import unittest
from knapsack_problem import knapsack

class TestKnapsackProblem(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(knapsack([], 10), (0,[]))

    def test_single_item(self):
        self.assertEqual(knapsack([[1,1]],  10), (1,[[1,1]]))
        self.assertEqual(knapsack([[1,10]], 10), (1,[[1,10]]))
        self.assertEqual(knapsack([[1,11]], 10), (0,[]))

    def test_multiple_items(self):
        self.assertEqual(knapsack([[3,4],[2,3],[4,2],[4,3]], 6), (8, [[4, 3], [4, 2]]))
        self.assertEqual(knapsack([[3,4],[2,3],[4,2],[4,3]], 7), (8, [[4, 3], [4, 2]]))
        self.assertEqual(knapsack([[3,4],[2,3],[4,2],[4,3]], 8), (10, [[4, 3], [4, 2], [2, 3]]))

if __name__ == '__main__':
    unittest.main()
