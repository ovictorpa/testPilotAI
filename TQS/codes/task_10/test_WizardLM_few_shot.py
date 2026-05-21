import unittest
from typing import List, Tuple
from sum_product import sum_product  # Assuming the function is in a file named sum_product.py

class TestSumProduct(unittest.TestCase):
    def test_empty_list(self):
        """Test that an empty list returns (0, 1)"""
        self.assertEqual(sum_product([]), (0, 1))

    def test_positive_numbers(self):
        """Test that a list of positive numbers returns the correct sum and product"""
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_mixed_numbers(self):
        """Test that a list with mixed numbers returns the correct sum and product"""
        self.assertEqual(sum_product([-1, 3, 5, -2]), (-9, 60))

    def test_all_zeroes(self):
        """Test that a list of all zeroes returns (0, 0)"""
        self.assertEqual(sum_product([0, 0, 0]), (0, 0))  # Note: The product should be 0 in this case as well

    def test_all_negatives(self):
        """Test that a list of all negative numbers returns the correct sum and negative product"""
        self.assertEqual(sum_product([-1, -2, -3]), (-6, 6))

    def test_large_numbers(self):
        """Test with large numbers to ensure no overflow or incorrect results"""
        self.assertEqual(sum_product([10**8, 10**9]), (10**9, 10**17))  # This might need handling of potential overflow if int is 32-bit

    def test_negative_and_positive(self):
        """Test a list with both negative and positive numbers"""
        self.assertEqual(sum_product([-5, -4, 1, 2]), (-9, 8))

    def test_with_floats(self):
        """Test that the function only accepts integers and ignores floats"""
        with self.assertRaises(TypeError):
            sum_product([1.0, 2, 3])

    def test_with_non_integers(self):
        """Test that the function only accepts integers and does not mix them with non-integers"""
        with self.assertRaises(TypeError):
            sum_product([1, '2', 3])

    def test_large_negative_numbers(self):
        """Test with large negative numbers to ensure no overflow or incorrect results"""
        self.assertEqual(sum_product([-5000, -6000]), (-11000, 302400000000000000000))  # This might also need handling of potential overflow

if __name__ == '__main__':
    unittest.main()