import unittest
from typing import List, Tuple
from sum_product import sum_product  # Replace 'your_module' with the actual module name where the function is defined

class TestSumProduct(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_non_empty_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, 3, 4]), (-6, -24))

    def test_positive_numbers(self):
        self.assertEqual(sum_product([5, 6, 7, 8]), (30, 336))

    def test_mixed_numbers(self):
        self.assertEqual(sum_product([-1, 3, 5, -7]), (-4, 75))

    def test_large_numbers(self):
        # Test with large numbers to ensure the product doesn't overflow
        large_list = [10**6, 10**6]
        self.assertEqual(sum_product(large_list), (2 * 10**12, 10**12))

    def test_floats_in_list(self):
        # This should raise a TypeError if the function is not handled for floats
        with self.assertRaises(TypeError):
            sum_product([1.5, 2.5])

    def test_non_integer_types(self):
        # Test with non-integer types to ensure they are not accepted
        with self.assertRaises(TypeError):
            sum_product(['1', '2', '3'])

    def test_large_sum_and_product(self):
        large_list = [i for i in range(10**6)]
        self.assertEqual(sum_product(large_list), (5 * 10**6, 10**12))

if __name__ == '__main__':
    unittest.main()