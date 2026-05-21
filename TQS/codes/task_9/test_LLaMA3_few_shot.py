import unittest
from truncate_number import truncate_number  # replace 'your_module' with the actual name of the module where the function is defined

class TestTruncateNumber(unittest.TestCase):

    def test_truncate_positive(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5, places=1)

    def test_truncate_negative(self):
        with self.assertRaises(ValueError):
            truncate_number(-3.5)

    def test_truncate_zero(self):
        self.assertEqual(truncate_number(0.0), 0.0)

    def test_truncate_large_decimal_part(self):
        self.assertAlmostEqual(truncate_number(12345.6789), 0.6789, places=4)

    def test_truncate_small_decimal_part(self):
        self.assertAlmostEqual(truncate_number(1.0), 0.0, places=1)

if __name__ == '__main__':
    unittest.main()