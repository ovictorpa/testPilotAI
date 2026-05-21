from truncate_number import *
import unittest

class TestTruncateNumber(unittest.TestCase):

    def test_truncate_number_positive(self):
        self.assertEqual(truncate_number(3.5), 0.5)

    def test_truncate_number_negative(self):
        self.assertEqual(truncate_number(-3.5), -0.5)

    def test_truncate_number_zero(self):
        self.assertEqual(truncate_number(0.0), 0.0)

    def test_truncate_number_large_number(self):
        self.assertEqual(truncate_number(123456789.5), 0.5)

    def test_truncate_number_small_number(self):
        self.assertEqual(truncate_number(0.0000000000000000000000000000000