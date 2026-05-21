from max_height import *
import unittest
from node import Node

class TestMaxHeight(unittest.TestCase):
    
    def setUp(self):
        self.node1 = Node("Root")
        self.node2 = Node("Left")
        self.node3 = Node("Right")
        self.node4 = Node("Left-Left")
        self.node5 = Node("Right-Right")
        
    def test_max_height_one(self):
        """Test max height with one node."""
        self.node1.left = self.node2
        self.assertEqual(max_height(self.node1), 1)
        
    def test_max_height_two(self):
        """Test max height with two nodes in tree."""
        self.node1.left = self.node2
        self.node1.right = self.node3
        self.assertEqual(max_height(self.node1), 2)
        
    def test_max_height_three(self):
        """Test max height with three nodes in tree."""
        self.node1.left = self.node2
        self.node1.right = self.node3
        self.node2.left = self.node4
        self.assertEqual(max_height(self.node1), 2)
    
    def test_max_height_four(self):
        """Test max height with four nodes in tree."""
        self.node1.left = self.node2
        self.node1.right = self.node3
        self.node2.left = self.node4
        self.node2.right = self.node5
        self.assertEqual(max_height(self.node1), 2)
    
    def test_max_height_none(self):
        """Test max height with an empty tree."""
        self.assertIsNone(max_height(None))
        
    def test_max_height_one_node(self):
        """Test max height of a single node is zero."""
        self.assertEqual(max_height(Node("Root")), 0)
        
if __name__ == '__main__':
    unittest.main()