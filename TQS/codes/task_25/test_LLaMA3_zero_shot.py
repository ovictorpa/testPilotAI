from binomial_Coeff import *
import unittest

class TestBinomialCoefficients(unittest.TestCase):

    def test_binomial_coefficient_0(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)

    def test_binomial_coefficient_1(self):
        self.assertEqual(binomial_Coeff(1, 1), 1)
        self.assertEqual(binomial_Coeff(2, 0), 1)
        self.assertEqual(binomial_Coeff(3, 2), 3)

    def test_binomial_coefficient_large_values(self):
        self.assertGreaterEqual(binomial_Coeff(100, 50), 0)
        self.assertLessEqual(binomial_Coeff(100, 50), 10**30) # max value for int in python

    def test_sum_of_product_1(self):
        self.assertEqual(sum_Of_product(1), binomial_Coeff(2*1, 1-1))

    def test_sum_of_product_2(self):
        self.assertEqual(sum_Of_product(2), binomial_Coeff(2*2, 2-1))

    def test_sum_of_product_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_Of_product("a")

    def test_binomial_coefficient_invalid_input(self):
        with self.assertRaises(TypeError):
            binomial_Coeff(-1,5)
        
if __name__ == '__main__':
    unittest.main()