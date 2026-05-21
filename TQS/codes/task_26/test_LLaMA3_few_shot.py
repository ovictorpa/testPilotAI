from max_chain_length import *
import unittest
from your_module import Pair, max_chain_length  # Import the Pair and max_chain_length functions

class TestMaxChainLength(unittest.TestCase):

    def test_max_chain_length_empty_array(self):
        arr = [Pair(1, 2), Pair(3, 4)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 0)

    def test_max_chain_length_single_element(self):
        arr = [Pair(5, 6)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_max_chain_length_no_connection(self):
        arr = [Pair(1, 2), Pair(3, 4)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 0)

    def test_max_chain_length_partial_connection(self):
        arr = [
            Pair(5, 6),
            Pair(7, 8),
            Pair(9, 10),
            Pair(11, 12),
        ]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_max_chain_length_full_connection(self):
        arr = [
            Pair(5, 6),
            Pair(7, 8),
            Pair(9, 10),
            Pair(11, 12),
            Pair(13, 14),
        ]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 4)

    def test_max_chain_length_negative_values(self):
        with self.assertRaises(ValueError):
            max_chain_length([Pair(-1, -2), Pair(3, 4)], 2)

    def test_max_chain_length_invalid_input(self):
        with self.assertRaises(TypeError):
            max_chain_length("hello", 5)

if __name__ == '__main__':
    unittest.main()