from truncate_number import *
class TestTruncateNumber(unittest.TestCase):

    def test_truncate_positive_number(self):
        self.assertEqual(truncate_number(3.5), 0.5)

    def test_truncate_negative_number(self):
        self.assertEqual(truncate_number(-3.5), -0.5)

    def test_truncate_whole_number(self):
        self.assertEqual(truncate_number(5.0), 0.0)

    def test_truncate_decimal_number(self):
        self.assertEqual(truncate_number(3.75), 0.75)

    def test_truncate_large_number(self):
        self.assertEqual(truncate_number(1000000.99), 0.99)