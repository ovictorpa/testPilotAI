from max_chain_length import *
import unittest

class TestMaxChainLength(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(max_chain_length([], 0), 0)

    def test_all_equal(self):
        arr = [Pair('a', 'a') for _ in range(5)]
        self.assertEqual(max_chain_length(arr, 5), 1)

    def test_different_values(self):
        arr = [Pair('a', 'b') for _ in range(5)]
        self.assertEqual(max_chain_length(arr, 5), 2)

    def test_cycle_of_length_1(self):
        arr = [Pair('a', 'b'), Pair('b', 'c'), Pair('c', 'a')]
        self.assertEqual(max_chain_length(arr, 3), 2)

    def test_cycle_of_length_2(self):
        arr = [Pair('a', 'b'), Pair('b', 'c'), Pair('c', 'd'), Pair('d', 'a')]
        self.assertEqual(max_chain_length(arr, 4), 3)

    def test_cycle_of_length_3(self):
        arr = [Pair('a', 'b'), Pair('b', 'c'), Pair('c', 'd'), Pair('d', 'e'), Pair('e', 'a')]
        self.assertEqual(max_chain_length(arr, 5), 4)

    def test_multiple_cycles(self):
        arr = [Pair('a', 'b'), Pair('b', 'c'), Pair('c', 'd'), Pair('d', 'e'), Pair('e', 'f'), Pair('f', 'g'), Pair('g', 'h'), Pair('h', 'i'), Pair('i', 'j')]
        self.assertEqual(max_chain_length(arr, 9), 5)