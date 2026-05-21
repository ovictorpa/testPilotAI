from binomial_Coeff import *
import unittest
from math import factorial as f

def test_sum_of_product():
    class TestSumOfProduct(unittest.TestCase):
        
        def test_sum_of_product(self):
            self.assertEqual(sum_Of_product(0), 1)
            self.assertEqual(sum_Of_product(1), f(2))
            self.assertEqual(sum_Of_product(3), sum([f(i) for i in range(2, 4)])) # 1 + 2 + 6 = 9 (n=2)
            self.assertEqual(sum_of_product(5), f(7))
    
    unittest.main()