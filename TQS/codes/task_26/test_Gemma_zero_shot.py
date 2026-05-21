from max_chain_length import *
import unittest

from chain_length import Pair, max_chain_length


class TestMaxChainLength(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_chain_length([], 0), 0)

    def test_single_pair(self):
        self.assertEqual(max_chain_length([Pair(1, 2)], 1), 1)

    def test_two_pairs(self):
        self.assertEqual(max_chain_length([Pair(1, 3), Pair(2, 3)], 2), 2)

    def test_three_pairs(self):
        self.assertEqual(max_chain_length([Pair(1, 3), Pair(2, 3), Pair(3, 4)], 3), 3)

    def test_large_input(self):
        pairs = [Pair(i, i+1) for i in range(100)]
        self.assertEqual(max_chain_length(pairs, len(pairs)), len(pairs))


if __name__ == '__main__':
    unittest.main()