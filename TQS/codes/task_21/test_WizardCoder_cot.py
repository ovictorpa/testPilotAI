from sequence import *
import unittest

class TestSequence(unittest.TestCase):
    
    def test_negative_input(self):
        self.assertRaises(ValueError, sequence, -1)
        
    def test_zero_input(self):
        self.assertEqual(sequence(0), 0)
        
    def test_base_case(self):
        self.assertEqual(sequence(1), 1) # base case when n=1 should return 1
        self.assertEqual(sequence(2), 1) # base case when n=2 should also return 1
        
    def test_recursive_case(self):
        self.assertTrue(isinstance(sequence(3), int)) # recursive call should always return an integer
        
if __name__ == '__main__':
    unittest.main()