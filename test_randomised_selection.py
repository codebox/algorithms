import unittest
from randomised_selection import randomised_select

class TestRandomisedSelect(unittest.TestCase):
    def check_all_positions(self, unsorted, sorted):
        for i in range(1, len(sorted)+1):
            answer = sorted[i-1]
            self.assertEqual(randomised_select(unsorted, i), answer, 'Failed using {}'.format(i))

    def test(self):
        self.check_all_positions([7,4,3,0,9,6,5,1,2,8], [0,1,2,3,4,5,6,7,8,9])
        self.check_all_positions([2,4,6,8], [2,4,6,8])
        self.check_all_positions([9,8,7,6,5], [5,6,7,8,9])
        self.check_all_positions([100, -43, 18, 332, 714, 3750, 6, 6, 1, 6], [-43, 1, 6, 6, 6, 18, 100, 332, 714, 3750])

if __name__ == '__main__':
    unittest.main()
