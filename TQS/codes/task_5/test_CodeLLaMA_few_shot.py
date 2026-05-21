import unittest
from greatest_common_divisor import greatest_common_divisor

class TestGreatestCommonDivisor(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)

    def test_example1(self):
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_zero(self):
        self.assertEqual(greatest_common_divisor(0, 10), 10)

    def test_one(self):
        self.assertEqual(greatest_common_divisor(1234, 5678), 2)

    def test_negative(self):
        self.assertEqual(greatest_common_divisor(-1234, -5678), 2)