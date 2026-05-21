from max_chain_length import *
import unittest
from typing import List, Tuple

class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class TestMaxChainLength(unittest.TestCase):
    def test_empty_array(self):
        arr = []
        n = 0
        self.assertEqual(max_chain_length(arr, n), 0)

    def test_single_element(self):
        arr = [Pair(1, 1)]
        n = 1
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_non_comparable_elements(self):
        arr = [Pair('a', 'b'), Pair(3, 2)]
        n = 2
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_all_pairs_comparable(self):
        arr = [Pair(1, 0), Pair(3, 2), Pair(4, 1)]
        n = 3
        self.assertEqual(max_chain_length(arr, n), 2)

    def test_no_chains_formed(self):
        arr = [Pair(5, 4), Pair(3, 2), Pair(1, 6)]
        n = 3
        self.assertEqual(max_chain_length(arr, n), 0)

    def test_trivial_chains(self):
        arr = [Pair(1, 0), Pair(0, 1)] * 5
        n = 5
        self.assertEqual(max_chain_length(arr, n), 4)

    def test_multiple_chains(self):
        arr = [Pair(1, 0), Pair(2, 1), Pair(3, 2), Pair(4, 3)]
        n = 4
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_mixed_array(self):
        arr = [Pair(5, 4), Pair('a', 'b'), Pair(3, 2)]
        n = 3
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_descending_subsequences(self):
        arr = [Pair(4, 5), Pair(3, 4), Pair(2, 3)]
        n = 3
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_large_inputs(self):
        arr = [Pair(i, i-1) for i in range(1000, 0, -1)]
        n = 1000
        self.assertEqual(max_chain_length(arr, n), 999)

    def test_optimization(self):
        arr = [Pair(1, 0), Pair(3, 2), Pair(6, 5)]
        n = 3
        self.assertEqual(max_chain_length(arr, n), 2)

    def test_large_input_with_duplicates(self):
        arr = [Pair(i, i-1) for i in range(1000)] + [Pair(1001, 1000)]
        n = 1001
        self.assertEqual(max_chain_length(arr, n), 1000)

if __name__ == '__main__':
    unittest.main()