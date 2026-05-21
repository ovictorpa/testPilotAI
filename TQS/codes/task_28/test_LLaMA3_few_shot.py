from max_height import *
import unittest
from binary_tree import Node, max_height  # Assuming the function is in a file named binary_tree.py

class TestMaxHeight(unittest.TestCase):

    def test_empty_tree(self):
        self.assertEqual(max_height(None), 0)

    def test_single_node_tree(self):
        node = Node(1)
        self.assertEqual(max_height(node), 1)

    def test_balanced_bst(self):
        # Construct a balanced binary search tree:
        #       4
        #      / \
        #     2   6
        #    / \   \
        #   1   3   5
        node = Node(4)
        node.left = Node(2)
        node.right = Node(6)
        node.left.left = Node(1)
        node.left.right = Node(3)
        node.right.right = Node(5)

        self.assertEqual(max_height(node), 3)

    def test_unbalanced_bst(self):
        # Construct an unbalanced binary search tree:
        #       10
        #      /
        #     20
        node = Node(10)
        node.left = Node(20)

        self.assertEqual(max_height(node), 2)

if __name__ == '__main__':
    unittest.main()