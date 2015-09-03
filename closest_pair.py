'''
----------------------
Closest Pair of Points
----------------------

Algorithm to find the closest pair of points in a 2-dimensional plane in O(n log n) time.

'''
def closest_pair(points):
    def merge_sort(points, get_value):
        END_OF_LIST = object()

        def list_get(l, i):
            if len(l) <= i:
                return END_OF_LIST
            return l[i]

        def merge(l1, l2):
            i1 = i2 = 0
            r = []

            while True:
                v1 = list_get(l1, i1)
                v2 = list_get(l2, i2)

                if v1 is END_OF_LIST:
                    r.extend(l2[i2:])
                    break

                elif v2 is END_OF_LIST:
                    r.extend(l1[i1:])
                    break

                elif get_value(v1) <= get_value(v2):
                    r.append(v1)
                    i1 += 1

                else:
                    r.append(v2)
                    i2 += 1

            return r

        def sort(points):
            l = len(points)

            if l < 2:
                return points

            r1 = sort(points[:l/2])
            r2 = sort(points[l/2:])

            return merge(r1, r2)

        return sort(points)

    def sort_by_y(p, p_plus_others_sorted_by_y):
        return filter(lambda n: n in p, p_plus_others_sorted_by_y)

    def distance_sq(p1, p2):
        return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2

    def distance(p1, p2):
        return distance_sq(p1, p2) ** 0.5

    def closest_split_pair(px, py, d):
        x_bar = px[len(px) / 2].x
        sy = filter(lambda p : (p.x >= x_bar - d) and (p.x < x_bar + d), py)
        best = d
        best_pair = (None, None)
        n = 7 # so weird that '7' is used here, but proof in video lectures in convincing

        for i in range(0, len(sy) - 1):
            for j in range(1, min(n+1, len(sy) - 1 - i)):
                this_d = distance(sy[i], sy[i+j])
                if this_d < best:
                    best = this_d
                    best_pair = (sy[i], sy[i+j])

        return best_pair

    def brute_force(pairs):
        pairs_copy = pairs[:]
        pairs_copy.sort(lambda pair1, pair2 : distance_sq(*pair1) - distance_sq(*pair2))
        return pairs_copy[0]

    def closest_pair(px, py):
        l = len(px)

        if l == 2:
            return px
        elif l == 3:
            return brute_force([[px[0], px[1]], [px[1], px[2]], [px[2], px[0]]])

        left_half  = px[:l/2]
        right_half = px[l/2:]

        left_half_sorted_by_x = left_half
        left_half_sorted_by_y = sort_by_y(left_half, sorted_by_y)

        right_half_sorted_by_x = right_half
        right_half_sorted_by_y = sort_by_y(right_half, sorted_by_y)

        p1, q1 = closest_pair(left_half_sorted_by_x, left_half_sorted_by_y)
        p2, q2 = closest_pair(right_half_sorted_by_x, right_half_sorted_by_y)

        d = min(distance(p1, q1), distance(p2, q2))
        p3, q3 = closest_split_pair(px, py, d)

        list_of_point_pairs = filter(lambda pair : pair[0] is not None, [[p1,q1], [p2,q2], [p3,q3]])

        return brute_force(list_of_point_pairs)

    class Point:
        def __init__(self, t):
            self.x = t[0]
            self.y = t[1]

    def map_to_xy(p):
        return map(Point, p)    

    points_xy = map_to_xy(points)
    sorted_by_x = merge_sort(points_xy, lambda p : p.x)
    sorted_by_y = merge_sort(points_xy, lambda p : p.y)

    result = closest_pair(sorted_by_x, sorted_by_y)

    return [(result[0].x, result[0].y), (result[1].x, result[1].y)]
