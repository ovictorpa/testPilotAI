import unittest
from truncate_number import truncate_number # importing the function to test 

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5) # checking if decimal part of 3.5 is equal to 0.5 
        self.assertAlmostEqual(truncate_number(-2.1415926535897932384), -0.1415926535897932384)
        self.assertAlmostEqual(truncate_number(2.0), 0.0) # checking if decimal part of a positive integer is 0
        
if __name__ == '__main__':
    unittest.main()