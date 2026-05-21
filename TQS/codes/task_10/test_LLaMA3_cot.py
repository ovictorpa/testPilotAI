import unittest
from sum_product import sum_product

class TestSumProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element_list(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_multiple_elements_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, -3]), (-6, -6))
        self.assertEqual(sum_product([1, -2, 3]), (0, 1))

    def test_zero_in_list(self):
        self.assertEqual(sum_product([0, 1, 2]), (3, 0))
        self.assertEqual(sum_product([1, 0, 2]), (3, 0))

    def test_mixed_signs(self):
        self.assertEqual(sum_product([-1, 2, -3, 4]), (-6, 1))
        self.assertEqual(sum_product([1, -2, 3, -4]), (0, 1))

if __name__ == '__main__':
    unittest.main()