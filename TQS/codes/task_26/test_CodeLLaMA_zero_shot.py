from max_chain_length import *
import unittest
from collections import namedtuple

Pair = namedtuple('Pair', 'a, b')

class TestMaxChainLength(unittest.TestCase):
    def test_empty_list(self):
        arr = []
        n = 0
        self.assertEqual(max_chain_length(arr, n), 0)

    def test_single_element_list(self):
        arr = [Pair(1, 2)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_multiple_elements_list(self):
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 4)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_list_with_no_chains(self):
        arr = [Pair(1, 2), Pair(2, 4), Pair(3, 5)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 0)