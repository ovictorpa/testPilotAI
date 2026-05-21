from TQS.tests_final.task_7.mean_absolute_deviation import *
from typing import List
import unittest

class TestMeanAbsoluteDeviation(unittest.TestCase):
    
    def test_mean_absolute_deviation(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)
        
if __name__ == '__main__':
    unittest.main()