'''
----------
Merge Sort
----------
* Performance:
    Best:       O(n log n)
    Average:    O(n log n)
    Worst:      O(n log n)
* Space:        2n
* Stable:       Yes
'''
def merge_sort(values):
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

            elif v1 <= v2: # this needs to be '<='' rather than '<' to ensure the sort is stable
                r.append(v1)
                i1 += 1

            else:
                r.append(v2)
                i2 += 1

        return r

    def sort(values):
        l = len(values)

        if l < 2:
            return values

        r1 = sort(values[:l/2])
        r2 = sort(values[l/2:])

        return merge(r1, r2)

    return sort(values)


'''
--------------
Selection Sort
--------------
* Performance:
    Best:       O(n^2)
    Average:    O(n^2)
    Worst:      O(n^2)
* Space:        n
* Stable:       No

Seems like it should be stable but: (b[1], b[2], a, c) -> (a, b[2], b[1], c) after the first cycle
'''
def selection_sort(values):
    def swap(i,j):
        tmp = values[i]
        values[i] = values[j]
        values[j] = tmp

    l = len(values)

    for s in range(l):
        smallest = values[s]
        i_smallest = s
        for i in range(s+1,l):
            next_value = values[i]
            if next_value < smallest:
                smallest = next_value
                i_smallest = i

        swap(s,i_smallest)

    return values

