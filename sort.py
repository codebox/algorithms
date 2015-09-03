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
Merge Sort is more efficient than Quick Sort for some types of lists if the data to be sorted can only 
be efficiently accessed sequentially, and is thus popular in languages such as Lisp, where sequentially 
accessed data structures are very common. Unlike some (efficient) implementations of Quick Sort, 
Merge Sort is a stable sort.

Summary: recursive, keep splitting the list into 2 halves, sort each half then merge them back together.
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
Selection Sort is noted for its simplicity, and it has performance advantages over more complicated algorithms 
in certain situations, particularly where auxiliary memory is limited. It generally performs worse than the 
similar Insertion Sort. 

Summary: step through all unsorted items, find the smallest one, swap it with the left-most item and repeat
'''
def selection_sort(values):
    l = len(values)

    for s in range(l):
        smallest = values[s]
        i_smallest = s
        for i in range(s+1,l):
            next_value = values[i]
            if next_value < smallest:
                smallest = next_value
                i_smallest = i

        s, i_smallest = i_smallest, s

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
Insertion Sort is one of the fastest algorithms for sorting very small arrays, even faster than Quick Sort; 
indeed, good Quick Sort implementations use Insertion Sort for arrays smaller than a certain threshold, also 
when arising as subproblems; the exact threshold must be determined experimentally and depends on the machine, 
but is commonly around ten.

Summary: step through the unsorted items, insert each one at the correct place within the sorted part of the list
'''
def insertion_sort(values):
    l = len(values)
    for i in range(1, l): 
        j = i - 1 # j is the index of largest sorted element
        while j >= 0 and values[i] < values[j]:
            j -= 1
        values.insert(j+1, values.pop(i))

    return values

'''
-----------
Bubble Sort
-----------
* Performance:
    Best:       O(n)
    Average:    O(n^2)
    Worst:      O(n^2)
* Space:        n
* Stable:       Yes

Notes (from https://en.wikipedia.org/wiki/Bubble_sort)
-----
Even other О(n^2) sorting algorithms, such as Insertion Sort, tend to have better performance than Bubble Sort. 
Therefore, Bubble Sort is not a practical sorting algorithm when n is large. The only significant advantage that 
Bubble Sort has over most other implementations, even Quick Sort (but not Insertion Sort), is that the ability 
to detect that the list is sorted is efficiently built into the algorithm. When the list is already sorted 
(best-case), the complexity of Bubble Sort is only O(n).

Summary: compare adjacent pairs of items, swap if they are in the wrong order, keep repeating for unsorted part of list
'''
def bubble_sort(values):
    l = len(values)

    for i in range(l): 
        for j in range(i+1, l):
            if values[i] > values[j]:
                values[i], values[j] = values[j], values[i]

    return values
