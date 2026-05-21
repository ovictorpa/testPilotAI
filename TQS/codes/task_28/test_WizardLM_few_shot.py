from max_height import *
import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class TestMaxHeight(unittest.TestCase):
    def setUp(self):
        self.empty_node = None
        self.single_node = Node(1)
        self.balanced_tree = Node(3)
        self.balanced_tree.left = Node(2)
        self.balanced_tree.right = Node(4)
        self.unbalanced_left_tree = Node(1)
        self.unbalanced_left_tree.left = Node(2)
        self.unbalanced_left_tree.left.left = Node(3)
        self.unbalanced_left_tree.left.left.left = Node(4)
        self.unbalanced_right_tree = Node(5)
        self.unbalanced_right_tree.right = Node(6)
        self.unbalanced_right_tree.right.right = Node(7)
        self.unbalanced_right_tree.right.right.right = Node(8)
        self.mixed_heights_tree = Node(1)
        self.mixed_heights_tree.left = Node(2, left=Node(3), right=Node(4))
        self.mixed_heights_tree.right = Node(5, left=Node(6), right=Node(7))
        self.subtree_node = Node(9)
        self.subtree_node.left = Node(10, left=Node(11))
        self.subtree_node.right = Node(12)

    def test_max_height_empty_tree(self):
        self.assertEqual(max_height(self.empty_node), 0)

    def test_max_height_single_node(self):
        self.assertEqual(max_height(self.single_node), 1)

    def test_max_height_balanced_tree(self):
        self.assertEqual(max_height(self.balanced_tree), 2)

    def test_max_height_unbalanced_left_heavy_tree(self):
        self.assertEqual(max_height(self.unbalanced_left_tree), 3)

    def test_max_height_unbalanced_right_heavy_tree(self):
        self.assertEqual(max_height(self.unbalanced_right_tree), 4)

    def test_max_height_mixed_heights_tree(self):
        self.assertEqual(max_height(self.mixed_heights_tree), 2)

    def test_max_height_subtree(self):
        self.assertEqual(max_height(self.subtree_node.left), 1)
        self.assertEqual(max_height(self.subtree_node.right), 1)
        self.assertEqual(max_height(self.subtree_node), 2)

    def test_max_height_large_tree(self):
        large_tree = Node(1)
        large_tree.left = Node(2, left=Node(3, left=Node(4)))
        large_tree.right = Node(5, right=Node(6, right=Node(7)))
        self.assertEqual(max_height(large_tree), 3)

if __name__ == '__main__':
    unittest.main()