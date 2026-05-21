from truncate_number import *
import unittest

class TestTruncateNumber(unittest.TestCase):

    def test_truncates_zero(self):
        self.assertEqual(truncate_number(0.0), 0.0)

    def test_truncates_small_decimal(self):
        self.assertEqual(truncate_number(0.1), 0.0)

    def test_truncates_large_decimal(self):
        self.assertEqual(truncate_number(3.5), 0.5)

    def test_truncates_negative_number(self):
        with self.assertRaises(ValueError):
            truncate_number(-1.0)

    def test_truncates_non_float(self):
        with self.assertRaises(ValueError):
            truncate_number(1)


if __name__ == '__main__':
    unittest.main()