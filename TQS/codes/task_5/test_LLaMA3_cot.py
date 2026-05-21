from greatest_common_divisor import *
import unittest

class TestGreatestCommonDivisor(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(10, 15), 5)

    def test_negative_integers(self):
        self.assertEqual(greatest_common_divisor(-3, 5), 1)
        self.assertEqual(greatest_common_divisor(-25, -15), 5)

    def test_zero_input(self):
        with self.assertRaises(ValueError):
            greatest_common_divisor(0, 10)
        self.assertEqual(greatest_common_divisor(10, 0), 10)

    def test_equal_numbers(self):
        self.assertEqual(greatest_common_divisor(12, 15), 3)
        self.assertEqual(greatest_common_divisor(20, 30), 10)

    def test_one_of_inputs_is_zero_or_one(self):
        self.assertEqual(greatest_common_divisor(0, 10), 10)
        self.assertEqual(greatest_common_divisor(1, 10), 1)
        with self.assertRaises(ValueError):
            greatest_common_divisor(0, 0)

    def test_large_numbers(self):
        import random
        for _ in range(100):
            num1 = random.randint(1, 10000)
            num2 = random.randint(1, 10000)
            self.assertEqual(greatest_common_divisor(num1, num2), greatest_common_divisor(random.randint(1, 10000), random.randint(1, 10000)))

    def test_euclidean_algorithm(self):
        self.assertEqual(greatest_common_divisor(48, 18), 6)

if __name__ == '__main__':
    unittest.main()