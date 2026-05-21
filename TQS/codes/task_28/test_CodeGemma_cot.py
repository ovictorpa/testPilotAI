from max_height import *
import unittest

class TestMaxHeight(unittest.TestCase):

    # Test case for a tree with no nodes
    def test_empty_tree(self):
        root = None
        self.assertEqual(max_height(root), 0)

    # Test case for a tree with a single node
    def test_single_node_tree(self):
        root = Node(1)
        self.assertEqual(max_height(root), 1)

    # Test case for a tree with two nodes and the root node having the maximum height
    def test_two_nodes_root_max_height(self):
        root = Node(1)
        root.left = Node(2)
        self.assertEqual(max_height(root), 2)

    # Test case for a tree with two nodes and the left node having the maximum height
    def test_two_nodes_left_max_height(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertEqual(max_height(root), 2)

    # Test case for a tree with two nodes and the right node having the maximum height
    def test_two_nodes_right_max_height(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertEqual(max_height(root), 2)

    # Test case for a tree with multiple levels
    def test_multiple_levels(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        self.assertEqual(max_height(root), 3)

if __name__ == '__main__':
    unittest.main()