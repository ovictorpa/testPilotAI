from sequence import *
[PYTHON]
import unittest

class TestSequence(unittest.TestCase):
    def test_sequence(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)
        self.assertEqual(sequence(3), 2)
        self.assertEqual(sequence(4), 3)
        self.assertEqual(sequence(5), 5)