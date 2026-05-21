from max_height import *
import unittest

class TestMaxHeightFunction(unittest.TestCase):

    # Create a test Node for an empty tree
    def test_empty_tree(self):
        node = None
        self.assertEqual(max_height(node), 0)

    # Create a test Node with one child on the left
    def test_single_left_child(self):
        node1 = Node(5)
        node2 = Node(10)
        node1.left = node2
        self.assertEqual(max_height(node1), 2)

    # Create a test Node with one child on the right
    def test_single_right_child(self):
        node1 = Node(5)
        node2 = Node(10)
        node1.right = node2
        self.assertEqual(max_height(node1), 2)

    # Create a test Node with two children (left and right)
    def test_balanced_tree(self):
        node1 = Node(5)
        node2 = Node(10)
        node3 = Node(15)
        node4 = Node(8)
        node1.left = node2
        node1.right = node3
        node2.left = node4
        self.assertEqual(max_height(node1), 3)

    # Create a test Node with left subtree that is taller than the right subtree
    def test_left_subtree_taller(self):
        node1 = Node(5)
        node2 = Node(10)
        node3 = Node(15)
        node4 = Node(8)
        node1.left = node2
        node1.right = node3
        node2.left = node4
        self.assertEqual(max_height(node1), 3)

    # Create a test Node with right subtree that is taller than the left subtree
    def test_right_subtree_taller(self):
        node1 = Node(5)
        node2 = Node(10)
        node3 = Node(15)
        node4 = Node(8)
        node1.left = node2
        node1.right = node3
        node3.left = node4
        self.assertEqual(max_height(node1), 3)

if __name__ == '__main__':
    unittest.main()