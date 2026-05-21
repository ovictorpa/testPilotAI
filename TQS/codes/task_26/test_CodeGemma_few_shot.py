from max_chain_length import *
import unittest

class TestMaxChainLength(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(max_chain_length([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(max_chain_length([Pair(1, 1)], 1), 1)

    def test_sorted_array(self):
        arr = [Pair(1, 2), Pair(3, 4), Pair(5, 6)]
        self.assertEqual(max_chain_length(arr, 3), 3)

    def test_unsorted_array(self):
        arr = [Pair(2, 1), Pair(4, 3), Pair(6, 5)]
        self.assertEqual(max_chain_length(arr, 3), 3)

    def test_large_array(self):
        arr = [Pair(i, i + 1) for i in range(1000)]
        self.assertEqual(max_chain_length(arr, 1000), 1000)

if __name__ == '__main__':
    unittest.main()