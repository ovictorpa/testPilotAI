from max_chain_length import *
import unittest

from chain import Pair, max_chain_length


class TestPair(unittest.TestCase):

    def test_init(self):
        a = 1
        b = 2
        pair = Pair(a, b)
        self.assertEqual(pair.a, a)
        self.assertEqual(pair.b, b)


class TestMaxChainLength(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_chain_length([], 0), 0)

    def test_single_element(self):
        self.assertEqual(max_chain_length([Pair(1, 2)], 1), 1)

    def test_valid_chains(self):
        pairs = [Pair(2, 3), Pair(1, 2), Pair(3, 4), Pair(4, 5)]
        self.assertEqual(max_chain_length(pairs, 4), 4)

    def test_invalid_chains(self):
        pairs = [Pair(2, 3), Pair(1, 2), Pair(3, 2), Pair(4, 5)]
        self.assertEqual(max_chain_length(pairs, 4), 3)

if __name__ == '__main__':
    unittest.main()