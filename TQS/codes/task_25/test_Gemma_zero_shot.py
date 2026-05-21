from binomial_Coeff import *
import unittest

class TestBinomialCoeff(unittest.TestCase):

    def test_binom_coeff_basic(self):
        self.assertEqual(binom_coeff(3, 2), 3)

    def test_binom_coeff_edge_cases(self):
        self.assertEqual(binom_coeff(0, 0), 1)
        self.assertEqual(binom_coeff(1, 0), 1)
        self.assertEqual(binom_coeff(2, 2), 1)

class TestSumOfProduct(unittest.TestCase):

    def test_sum_of_product_basic(self):
        self.assertEqual(sum_of_product(2), 6)

    def test_sum_of_product_large(self):
        self.assertEqual(sum_of_product(10), 3024)


if __name__ == '__main__':
    unittest.main()