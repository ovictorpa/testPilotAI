import unittest
from truncate_number import truncate_number

class TestTruncateNumber(unittest.TestCase):
    
    def test_positive_integer(self):
        """Test that truncating a positive integer returns 0.0"""
        self.assertEqual(truncate_number(5), 0.0)
        
    def test_positive_fraction(self):
        """Test that truncating a positive fraction returns the fractional part"""
        self.assertAlmostEqual(truncate_number(3.5), 0.5, places=1)
        
    def test_zero(self):
        """Test that truncating zero returns 0.0"""
        self.assertEqual(truncate_number(0), 0.0)

    def test_negative_number(self):
        """Test that the function raises an AssertionError for negative numbers"""
        with self.assertRaises(AssertionError):
            truncate_number(-1)
        
    def test_non_numeric_input(self):
        """Test that the function raises a TypeError for non-numeric inputs"""
        with self.assertRaises(TypeError):
            truncate_number("one")
        
if __name__ == '__main__':
    unittest.main()