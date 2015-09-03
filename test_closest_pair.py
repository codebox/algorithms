import unittest
from closest_pair import closest_pair

class TestArrayInversions(unittest.TestCase):

    def test_3(self):
        points = [(0,0), (10, 10), (11,11)]
        self.assertEqual(closest_pair(points), [(10,10), (11,11)])

    def test_10(self):
        points = [(-10,-10), (0, 0), (10,10), (-10,10), (10,-10), (5,5), (-5,5), (5,-5), (-5,-5), (6,6)]
        self.assertEqual(closest_pair(points), [(5,5), (6,6)])

if __name__ == '__main__':
    unittest.main()
