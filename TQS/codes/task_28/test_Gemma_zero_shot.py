import unittest

from solution import Node
from max_height import max_height

class TestMaxHeight(unittest.TestCase):

    def test_empty_tree(self):
        self.assertEqual(max_height(None), 0)

    def test_single_node(self):
        node = Node(1)
        self.assertEqual(max_height(node), 1)

    def test_balanced_tree(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        self.assertEqual(max_height(node), 2)

    def test_unbalanced_tree(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(4)
        self.assertEqual(max_height(node), 3)

if __name__ == '__main__':
    unittest.main()