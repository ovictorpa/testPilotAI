import unittest
from greatest_common_divisor import greatest_common_divisor as gcd  # Assuming the function is in a file named greatest_common_divisor.py

class TestGCD(unittest.TestCase):
    def test_gcd_of_two_large_numbers(self):
        self.assertEqual(gcd(123456789, 987654321), 1089)

    def test_gCD_with_zero_and_non_zero(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)

    def test_gCD_of_coprime_numbers(self):
        self.assertEqual(gcd(8, 17), 1)

    def test_gCD_with_negative_numbers(self):
        self.assertEqual(gcd(-24, 18), 6)
        self.assertEqual(gcd(-5, -8), 5)

    def test_gCD_of_two_large_coprime_numbers(self):
        self.assertEqual(gcd(987654321, 123456789), 1)

    def test_gCD_with_equal_numbers(self):
        self.assertEqual(gcd(3, 3), 3)

    def test_gCD_with_one_and_non_zero(self):
        self.assertEqual(gcd(1, 5), 1)

    def test_gCD_with_both_zero(self):
        # This case is often omitted as it's a matter of convention, but we can define it to be 0.
        self.assertEqual(gcd(0, 0), 0)

    def test_gCD_of_two_integers_inverse_relationship(self):
        self.assertEqual(gcd(48, 150), 6)

    def test_gCD_with_large_fibonacci_numbers(self):
        self.assertEqual(gcd(55, 89), 1)

    def test_gCD_of_large_prime_numbers(self):
        self.assertEqual(gcd(2330019, 2330039), 4675)

    def test_gCD_with_perfect_squares(self):
        self.assertEqual(gcd(16, 25), 1)

    def test_gCD_of_integers_spanning_a_large_range(self):
        self.assertEqual(gcd(-32768, 65535), 1484)

if __name__ == '__main__':
    unittest.main()