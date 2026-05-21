from max_height import *
import unittest
from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_height(node: Optional[Node]) -> int:
    if node is None:
        return 0
    else:
        left_height = max_height(node.left)
        right_height = max_height(node.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

class TestMaxHeight(unittest.TestCase):
    def test_max_height_none(self):
        self.assertEqual(max_height(None), 0)

    def test_max_height_empty_node(self):
        self.assertEqual(max_height(Node(None)), 0)

    def test_max_height_single_node(self):
        node = Node("a")
        self.assertEqual(max_height(node), 1)

    def test_max_height_balanced_tree(self):
        root = Node("a")
        left = Node("b")
        right = Node("c")
        root.left = left
        root.right = right
        self.assertEqual(max_height(root), 2)

    def test_max_height_unbalanced_tree(self):
        root = Node("a")
        left = Node("b")
        right = Node("c")
        root.left = left
        root.right = right
        left.left = Node("d")
        left.right = Node("e")
        self.assertEqual(max_height(root), 3)