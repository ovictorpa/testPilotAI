from max_height import *
import unittest
from node import Node

class TestMaxHeight(unittest.TestCase):
    def test_empty_tree(self):
        tree = Node(None)
        self.assertEqual(max_height(tree), 0)

    def test_single_node_tree(self):
        tree = Node(1)
        self.assertEqual(max_height(tree), 1)

    def test_balanced_tree(self):
        tree = Node(1, Node(2), Node(3))
        self.assertEqual(max_height(tree), 2)

    def test_unbalanced_tree(self):
        tree = Node(1, Node(2, Node(4), None), Node(3))
        self.assertEqual(max_height(tree), 3)