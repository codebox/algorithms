'''
-------------------------
Counting Array Inversions
-------------------------
An array inversion is defined as a single pair of elements A[i] and A[j] in the array 'A' 
such that i < j but A[i] > A[j].

This implementation runs in O(n log n) time, and uses a recursive approach similar to Merge Sort in order
to efficiently count the number of split inversions resulting from dividing the input array in two.
'''
def count_inversions(values):
    def sort_and_count_inversions(values):
        l = len(values)

        if l <= 1:
            return values, 0
        
        v1 = values[:l/2]
        v2 = values[l/2:]

        sorted_v1, c1 = sort_and_count_inversions(v1)
        sorted_v2, c2 = sort_and_count_inversions(v2)

        sorted_values, c3 = merge_and_count_split_inversions(sorted_v1, sorted_v2)

        return sorted_values, c1 + c2 + c3

    def merge_and_count_split_inversions(l1, l2):
        END_OF_LIST = object()
        inversion_count = 0

        def list_get(l, i):
            if len(l) <= i:
                return END_OF_LIST
            return l[i]

        i1 = i2 = 0
        l1_len = len(l1)
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

            elif v1 <= v2:
                r.append(v1)
                i1 += 1

            else:
                r.append(v2)
                inversion_count += (l1_len - i1)
                i2 += 1

        return r, inversion_count

    return sort_and_count_inversions(values)[1]
 