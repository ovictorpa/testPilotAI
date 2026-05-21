from binomial_Coeff import *
import unittest

class TestBinomialCoefficientAndSumOfProduct(unittest.TestCase):
    def test_binomial_coefficient_edge_cases(self):
        self.assertEqual(binomial_Coeff(0, 0), 1) # nC0 is always 1 for any value of n and k
        self.assertEqual(binomial_Coeff(-1, -1), None) # Invalid input values should return None
    
    def test_sum_of_product(self):
        self.assertEqual(sum_Of_product(0), 1)
        self.assertEqual(sum_Of_product(1), 1)
        self.assertEqual(sum_Of_product(2), 3) # C(4, 3) = C(2 * 2, 2-1) + C(2 * 2, 1-1) = 5
        self.assertEqual(sum_Of_product(3), 6)
        self.assertEqual(sum_Of_product(-1), None) # Invalid input values should return None
    
if __name__ == '__main__':
    unittest.main()