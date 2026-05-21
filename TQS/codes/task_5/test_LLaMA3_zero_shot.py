import unittest
from greatest_common_divisor import greatest_common_divisor  # Replace 'your_module' with the actual name of the module containing the function

class TestGCDFunction(unittest.TestCase):

    def test_gcd_of_positive_numbers(self):
        self.assertEqual(greatest_common_divisor(12, 18), 6)
        self.assertEqual(greatest_common_divisor(24, 30), 6)

    def test_gcd_of_zero_and_positive_number(self):
        with self.assertRaises(TypeError):
            greatest_common_divisor(0, 5)

    def test_gcd_of_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(-12, -18), 6)
        self.assertEqual(greatest_common_divisor(-24, -30), 6)

    def test_gcd_of_positive_and_zero(self):
        with self.assertRaises(TypeError):
            greatest_common_divisor(5, 0)

    def test_gcd_edge_case(self):
        self.assertEqual(greatest_common_divisor(1, 1), 1)
        self.assertEqual(greatest_common_divisor(2, 4), 2)

if __name__ == '__main__':
    unittest.main()