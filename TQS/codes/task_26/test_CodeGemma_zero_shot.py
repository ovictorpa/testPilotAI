from max_chain_length import *
import unittest

class TestMaxChainLength(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(max_chain_length([], 0), 0)

    def test_single_element_array(self):
        pair = Pair(1, 2)
        self.assertEqual(max_chain_length([pair], 1), 1)

    def test_sorted_array(self):
        pairs = [Pair(i, i+1) for i in range(5)]
        self.assertEqual(max_chain_length(pairs, 5), 5)

    def test_unsorted_array(self):
        pairs = [Pair(2, 1), Pair(1, 3), Pair(3, 4)]
        self.assertEqual(max_chain_length(pairs, 3), 3)

if __name__ == '__main__':
    unittest.main()