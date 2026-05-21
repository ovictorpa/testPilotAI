import unittest

from sum_product import sum_product


class TestSumProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element_list(self):
        self.assertEqual(sum_product([1]), (1, 1))

    def test_multiple_element_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

if __name__ == '__main__':
    unittest.main()