from binomial_Coeff import *
import unittest

class TestBinomialCoeff(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(binomial_Coeff(3,2), 3)

    def test_n_k_negative(self):
        with self.assertRaises(ValueError):
            binomial_Coeff(-1,2)

    def test_n_k_outside_range(self):
        with self.assertRaises(ValueError):
            binomial_Coeff(1000,500)

    def test_n_less_than_k(self):
        self.assertEqual(binomial_Coeff(2,1), 2)

    def test_n_even_k_even(self):
        self.assertEqual(binomial_Coeff(4,2), 6)

    def test_n_odd_k_odd(self):
        self.assertEqual(binomial_Coeff(5,3), 10)

class TestSumOfProduct(unittest.TestCase):

    def test_sum_of_product(self):
        self.assertEqual(sum_Of_product(2), 6)

if __name__ == '__main__':
    unittest.main()