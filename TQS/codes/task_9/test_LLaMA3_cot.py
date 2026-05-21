from truncate_number import *
import unittest

class TestTruncateNumber(unittest.TestCase):

    def test_positive_number(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5, places=1)
        self.assertEqual(truncate_number(10.0), 0.0)

    def test_zero_input(self):
        self.assertAlmostEqual(truncate_number(0.0), 0.0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            truncate_number(-3.5)  # Assuming ValueError for invalid input

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            truncate_number("hello")  # Assuming TypeError for non-numeric input
        with self.assertRaises(TypeError):
            truncate_number([1, 2, 3])  # Assuming TypeError for non-numeric input

    def test_large_numbers(self):
        self.assertAlmostEqual(truncate_number(12345.6789), 0.6789, places=4)

if __name__ == '__main__':
    unittest.main()