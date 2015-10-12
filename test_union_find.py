import unittest
from union_find import UnionFind

class TestUnionFind(unittest.TestCase):

    def test_find(self):
        uf = UnionFind([[1,2,3],[4,5],[6,7,8,9,0]])
        self.assertEqual(uf.find(1), 1)
        self.assertEqual(uf.find(2), 1)
        self.assertEqual(uf.find(3), 1)

        self.assertEqual(uf.find(4), 4)
        self.assertEqual(uf.find(5), 4)

        self.assertEqual(uf.find(6), 6)
        self.assertEqual(uf.find(7), 6)
        self.assertEqual(uf.find(8), 6)
        self.assertEqual(uf.find(9), 6)
        self.assertEqual(uf.find(0), 6)

    def test_union_when_already_united(self):
        uf = UnionFind([[1,2,3],[4,5],[6,7,8,9,0]])
        self.assertEqual(uf.find(1), 1)
        self.assertEqual(uf.find(2), 1)

        uf.union(1,2)

        self.assertEqual(uf.find(1), 1)
        self.assertEqual(uf.find(2), 1)

    def test_union(self):
        uf = UnionFind([[1,2,3],[4,5],[6,7,8,9,0]])
        self.assertEqual(uf.find(2), 1)
        self.assertEqual(uf.find(5), 4)

        uf.union(2,5)

        self.assertEqual(uf.find(1), 1)
        self.assertEqual(uf.find(2), 1)
        self.assertEqual(uf.find(3), 1)
        self.assertEqual(uf.find(4), 1)
        self.assertEqual(uf.find(5), 1)

if __name__ == '__main__':
    unittest.main()
