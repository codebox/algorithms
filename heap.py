import sys

MAX_INT = sys.maxint
'''
Heap data structure
-------------------
Maintains a balanced binary tree, where the value of each node is never larger than the values of its children.
The tree is represented using an array, since it is easy to calculate the index of the parent/child of a given
element (see __find_parent_index/__find_child_indexes)
'''
class Heap:
    def __init__(self):
        self.l = []

    def insert(self, value):
        self.l.append(value)
        index_of_value = len(self.l) - 1

        while index_of_value:
            index_of_parent = self.__find_parent_index(index_of_value)
            value_of_parent = self.l[index_of_parent]
            if value_of_parent > value:
                self.__swap(index_of_value, index_of_parent)
                index_of_value = index_of_parent
            else:
                break


    def extract_min(self):
        count = len(self.l)
        if count == 0:
            return None

        min_value = self.l.pop(0)
        count -= 1
        if count == 0:
            return min_value

        last_value = self.l.pop(count - 1)
        self.l.insert(0, last_value)

        i = 0
        value = last_value

        while True:
            i1, i2 = self.__find_child_indexes(i)

            v1 = MAX_INT if i1 is None else self.l[i1]
            v2 = MAX_INT if i2 is None else self.l[i2]

            if value <= min(v1, v2):
                break

            elif v1 <= v2:
                self.__swap(i1, i)
                i = i1
            else:
                self.__swap(i2, i)
                i = i2

        return min_value

    def __swap(self, i1, i2):
        self.l[i1], self.l[i2] = self.l[i2], self.l[i1]

    def __find_parent_index(self, i):
        return i / 2 # Python discards remainders for integer division, which is what we need here

    def __find_child_indexes(self, i):
        max_index = len(self.l) - 1
        i1 = i*2
        i2 = i1 + 1

        if i1 > max_index:
            return None, None
        else:
            return i1, None if i2 > max_index else i2