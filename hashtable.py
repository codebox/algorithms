'''
Hash Table
----------
Hash table implementation providing constant-time performance for insertion/retrieval assuming reasonable choice
of bucket_count (bucket counts should be prime and not too close to powers of 2 or 10) and non-pathological data.
Keys should be strings, values can be of any type.
'''

class HashTable:
    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [None] * bucket_count

    def put(self, key, value):
        n = self.__get_bucket_for_key(key)
        if not self.buckets[n]:
            self.buckets[n] = []
        self.buckets[n].append((key, value))

    def get(self, key):
        n = self.__get_bucket_for_key(key)
        bucket_contents = self.buckets[n]
        value = None

        if bucket_contents:
            for item in bucket_contents:
                if item[0] == key:
                    value = item[1]
                    break

        return value

    def __get_bucket_for_key(self, key):
        hash_value = reduce(lambda x,y : x * 37 + y, map(ord, list(key)), 0)
        return hash_value % self.bucket_count

