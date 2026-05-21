from sequence import *
import unittest

class TestSequence(unittest.TestCase):

    def test_base_cases(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)

    def test_small_numbers(self):
        self.assertEqual(sequence(3), 2)
        self.assertEqual(sequence(4), 3)

    def test_large_numbers(self):
        self.assertEqual(sequence(10), 55)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            sequence(-1)


if __name__ == '__main__':
    unittest.main()