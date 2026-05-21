from sequence import *
import unittest
from functools import lru_cache  # Added decorator to improve performance

@lru_cache(maxsize=None)  # Memoization with LRU cache
def sequence(n):
    if n == 1 or n == 2:
        return 1
    else:
        return sequence(sequence(n-1)) + sequence(n-sequence(n-1))

class TestSequence(unittest.TestCase):

    def test_sequence_one(self):
        self.assertEqual(sequence(1), 1)

    def test_sequence_two(self):
        self.assertEqual(sequence(2), 1)

    def test_sequence_three(self):
        self.assertEqual(sequence(3), 2)

    def test_sequence_four(self):
        self.assertEqual(sequence(4), 5)

    def test_sequence_negative(self):
        with self.assertRaises(ValueError):  # Assuming negative inputs are not supported
            sequence(-1)

if __name__ == '__main__':
    unittest.main()