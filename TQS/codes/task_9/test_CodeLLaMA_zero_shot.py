from truncate_number import *
import unittest

class TestTruncateNumber(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(truncate_number(3.5), 0.5)
        self.assertEqual(truncate_number(4.7), 0.7)
        self.assertEqual(truncate_number(5.2), 0.2)

    def test_negative_numbers(self):
        self.assertEqual(truncate_number(-3.5), -0.5)
        self.assertEqual(truncate_number(-4.7), -0.7)
        self.assertEqual(truncate_number(-5.2), -0.2)

    def test_zero(self):
        self.assertEqual(truncate_number(0), 0.0)

    def test_negative_zeros(self):
        self.assertEqual(truncate_number(-0.5), -0.5)
        self.assertEqual(truncate_number(-0.7), -0.7)
        self.assertEqual(truncate_number(-0.2), -0.2)

    def test_decimals_greater_than_one(self):
        with self.assertRaises(ValueError):
            truncate_number(1.5)
        with self.assertRaises(ValueError):
            truncate_number(2.7)
        with self.assertRaises(ValueError):
            truncate_number(3.2)