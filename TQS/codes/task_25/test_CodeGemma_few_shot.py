from binomial_Coeff import *
import unittest

class TestBinomialCoeff(unittest.TestCase):

    def test_binom_coeff_basic(self):
        self.assertEqual(binomial_Coeff(5,3), 10)

    def test_binom_coeff_edge_cases(self):
        self.assertEqual(binomial_Coeff(0,0), 1)
        self.assertEqual(binomial_Coeff(10,10), 1)

    def test_binom_coeff_invalid_inputs(self):
        with self.assertRaises(ValueError):
            binomial_Coeff(-5,3)

class TestSumOfProduct(unittest.TestCase):

    def test_sum_of_product_basic(self):
        self.assertEqual(sum_Of_product(5), 455)

    def test_sum_of_product_edge_cases(self):
        self.assertEqual(sum_Of_product(0), 1)
        self.assertEqual(sum_Of_product(1), 2)

    def test_sum_of_product_invalid_inputs(self):
        with self.assertRaises(ValueError):
            sum_Of_product(-5)

if __name__ == '__main__':
    unittest.main()