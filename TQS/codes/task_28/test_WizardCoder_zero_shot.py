from max_height import *
import unittest

class TestMaxHeight(unittest.TestCase):
    def test_max_height(self):
        """
        Tests the max_height function with various inputs.
        """
        # Test case 1: node is None
        root = Node(None)
        self.assertEqual(0, max_height(root))
    
        # Test case 2: only left child exists
        left_child = Node("left")
        root = Node("node")
        root.left = left_child
        self.assertEqual(1, max_height(root))
    
        # Test case 3: only right child exists
        right_child = Node("right")
        root = Node("node")
        root.right = right_child
        self.assertEqual(1, max_height(root))
    
        # Test case 4: tree has height of 2
        left_child = Node("left")
        right_child = Node("right")
        root = Node("node")
        root.left = left_child
        root.right = right_child
        self.assertEqual(2, max_height(root))
    
        # Test case 5: tree has height of 3
        left_child1 = Node("left")
        left_child2 = Node("left1")
        right_child1 = Node("right")
        root = Node("node")
        root.left = left_child1
        left_child1.right = left_child2
        root.right = right_child1
        self.assertEqual(3, max_height(root))
    
if __name__ == '__main__':
    unittest.main()