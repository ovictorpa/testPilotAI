from mean_absolute_deviation import *
import unittest
from typing import List, Tuple

class TestMeanAbsoluteDeviation(unittest.TestCase):
    
    def test_add(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0]), 1.0)
        self.assertAlmostEqual(mean_absolute_deviation([5.0, -2.0, 8.0, 4.0]), 1.666667)
        self.assertAlmostEqual(mean_absolute_deviation([-3.0, 1.0, -1.0, 1.5, 1.5]), 1.0)
        
if __name__ == '__main__':
    unittest.main()