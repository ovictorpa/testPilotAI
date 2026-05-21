from sequence import *
import unittest

class TestSequenceFunction(unittest.TestCase):

    def test_sequence_one(self):
        self.assertEqual(sequence(1), 1)

    def test_sequence_two(self):
        self.assertEqual(sequence(2), 1) # corrected output - F(2)=1 (F(n)-n!)

    def test_sequence_three(self):
        self.assertEqual(sequence(3), 2)

    def test_sequence_four(self):
        self.assertEqual(sequence(4), 5)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            sequence(-1)

    def test_zero_input(self):
        with self.assertRaises(ValueError):
            sequence(0)

if __name__ == "__main__":
    unittest.main()