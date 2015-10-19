'''
Find Maximum Weight Independent Set
-----------------------------------
Finds the sub-set of values with the largest sum, where no two values are adjacent in the list.
'''
def find_mwis(values):
    n = len(values)
    max_weight_values = [0, values[0]]

    for i in range(2, n+1):
        max_weight_values.append(max(max_weight_values[i-1], max_weight_values[i-2] + values[i-1]))

    i = n
    mwis = []
    while i >= 1:
        if max_weight_values[i-1] >= max_weight_values[i-2] + values[i-1]:
            i -= 1
        else:
            mwis.insert(0, values[i-1])
            i -= 2

    return mwis
