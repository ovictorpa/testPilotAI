from max_chain_length import *
import unittest

class TestMaxChainLength(unittest.TestCase):

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 0)

    def test_single_element_array(self):
        arr = [Pair(1, 2)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_sorted_array(self):
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 4)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_unsorted_array(self):
        arr = [Pair(2, 3), Pair(1, 2), Pair(3, 4)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_duplicates(self):
        arr = [Pair(1, 2), Pair(2, 3), Pair(2, 4)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_large_array(self):
        arr = [Pair(i, i + 1) for i in range(1000)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1000)

if __name__ == '__main__':
    unittest.main()