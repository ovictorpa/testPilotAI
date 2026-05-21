from binomial_Coeff import *
import unittest

class TestBinomialFunctions(unittest.TestCase):

    def test_binomial_coefficient(self):
        self.assertEqual(binomial_Coeff(5, 2), 10) # nC2 should be equal to 10

    def test_binomial_coefficient_zero_k(self):
        self.assertEqual(binomial_Coeff(5, 0), 1) # nC0 is always 1

    def test_binomial_coefficient_large_n(self):
        self.assertEqual(binomial_Coeff(20, 15), 15511210043330985984000000) 

    def test_binomial_coefficient_negative_k(self):
        with self.assertRaises(ValueError): 
            binomial_Coeff(-5, -2)

    def test_sum_of_product(self):
        self.assertEqual(sum_Of_product(3), binomial_Coeff(6, 2))

    def test_sum_of_product_zero_n(self):
        with self.assertRaises(ValueError):
            sum_Of_product(0)

    def test_binomial_coefficient_edge_case(self): # Test edge cases by making sure that the input values don't result in a division by zero or negative numbers
        with self.assertRaises(ValueError): 
            binomial_Coeff(-5, -2)
        
if __name__ == '__main__':
    unittest.main()