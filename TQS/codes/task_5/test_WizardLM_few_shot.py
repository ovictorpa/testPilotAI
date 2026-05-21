import unittest
from greatest_common_divisor import greatest_common_divisor  # Assuming the function is defined in greatest_common_divisor.py

class TestGreatestCommonDivisor(unittest.TestCase):
    def test_gcd_of_two_numbers(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)

    def test_gcd_with_larger_numbers(self):
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_gcd_when_one_of_the_numbers_is_negative(self):
        self.assertEqual(greatest_common_divisor(-8, 12), 4)

    def test_gcd_with_zero_as_divisor(self):
        self.assertEqual(greatest_common_divisor(0, 5), 5)
        self.assertEqual(greatest_common_divisor(5, 0), 5)
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_gcd_with_one_of_the_numbers_being_zero(self):
        self.assertEqual(greatest_common_divisor(1, 0), 1)

    def test_gcd_for_two_coprime_numbers(self):
        self.assertEqual(greatest_common_divisor(6, 9), 3)

    def test_gcd_of_large_numbers(self):
        self.assertEqual(greatest_common_divisor(123456789, 987654321), 35245807)

    def test_gcd_for_two_prime_numbers(self):
        self.assertEqual(greatest_common_divisor(17, 19), 1)
        self.assertEqual(greatest_common_divisor(23, 461), 1)

    def test_gcd_when_one_number_is_twice_the_other(self):
        self.assertEqual(greatest_common_divisor(4, 8), 4)
        self.assertEqual(greatest_common_divisor(16, 32), 16)

    def test_gcd_when_one_number_is_a_multiple_of_the_other(self):
        self.assertEqual(greatest_common_divisor(10, 50), 10)
        self.assertEqual(greatest_common_divisor(60, 120), 120)

    def test_gcd_when_one_number_is_three_times_the_other(self):
        self.assertEqual(greatest_common_divisor(12, 36), 12)

    # Additional edge case tests can be added here

if __name__ == '__main__':
    unittest.main()