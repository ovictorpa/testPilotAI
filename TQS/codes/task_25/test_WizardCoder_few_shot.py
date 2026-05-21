from binomial_Coeff import *
import unittest
class TestSumOfProduct(unittest.TestCase):
    def test_binomial_coeff(self):
        #test case 1
        self.assertEqual(binomial_Coeff(2,1),3)
        
        #test case 2
        self.assertEqual(binomial_Coeff(3,2),6)
    
        #test case 3
        with self.assertRaises(IndexError):
            binomial_Coeff(1,-2)
    
        #test case 4
        self.assertEqual(binomial_Coeff(-5,6),0)
        
class TestSumOfProduct(unittest.TestCase):
    def test_sum_of_product(self):
        #test case 1
        self.assertEqual(sum_Of_product(2),3)
        
        #test case 2
        self.assertEqual(sum_Of_product(5),60)
        
        #test case 3
        with self.assertRaises(TypeError):
            sum_Of_product("a")
            
if __name__ == '__main__':
    unittest.main()