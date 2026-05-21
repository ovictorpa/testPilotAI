from truncate_number import *
import unittest

class TestTruncateNumber(unittest.TestCase):

    def test_positive_number_with_decimal_part(self):
        number = 3.5
        expected_result = 0.5
        actual_result = truncate_number(number)
        self.assertEqual(actual_result, expected_result)

    def test_positive_number_without_decimal_part(self):
        number = 3.0
        expected_result = 0.0
        actual_result = truncate_number(number)
        self.assertEqual(actual_result, expected_result)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            truncate_number(-3.5)

    def test_zero(self):
        self.assertEqual(truncate_number(0.0), 0.0)

    def test_not_a_float(self):
        with self.assertRaises(TypeError):
            truncate_number(3)


if __name__ == '__main__':
    unittest.main()