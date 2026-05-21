from sum_product import *
import unittest


def sum_product(numbers: List[int]) -> Tuple[int, int]:

    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n

    return sum_value, prod_value


class TestSumProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element(self):
        self.assertEqual(sum_product([1]), (1, 1))

    def test_multiple_elements(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_negative_elements(self):
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-10, 24))

    def test_large_elements(self):
        self.assertEqual(sum_product([1000, 2000, 3000, 4000]), (10000, 240000000))


if __name__ == '__main__':
    unittest.main()