import random

'''
-----------------------
Deterministic Selection
-----------------------
* Performance:
    Best:       O(n)
    Average:    O(n)
    Worst:      O(n)
* Space:        n

Notes
-----
Selects the ith-smallest element from the list of values, without the use of a random pivot. This approach
tends to be slower on average than using random selection, however the worst-case running time is improved
from O(n^2) to O(n).
'''
def deterministic_select(values, ith_order):
    def select_pivot(values):
        groups_of_5 = []
        i=0
        while i < len(values):
            group = values[i:i+5]
            group.sort()
            groups_of_5.append(group)
            i+=5
        medians = map(lambda a : a[len(a)/2], groups_of_5)
        return select(medians, len(medians)/2)

    def partition(values):
        pivot_value = select_pivot(values)
        found_pivot = False
        smaller = []
        larger = []

        for v in values:
            if v > pivot_value:
                larger.append(v)
            elif v == pivot_value:
                if not found_pivot:
                    found_pivot = True
                else:
                    smaller.append(v)
            else:
                smaller.append(v)

        return [pivot_value], smaller, larger

    def select(values, i):
        if len(values) == 1:
            return values[0]

        pivot, smaller, larger = partition(values)
        len_smaller = len(smaller)

        if len_smaller == i:
            return pivot[0]
        elif i < len_smaller:
            return select(smaller, i)
        else:
            return select(larger, i - len_smaller - 1)

    return select(values, ith_order - 1)
