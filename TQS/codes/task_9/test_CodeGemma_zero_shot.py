from truncate_number import *
import unittest

class TestTruncateNumber(unittest.TestCase):

    def test_positive_number(self):
        self.assertEqual(truncate_number(3.5), 0.5)

    def test_negative_number(self):
        self.assertEqual(truncate_number(-3.5), -0.5)

    def test_zero(self):
        self.assertEqual(truncate_number(0), 0)

    def test_integer(self):
        self.assertEqual(truncate_number(5), 0)

    def test_large_number(self):
        self.assertEqual(truncate_number(1234567.89), 0.89)

if __name__ == '__main__':
    unittest.main()