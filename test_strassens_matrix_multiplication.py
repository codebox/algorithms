import unittest
from strassens_matrix_multiplication import strassen_multiply

class TestArrayInversions(unittest.TestCase):

    def test_2_by_2(self):
        m1 = [[1,2], 
              [3,4]]
              
        m2 = [[5,6], 
              [7,8]]

        r = [[19, 22], 
             [43, 50]]
        self.assertEqual(strassen_multiply(m1, m2), r)
        
    def test_4_by_4(self):
        m1 = [[ 1, 2, 3, 4], 
              [ 5, 6, 7, 8], 
              [ 9,10,11,12], 
              [13,14,15,16]]

        m2 = [[17,18,19,20], 
              [21,22,23,24], 
              [25,26,27,28], 
              [29,30,31,32]]

        r = [[ 250, 260, 270, 280], 
             [ 618, 644, 670, 696], 
             [ 986,1028,1070,1112], 
             [1354,1412,1470,1528]]
        self.assertEqual(strassen_multiply(m1, m2), r)

if __name__ == '__main__':
    unittest.main()
