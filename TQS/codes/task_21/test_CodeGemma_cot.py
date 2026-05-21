from sequence import *
import unittest

class SequenceTest(unittest.TestCase):

    def test_base_case_1(self):
        self.assertEqual(sequence(1), 1)

    def test_base_case_2(self):
        self.assertEqual(sequence(2), 1)

    def test_recursive_case(self):
        self.assertEqual(sequence(3), 2)

    def test_large_input(self):
        self.assertEqual(sequence(10), 1023)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            sequence(-1)

    def test_float_input(self):
        with self.assertRaises(TypeError):
            sequence(1.5)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            sequence(1.5)

if __name__ == '__main__':
    unittest.main()