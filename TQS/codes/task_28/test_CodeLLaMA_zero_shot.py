from max_height import *
import unittest

class TestMaxHeight(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(max_height(None), 0)

    def test_single_node_tree(self):
        node = Node(1)
        self.assertEqual(max_height(node), 1)

    def test_left_heavy_tree(self):
        node = Node(1)
        node.left = Node(2)
        self.assertEqual(max_height(node), 2)

    def test_right_heavy_tree(self):
        node = Node(1)
        node.right = Node(2)
        self.assertEqual(max_height(node), 2)

    def test_balanced_tree(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        self.assertEqual(max_height(node), 2)

if __name__ == '__main__':
    unittest.main()