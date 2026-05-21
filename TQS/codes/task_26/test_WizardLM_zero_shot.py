from max_chain_length import *
import unittest
from typing import List, Tuple
from your_module import Pair, max_chain_length  # Replace 'your_module' with the actual module name where the functions are defined.

class TestMaxChainLength(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(max_chain_length([], 0), 0)

    def test_single_element(self):
        self.assertEqual(max_chain_length([Pair(5, 3)), 1], 1)

    def test_no_chains_possible(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(3, 1), Pair(2, 4), Pair(5, 6)), 4], 1)

    def test_simple_chain(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(2, 1), Pair(3, 4), Pair(4, 3), Pair(5, 6)), 5], 3)

    def test_multiple_chains(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(3, 1), Pair(5, 6), Pair(7, 8), Pair(9, 10)], 5), 3)

    def test_chains_with_gaps(self):
        self.assertEqual(max_chain_length([Pair(2, 1), Pair(4, 3), Pair(6, 5), Pair(8, 7), Pair(10, 9)], 5), 3)

    def test_longest_chain_in_middle(self):
        self.assertEqual(max_chain_length([Pair(2, 1), Pair(5, 4), Pair(8, 7), Pair(9, 6), Pair(10, 8)], 5), 3)

    def test_all_pairs_in_a_chain(self):
        self.assertEqual(max_chain_length([Pair(i, i-1) for i in range(1, 6)], 4), 4)

    def test_overlapping_chains(self):
        self.assertEqual(max_chain_length([Pair(1, 2), Pair(3, 1), Pair(5, 4), Pair(4, 3), Pair(6, 5), Pair(7, 8)], 6), 3)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            max_chain_length([Pair(1, 2), Pair(3, 1)], 0)  # Invalid input: empty list as the second argument.

    def test_large_dataset(self):
        large_dataset = [Pair(i+j, i) for j in range(1, 6) for i in range(1, 6)]
        self.assertEqual(max_chain_length(large_dataset, len(large_dataset)), len(large_dataset))

if __name__ == '__main__':
    unittest.main()