from TQS.tests_final.task_9.truncate_number import *
import unittest

class TestTruncateNumber(unittest.TestCase):
    
    def test_positive_integer(self):
        self.assertEqual(truncate_number(4), 0)
        
    def test_decimal(self):
        self.assertLess(truncate_number(3.5), 1)