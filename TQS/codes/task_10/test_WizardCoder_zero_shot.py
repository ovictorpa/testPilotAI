from sum_product import *
from typing import List, Tuple
import unittest

class TestSumProduct(unittest.TestCase):
    
    def test_sum_product(self):
        self.assertEqual(sum_product([]), (0, 1))
        self.assertEqual(sum_product([1]), (1, 1))
        self.assertEqual(sum_product([1, 2, 3]), (6, 6))
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))
        self.assertEqual(sum_product([-1, -2, 3, 4]), (-2, -24))
        
unittest.main()