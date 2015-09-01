import unittest
import array_inversions

class TestArrayInversions(unittest.TestCase):

    def check_inversion_count(self, input_values, expected_count):
        self.assertEqual(array_inversions.count_inversions(input_values), expected_count)

    def test(self):
        self.check_inversion_count([], 0)
        self.check_inversion_count([1], 0)
        self.check_inversion_count([1,1,1], 0)
        self.check_inversion_count([1,2,3,4], 0)
        self.check_inversion_count([2,1], 1)
        self.check_inversion_count([3,2,1], 3)
        self.check_inversion_count([5,4,3,2,1], 10)
        self.check_inversion_count([1,2,3,5,4], 1)
        self.check_inversion_count([3,4,6,1,2,5], 7)
        self.check_inversion_count([1,2,1], 1)
        self.check_inversion_count([2,2,1,1], 4)
        self.check_inversion_count([1,2,3,4,1], 3)
        self.check_inversion_count([5,2,10,8,1,9,4,3,6,7], 22)
        
if __name__ == '__main__':
    unittest.main()
