import unittest
import sort

class TestSort(unittest.TestCase):

    def run_sort_tests(self, sort_fn):
        self.assertEqual(sort_fn([]), [])
        self.assertEqual(sort_fn([1]), [1])
        self.assertEqual(sort_fn([1,1,1]), [1,1,1])
        self.assertEqual(sort_fn([1,2]), [1,2])
        self.assertEqual(sort_fn([2,1]), [1,2])
        self.assertEqual(sort_fn([3,1,2,4]), [1,2,3,4])
        self.assertEqual(sort_fn([3,1,2,2,4]), [1,2,2,3,4])
        self.assertEqual(sort_fn([4,-4,90,0,-1,1006,2,3,3]), [-4,-1,0,2,3,3,4,90,1006])

    def test_merge_sort(self):
        self.run_sort_tests(sort.merge_sort)

    def test_selection_sort(self):
        self.run_sort_tests(sort.selection_sort)

if __name__ == '__main__':
    unittest.main()
