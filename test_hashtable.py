import unittest
from hashtable import HashTable

class TestHashTable(unittest.TestCase):

    def test_distinct_buckets(self):
        h = HashTable(13)
        h.put('a', 1)
        h.put('b', 2)
        h.put('c', 3)
        self.assertEqual(h.get('a'), 1)

    def test_bucket_collision(self):
        h = HashTable(13)
        h.put('a', 1) # both will use bucket 6
        h.put('n', 2)
        self.assertEqual(h.get('a'), 1)
        self.assertEqual(h.get('n'), 2)

if __name__ == '__main__':
    unittest.main()
