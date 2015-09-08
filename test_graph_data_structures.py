import unittest
from graph_data_structures import DirectedAdjacencyMatrix

class TestDirectedAdjacencyMatrix(unittest.TestCase):

    def test_are_connected(self):
        m = DirectedAdjacencyMatrix(5)

        self.assertEqual(m.are_connected(1,2), False)
        self.assertEqual(m.are_connected(2,1), False)
        m.connect(1,2)
        self.assertEqual(m.are_connected(1,2), True)
        self.assertEqual(m.are_connected(2,1), True)
        m.connect(1,2)
        self.assertEqual(m.are_connected(1,2), True)
        self.assertEqual(m.are_connected(2,1), True)

    def test_get_incoming(self):
        m = DirectedAdjacencyMatrix(5)

        self.assertEqual(m.get_incoming(1), [])        
        m.connect(1,2)
        self.assertEqual(m.get_incoming(1), [])
        self.assertEqual(m.get_incoming(2), [1])
        m.connect(3,2)
        self.assertEqual(m.get_incoming(2), [1,3])
        m.connect(3,2)
        self.assertEqual(m.get_incoming(2), [1,3])

    def test_get_outgoing(self):
        m = DirectedAdjacencyMatrix(5)

        self.assertEqual(m.get_outgoing(1), [])  
        m.connect(1,2)
        self.assertEqual(m.get_outgoing(1), [2])
        self.assertEqual(m.get_outgoing(2), [])
        m.connect(1,3)
        self.assertEqual(m.get_outgoing(1), [2,3])
        m.connect(1,3)
        self.assertEqual(m.get_outgoing(1), [2,3])
        
    def test_connect_disconnect(self):
        def are_connected(b):
            self.assertEqual(m.are_connected(1,2), b)
            self.assertEqual(m.are_connected(2,1), b)

        m = DirectedAdjacencyMatrix(5)

        are_connected(False)

        m.connect(1,2) # 1 connection
        are_connected(True)
        
        m.disconnect(1,2) # 0 connections
        are_connected(False)
        
        m.disconnect(1,2) # 0 connections
        are_connected(False)
        
        m.connect(1,2) # 1 connection
        are_connected(True)

        m.connect(1,2) # 2 connections
        are_connected(True)

        m.disconnect(1,2) # 1 connection
        are_connected(True)

        m.disconnect(1,2) # 0 connections
        are_connected(False)

if __name__ == '__main__':
    unittest.main()
