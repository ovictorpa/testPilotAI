from greatest_common_divisor import *
import unittest

def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

class TestGCD(unittest.TestCase):
    def test_co_prime_numbers(self):
        self.assertEqual(greatest_common_divisor(35, 23), 1)

    def test_coprime_pairs(self):
        self.assertEqual(greatest_common_divisor(24, 36), 8)

    def test_equal_numbers(self):
        self.assertEqual(greatest_common_divisor(7, 7), 7)

    def test_one_number_is_zero(self):
        self.assertEqual(greatest_common_divisor(0, 5), 5)
        self.assertEqual(greatest_common_divisor(-5, 0), 5)

    def test_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(-3, -5), 1)
        self.assertEqual(greatest_common_divisor(-3, 5), 1)

    def test_large_fibonacci_numbers(self):
        self.assertEqual(greatest_common_divisor(89, 144), 89)

    def test_input_as_tuple_or_list(self):
        self.assertEqual(greatest_common_divisor((27, 64),), 9)
        self.assertEqual(greatest_common_divisor([1024, 256],), 256)

    def test_invalid_input_types(self):
        with self.assertRaises(TypeError):
            greatest_common_divisor("not an int", 5)
        with self.assertRaises(TypeError):
            greatest_common_divisor(5, "not an int")
        with self.assertRaises(TypeError):
            greatest_common_divisor([5],)
        with self.assertRaises(TypeError):
            greatest_common_divisor((5,), 2)

    def test_large_inputs(self):
        large_gcd = greatest_common_divisor(2**30, 2**15)
        self.assertEqual(large_gcd, 2**15)

    def test_different_magnitude_numbers(self):
        self.assertEqual(greatest_common_divisor(2**18, 2**6), 2**6)

    def test_basic_examples(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)

if __name__ == '__main__':
    unittest.main()