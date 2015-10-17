def encode(input):
    chars = list(input)
    char_map = {}
    tree_root_node = None

    for char in chars:
        if not char_map.has_key(char):
            char_map[char] = 0
        char_map[char] += 1

    counts = CharCounts()
    for letter, count in char_map.iteritems():
        counts.add_new(CharCount(letter, count, None))

    while counts.get_size() > 1:
        char1 = counts.extract_min()
        char2 = counts.extract_min()

        counts.add_new(char1.merge(char2))

    return Result(input, counts.counts[0].node)

class Result:
    def __init__(self, original_string, root_node):
        self.letter_encodings = {}

        for l in set(list(original_string)):
            self.letter_encodings[l] = root_node.find(l)

        self.result_list = map(lambda l : self.letter_encodings[l], list(original_string))

class CharCount:
    def __init__(self, letters, count, node):
        self.letters = letters
        self.count = count
        self.node = node if node else letters

    def merge(self, other):
        new_node = TreeNode(self.node, other.node)
        return CharCount(self.letters + other.letters, self.count + other.count, new_node)

class CharCounts:
    def __init__(self):
        self.counts = []

    def extract_min(self):
        # better to use a heap for this
        min_count = min(self.counts, key=lambda c : c.count)
        self.counts.remove(min_count)
        return min_count

    def add_new(self, char_count):
        self.counts.append(char_count)

    def get_size(self):
        return len(self.counts)

class TreeNode:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def find(self, value):
        if type(self.l) is str:
            if self.l == value:
                return '0'
        else:
            child_result = self.l.find(value)
            if child_result is not None:
                return '0' + child_result

        if type(self.r) is str:
            if self.r == value:
                return '1'
        else:
            child_result = self.r.find(value)
            if child_result is not None:
                return '1' + child_result

        return None
