import unittest
from huffman_encoding import encode

class TestHuffmanEncoding(unittest.TestCase):
    def test_1(self):
        r = encode('aaabc')
        self.assertEqual(r.letter_encodings, {'a': '1', 'c': '00', 'b': '01'})
        self.assertEqual(r.result_list, ['1', '1', '1', '01', '00'])

    def test_2(self):
        r = encode('aabbccdd')
        self.assertEqual(r.letter_encodings, {'a': '00', 'c': '01', 'b': '10', 'd': '11'})
        self.assertEqual(r.result_list, ['00', '00', '10', '10', '01', '01', '11', '11'])

    def test_2(self):
        r = encode('aaaaaaaabbbbccccddee')
        self.assertEqual(r.letter_encodings, {'a': '11', 'c': '00', 'b': '01', 'e': '100', 'd': '101'})
        self.assertEqual(r.result_list, ['11', '11', '11', '11', '11', '11', '11', '11', '01', '01', '01', '01', '00', '00', '00', '00', '101', '101', '100', '100'])

if __name__ == '__main__':
    unittest.main()
