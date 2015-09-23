import unittest
from heap import Heap

class TestHeap(unittest.TestCase):

    def test_simple(self):
        h = Heap()
        h.insert(2)
        h.insert(1)
        h.insert(3)
        self.assertEqual(h.extract_min(), 1)
        self.assertEqual(h.extract_min(), 2)
        self.assertEqual(h.extract_min(), 3)
        self.assertEqual(h.extract_min(), None)

    def test_with_duplicates_and_negatives(self):
        h = Heap()
        h.insert(2)
        h.insert(2)
        h.insert(1)
        h.insert(0)
        h.insert(12)
        h.insert(5)
        h.insert(-8)
        h.insert(1)
        self.assertEqual(h.extract_min(), -8)
        self.assertEqual(h.extract_min(), 0)
        self.assertEqual(h.extract_min(), 1)
        self.assertEqual(h.extract_min(), 1)
        self.assertEqual(h.extract_min(), 2)
        self.assertEqual(h.extract_min(), 2)
        self.assertEqual(h.extract_min(), 5)
        self.assertEqual(h.extract_min(), 12)
        self.assertEqual(h.extract_min(), None)

if __name__ == '__main__':
    unittest.main()
