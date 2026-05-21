from max_chain_length import *
import unittest

class TestMaxChainLength(unittest.TestCase):

    def test_empty_array(self):
        arr = []
        n = 0
        self.assertEqual(max_chain_length(arr, n), 0)

    def test_single_element_array(self):
        arr = [Pair(1, 2)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_multiple_chains(self):
        # Test case 1: Two pairs can be chained together
        arr = [Pair(3, 5), Pair(4, 6)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 2)

        # Test case 2: Three pairs can be chained together
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 4)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_optimal_chain(self):
        # Test case: One optimal chain with length 5
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5), Pair(5, 6)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 5)

    def test_no_optimal_chain(self):
        # Test case: No optimal chain
        arr = [Pair(1, 2), Pair(3, 4), Pair(5, 6)]
        n = len(arr)
        self.assertLessEqual(max_chain_length(arr, n), 1)

    def test_negative_numbers(self):
        # Test case: Array with negative numbers
        arr = [Pair(-1, 0), Pair(2, -3), Pair(-4, 5)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 2)

if __name__ == '__main__':
    unittest.main()