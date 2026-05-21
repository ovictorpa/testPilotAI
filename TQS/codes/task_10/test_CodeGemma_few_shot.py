import unittest

from sum_product import sum_product

class TestSumProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element_list(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_multiple_element_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, -3]), (-6, -6))

    def test_mixed_numbers(self):
        self.assertEqual(sum_product([1, 2, -3, 4]), (4, 4))

if __name__ == '__main__':
    unittest.main()