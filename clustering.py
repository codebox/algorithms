from union_find import UnionFind
from itertools import combinations

'''
Single-Link Clustering
----------------------
Partitions a set of points into k distinct clusters to maximise the max-spacing value (distance between closest pair of points
that lie is different clusters).
'''
def cluster(points, k):
    uf = UnionFind2(map(lambda o : [o], points), lambda p : str(p[0]) + '-' + str(p[1]))
    cluster_count = len(points)

    while cluster_count > k:
        p = closest_pair(points, uf)
        uf.union(p[0], p[1])
        cluster_count -= 1

    return uf.get_clusters()

def get_sqdistance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def closest_pair(points, uf):
    min_pair = None
    min_sqdistance = None
    for pair in combinations(points, 2):
        in_same_cluster = (uf.find(pair[0]) == uf.find(pair[1]))
        if not in_same_cluster:
            if not min_pair:
                min_pair = pair
                min_sqdistance = get_sqdistance(pair[0], pair[1])
            else:
                sqdistance = get_sqdistance(pair[0], pair[1])
                if sqdistance < min_sqdistance:
                    min_sqdistance = sqdistance
                    min_pair = pair
    return min_pair

class UnionFind2:
    def __init__(self, groups, fn):
        self.fn = fn
        g = []
        for group in groups:
            g.append(map(fn, group))
        self.uf = UnionFind(g)

    def find(self, item):
        return self.uf.find(self.fn(item))

    def union(self, item_1, item_2):
        self.uf.union(self.fn(item_1), self.fn(item_2))

    def get_clusters(self):
        return self.uf.leader_to_group.values()