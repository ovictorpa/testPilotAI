from max_height import *
import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_height(node):
    if node is None:
        return 0
    else:
        left_height = max_height(node.left)
        right_height = max_height(node.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1


class TestMaxHeightFunction(unittest.TestCase):

    def test_empty_tree(self):
        # Create an empty tree (both children are None)
        node = Node(5)
        self.assertEqual(max_height(node), 0)

    def test_single_node_tree(self):
        # Create a single-node tree
        node = Node(5)
        self.assertEqual(max_height(node), 1)

    def test_balanced_binary_tree(self):
        # Create a balanced binary tree with nodes having values from 5 to 10
        root = Node(5)
        root.left = Node(6)
        root.right = Node(7)
        root.left.left = Node(8)
        root.left.right = Node(9)
        self.assertEqual(max_height(root), 3)

    def test_unbalanced_binary_tree_left_skewed(self):
        # Create a left-skewed binary tree with nodes having values from 5 to 10
        root = Node(5)
        root.left = Node(6)
        root.left.left = Node(7)
        self.assertEqual(max_height(root), 2)

    def test_unbalanced_binary_tree_right_skewed(self):
        # Create a right-skewed binary tree with nodes having values from 5 to 10
        root = Node(5)
        root.right = Node(6)
        root.right.right = Node(7)
        self.assertEqual(max_height(root), 2)

    def test_nested_binary_tree(self):
        # Create a nested binary tree with nodes having values from 5 to 15
        root = Node(5)
        root.left = Node(6)
        root.right = Node(7)
        root.left.left = Node(8)
        root.left.right = Node(9)
        root.left.left.left = Node(10)
        self.assertEqual(max_height(root), 3)

    def test_invalid_input(self):
        # Test if the function handles None input correctly
        with self.assertRaises(TypeError):
            max_height(None)

if __name__ == '__main__':
    unittest.main()