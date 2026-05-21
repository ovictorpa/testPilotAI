from truncate_number import *
import unittest

class TestTruncateNumber(unittest.TestCase):

    def test_truncates_decimal_part(self):
        self.assertEqual(truncate_number(3.5), 0.5)

    def test_truncates_numbers_with_trailing_zeros(self):
        self.assertEqual(truncate_number(1.0), 0.0)

    def test_truncates_numbers_greater_than_one(self):
        self.assertEqual(truncate_number(2.5), 0.5)

    def test_handles_negative_numbers(self):
        with self.assertRaises(ValueError):
            truncate_number(-1.0)

    def test_handles_non_floats(self):
        with self.assertRaises(TypeError):
            truncate_number('1.0')


if __name__ == '__main__':
    unittest.main()