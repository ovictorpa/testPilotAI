from max_height import *
import unittest

class TestMaxHeight(unittest.TestCase):

    def test_empty_tree(self):
        self.assertEqual(max_height(None), 0)

    def test_single_node_tree(self):
        root = Node(1)
        self.assertEqual(max_height(root), 1)

    def test_balanced_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        self.assertEqual(max_height(root), 3)

    def test_unbalanced_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        self.assertEqual(max_height(root), 3)

if __name__ == '__main__':
    unittest.main()