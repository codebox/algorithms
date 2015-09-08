import unittest
from graph_data_structures import DirectedAdjacencyMatrix, DirectedAdjacencyList

class TestStructure(unittest.TestCase):

    def test_are_connected(self):
        self.assertEqual(self.m.are_connected(1,2), False)
        self.assertEqual(self.m.are_connected(2,1), False)
        self.m.connect(1,2)
        self.assertEqual(self.m.are_connected(1,2), True)
        self.assertEqual(self.m.are_connected(2,1), True)
        self.m.connect(1,2)
        self.assertEqual(self.m.are_connected(1,2), True)
        self.assertEqual(self.m.are_connected(2,1), True)

    def test_get_incoming(self):
        self.assertEqual(self.m.get_incoming(1), [])        
        self.m.connect(1,2)
        self.assertEqual(self.m.get_incoming(1), [])
        self.assertEqual(self.m.get_incoming(2), [1])
        self.m.connect(3,2)
        self.assertEqual(self.m.get_incoming(2), [1,3])
        self.m.connect(3,2)
        self.assertEqual(self.m.get_incoming(2), [1,3])

    def test_get_outgoing(self):
        self.assertEqual(self.m.get_outgoing(1), [])  
        self.m.connect(1,2)
        self.assertEqual(self.m.get_outgoing(1), [2])
        self.assertEqual(self.m.get_outgoing(2), [])
        self.m.connect(1,3)
        self.assertEqual(self.m.get_outgoing(1), [2,3])
        self.m.connect(1,3)
        self.assertEqual(self.m.get_outgoing(1), [2,3])
        
    def test_connect_disconnect(self):
        def are_connected(b):
            self.assertEqual(self.m.are_connected(1,2), b)
            self.assertEqual(self.m.are_connected(2,1), b)

        are_connected(False)

        self.m.connect(1,2) # 1 connection
        are_connected(True)
        
        self.m.disconnect(1,2) # 0 connections
        are_connected(False)
        
        self.m.disconnect(1,2) # 0 connections
        are_connected(False)
        
        self.m.connect(1,2) # 1 connection
        are_connected(True)

        self.m.connect(1,2) # 2 connections
        are_connected(True)

        self.m.disconnect(1,2) # 1 connection
        are_connected(True)

        self.m.disconnect(1,2) # 0 connections
        are_connected(False)

class TestDirectedAdjacencyMatrix(TestStructure):
    def setUp(self):
        self.m = DirectedAdjacencyMatrix(5)

class TestDirectedAdjacencyList(TestStructure):
    def setUp(self):
        self.m = DirectedAdjacencyList(5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDirectedAdjacencyMatrix)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDirectedAdjacencyList)
    unittest.TextTestRunner(verbosity=2).run(suite)
