import unittest
from truncate_number import truncate_number

class TestTruncateNumber(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertEqual(truncate_number(3.5), 0.5)
        self.assertEqual(truncate_number(4.2), 0.2)
        self.assertAlmostEqual(truncate_number(123.456789), 0.456789)
    
    def test_negative_numbers(self):
        self.assertEqual(truncate_number(-3.5), 0.5)
        self.assertAlmostEqual(truncate_number(-2.1), 0.1)
    
    def test_zero(self):
        self.assertEqual(truncate_number(0), 0)
        
    def test_decimal_numbers(self):
        self.assertAlmostEqual(truncate_number(3.25), 0.25)
        self.assertAlmostEqual(truncate_number(-2.75), 0.75)
    
    def test_edge_cases(self):
        self.assertEqual(truncate_number(1.), 0)
        self.assertEqual(truncate_number(float('inf')), float('nan'))
        self.assertTrue(isinstance(truncate_number(5), float)) # check if the function returns a float value