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


class TestMaxHeight(unittest.TestCase):

    def test_empty_tree(self):
        self.assertEqual(max_height(None), 0)

    def test_single_node(self):
        node = Node(1)
        self.assertEqual(max_height(node), 1)

    def test_left_subtree_greater(self):
        node = Node(1)
        node.left = Node(2)
        node.left.left = Node(3)
        self.assertEqual(max_height(node), 2)

    def test_right_subtree_greater(self):
        node = Node(1)
        node.right = Node(2)
        node.right.right = Node(3)
        self.assertEqual(max_height(node), 2)

    def test_balanced_tree(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        self.assertEqual(max_height(node), 1)

if __name__ == '__main__':
    unittest.main()