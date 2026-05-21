from max_height import *
import unittest
from your_module import Node, max_height  # Replace 'your_module' with the actual module name

class TestMaxHeight(unittest.TestCase):
    def setUp(self):
        self.null_node = None
        self.single_node = Node(1)
        self.empty_left_tree = Node(2, left=None)
        self.empty_right_tree = Node(3, right=None)
        self.balanced_tree = Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, left=Node(6)))
        self.skewed_left_tree = Node(1, left=Node(2, left=Node(4), right=Node(7)))
        self.skewed_right_tree = Node(1, right=Node(3, right=Node(5, left=Node(6))))
        self.complete_binary_tree = Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, left=Node(6), right=Node(7)))
        self.mixed_heights_tree = Node(1, left=Node(2, left=Node(4), right=Node(6)), right=Node(3, left=Node(7), right=Node(8, left=Node(9))))
        self.duplicate_values_tree = Node(1, left=Node(1, left=Node(1)), right=Node(2))
        self.leaf_node_other_than_root = Node(1, left=Node(2), right=Node(3))

    def test_empty_tree(self):
        self.assertEqual(max_height(self.null_node), 0)

    def test_single_node(self):
        self.assertEqual(max_height(self.single_node), 1)

    def test_leaf_node_other_than_root(self):
        self.assertEqual(max_height(self.leaf_node_other_than_root), 2)

    def test_balanced_tree(self):
        self.assertEqual(max_height(self.balanced_tree), 2)

    def test_skewed_left_tree(self):
        self.assertEqual(max_height(self.skewed_left_tree), 3)

    def test_skewed_right_tree(self):
        self.assertEqual(max_height(self.skewed_right_tree), 3)

    def test_complete_binary_tree(self):
        self.assertEqual(max_height(self.complete_binary_tree), 2)

    def test_mixed_heights_tree(self):
        self.assertEqual(max_height(self.mixed_heights_tree), 3)

    def test_duplicate_values_tree(self):
        self.assertEqual(max_height(self.duplicate_values_tree), 2)

if __name__ == '__main__':
    unittest.main()