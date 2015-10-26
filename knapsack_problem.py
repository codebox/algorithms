'''
Knapsack Problem
----------------
Given a list of items, each with a weight and a value, determine the subset of items with the largest value and with
total weight not exceeding some fixed capacity.

This algorithm runs in O(nW) where 'n' is the number of items in the list and 'W' is the maximum capacity.
'''

def knapsack(l, capacity):
    # A[x][y] will contain value for optimal solution using first 'x' items and capacity 'y'
    A = []

    values_for_first_0_items = [0] * (capacity + 1)
    A.append(values_for_first_0_items)

    for i in range(1, len(l) + 1):
        # items in 'l' are of the form [<value>,<weight>]
        v, w = l[i-1]
        values_for_first_i_items = []

        for x in range(capacity + 1):
            if w > x or A[i-1][x] > A[i-1][x-w] + v:
                values_for_first_i_items.append(A[i-1][x])
            else:
                values_for_first_i_items.append(A[i-1][x-w] + v)

        A.append(values_for_first_i_items)

    # We now know the total value for the optimal solution, work backwards to determine which items the value represents
    items = []
    w = capacity
    for i in range(len(l), 0, -1):
        if A[i][w] > A[i-1][w]:
            items.append(l[i-1])
            w -= l[i-1][1]

    return A[len(l)][capacity], items

