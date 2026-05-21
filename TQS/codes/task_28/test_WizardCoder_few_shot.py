from max_height import *
import unittest

class TestMaxHeight(unittest.TestCase):
    
    def test_max_height(self):
        node = Node(5)
        self.assertEqual(max_height(node), 1) # root node only, height is 1

        node = Node(5)
        node.left = Node(3)
        node.right = Node(7)
        self.assertEqual(max_height(node), 2) # binary tree with single path, height is 2
    
        node = Node(10)
        node.left = Node(5)
        node.right = Node(15)
        node.left.left = Node(3)
        self.assertEqual(max_height(node), 3) # binary tree with two paths, height is 3
    
        node = Node(4)
        node.left = Node(2)
        node.right = Node(7)
        node.left.left = Node(1)
        self.assertEqual(max_height(node), 3) # binary tree with two paths, height is 3
    
        node = Node(8)
        node.left = Node(5)
        node.right = Node(7)
        node.right.left = Node(6)
        self.assertEqual(max_height(node), 2) # binary tree with two paths, height is 2
    
        node = Node(8)
        node.left = Node(5)
        node.right = Node(7)
        node.right.right = Node(9)
        self.assertEqual(max_height(node), 3) # binary tree with three paths, height is 3
    
        node = Node(8)
        node.left = Node(5)
        node.right = Node(7)
        node.right.left = Node(6)
        node.right.right = Node(9)
        self.assertEqual(max_height(node), 3) # binary tree with three paths, height is 3
    
if __name__ == '__main__':
    unittest.main()