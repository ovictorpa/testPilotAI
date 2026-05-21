import unittest
from max_chain_length import max_chain_length, Pair

class TestMaxChainLength(unittest.TestCase):
    def test_empty_array(self):
        pairs = []
        self.assertEqual(max_chain_length(pairs, 0), 0)

    def test_single_element(self):
        pair = Pair(10, 5)
        pairs = [pair]
        self.assertEqual(max_chain_length(pairs, 1), 1)

    def test_no_chains(self):
        pairs = [Pair(2, 3), Pair(4, 5)]
        self.assertEqual(max_chain_length(pairs, 2), 0)

    def test_single_chain(self):
        pairs = [Pair(1, 2), Pair(3, 4)]
        self.assertEqual(max_chain_length(pairs, 2), 2)

    def test_multiple_chains_increasing(self):
        pairs = [Pair(1, 2), Pair(3, 5), Pair(7, 9)]
        self.assertEqual(max_chain_length(pairs, 3), 3)

    def test_multiple_chains_overlapping(self):
        pairs = [Pair(1, 3), Pair(6, 8), Pair(2, 5)]
        self.assertEqual(max_chain_length(pairs, 3), 3)

    def test_all_chains_in_one(self):
        pairs = [Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(4, 5)]
        self.assertEqual(max_chain_length(pairs, 4), 4)

    def test_longest_chain_with_gaps(self):
        pairs = [Pair(100, 2), Pair(3, 101), Pair(5, 102)]
        self.assertEqual(max_chain_length(pairs, 3), 3)

    def test_mixed_chains(self):
        pairs = [Pair(1, 4), Pair(7, 9), Pair(2, 3), Pair(5, 8)]
        self.assertEqual(max_chain_length(pairs, 4), 3)

    def test_complex_chains(self):
        pairs = [Pair(1, 10), Pair(12, 14), Pair(5, 6), Pair(7, 9)]
        self.assertEqual(max_chain_length(pairs, 4), 3)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            max_chain_length([], 0)
        with self.assertRaises(TypeError):
            max_chain_length(['a', 'b'], 2)

if __name__ == '__main__':
    unittest.main()