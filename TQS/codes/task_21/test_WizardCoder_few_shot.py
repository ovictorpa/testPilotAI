from sequence import *
import unittest

def sequence(n):
    if n == 1 or n == 2: 
        return 1
    else: 
        return sequence(n-1) + sequence(n-sequence(n-1))

class TestSequence(unittest.TestCase):
    def test_sequence(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)
        self.assertEqual(sequence(3), 1)
        self.assertEqual(sequence(4), 2)
        self.assertEqual(sequence(5), 3)
        self.assertEqual(sequence(6), 5)
        self.assertEqual(sequence(7), 8)
        with self.assertRaises(RecursionError):
            sequence(0)