from binomial_Coeff import *
import unittest

class TestBinomialCoeff(unittest.TestCase):

    def test_binomical_coeff(self):
        self.assertEqual(binomial_Coeff(3, 2), 3)
        self.assertEqual(binomial_Coeff(4, 3), 6)

class TestSumOfProduct(unittest.TestCase):

    def test_sum_of_product(self):
        self.assertEqual(sum_Of_product(2), 6)
        self.assertEqual(sum_Of_product(3), 20)


if __name__ == '__main__':
    unittest.main()