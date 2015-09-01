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

Notes (from https://en.wikipedia.org/wiki/Merge_sort)
-----
Merge sort is more efficient than quicksort for some types of lists if the data to be sorted can only be efficiently accessed sequentially, and is thus popular in languages such as Lisp, where sequentially accessed data structures are very common. Unlike some (efficient) implementations of quicksort, merge sort is a stable sort.
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

This sort seems like it should be stable but: (b[1], b[2], a, c) -> (a, b[2], b[1], c) after the first cycle

Notes (from https://en.wikipedia.org/wiki/Selection_sort)
-----
Selection sort is noted for its simplicity, and it has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory is limited. It generally performs worse than the similar Insertion Sort. 
'''
def selection_sort(values):
    def swap(i,j):
        values[i], values[j] = values[j], values[i]

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

'''
--------------
Insertion Sort
--------------
* Performance:
    Best:       O(n)
    Average:    O(n^2)
    Worst:      O(n^2)
* Space:        n
* Stable:       Yes

Notes (from https://en.wikipedia.org/wiki/Insertion_sort)
-----
Insertion sort is one of the fastest algorithms for sorting very small arrays, even faster than quicksort; indeed, good quicksort implementations use insertion sort for arrays smaller than a certain threshold, also when arising as subproblems; the exact threshold must be determined experimentally and depends on the machine, but is commonly around ten.
'''
def insertion_sort(values):
    l = len(values)
    for i in range(1, l): 
        j = i - 1 # j is the index of largest sorted element
        while j >= 0 and values[i] < values[j]:
            j -= 1
        values.insert(j+1, values.pop(i))

    return values
