import random

'''
--------------------
Randomised Selection
--------------------
* Performance:
    Best:       O(n)
    Average:    O(n)
    Worst:      O(n^2)
* Space:        n

Notes
-----
Selects the ith-smallest element from the list of values - this algorithm is based on QuickSort.
'''
def randomised_select(values, ith_order):
    def partition(values):
        i_pivot = random.randint(0, len(values) - 1)

        values[0], values[i_pivot] = values[i_pivot], values[0]

        pivot_value = values[0]
        i_last_smaller = 0

        for i in range(1, len(values)):
            if values[i] <= pivot_value:
                values[i], values[i_last_smaller + 1] = values[i_last_smaller + 1], values[i]
                i_last_smaller += 1

        return values[0:1], values[1:i_last_smaller+1], values[i_last_smaller+1:]

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
