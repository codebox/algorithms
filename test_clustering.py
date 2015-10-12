import unittest
from clustering import cluster

class TestClustering(unittest.TestCase):

    def test_cluster_count_correct(self):
        clusters = cluster([[1,12], [2,10], [1,8], [3,14], [2,9], [12,1], [10,2], [8,1], [14,3], [9,2]], 1)
        self.assertEqual(len(clusters), 1)

        clusters = cluster([[1,12], [2,10], [1,8], [3,14], [2,9], [12,1], [10,2], [8,1], [14,3], [9,2]], 2)
        self.assertEqual(len(clusters), 2)

        clusters = cluster([[1,12], [2,10], [1,8], [3,14], [2,9], [12,1], [10,2], [8,1], [14,3], [9,2]], 3)
        self.assertEqual(len(clusters), 3)

        clusters = cluster([[1,12], [2,10], [1,8], [3,14], [2,9], [12,1], [10,2], [8,1], [14,3], [9,2]], 4)
        self.assertEqual(len(clusters), 4)

    def test_clusters_correct(self):
        clusters = cluster([[1,12], [2,10], [1,8], [3,14], [2,9], [12,1], [10,2], [8,1], [14,3], [9,2]], 2)

        self.assertTrue('1-12' in clusters[0])
        self.assertTrue('2-10' in clusters[0])
        self.assertTrue('1-8'  in clusters[0])
        self.assertTrue('3-14' in clusters[0])
        self.assertTrue('2-9'  in clusters[0])

        self.assertTrue('12-1' in clusters[1])
        self.assertTrue('10-2' in clusters[1])
        self.assertTrue('8-1'  in clusters[1])
        self.assertTrue('14-3' in clusters[1])
        self.assertTrue('9-2'  in clusters[1])
