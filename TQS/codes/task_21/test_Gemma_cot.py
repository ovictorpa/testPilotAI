from sequence import *
import unittest

class TestSequence(unittest.TestCase):

    def test_base_case_1(self):
        self.assertEqual(sequence(1), 1)

    def test_base_case_2(self):
        self.assertEqual(sequence(2), 1)

    def test_recursive_case(self):
        self.assertEqual(sequence(3), 2)
        self.assertEqual(sequence(4), 3)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            sequence(-1)

    def test_large_input(self):
        with self.assertRaises(StackOverflowError):
            sequence(21)

if __name__ == '__main__':
    unittest.main()