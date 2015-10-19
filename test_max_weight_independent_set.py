import unittest
from max_weight_independent_set import find_mwis

class TestFindMaxWeightIndependentSet(unittest.TestCase):
    def test_with_single_item(self):
        self.assertEqual(find_mwis([3]), [3])

    def test_with_multiple_solutions(self):
        self.assertEqual(find_mwis([3,3,1,1]), [3,1])

    def test_with_single_solution(self):
        self.assertEqual(find_mwis([3,4,5,6,7]), [3,5,7])
        self.assertEqual(find_mwis([1,4,5,4]), [4,4])
