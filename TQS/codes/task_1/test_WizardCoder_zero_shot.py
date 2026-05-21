import unittest
from intersperse import intersperse

class TestInterspersing(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])
    
    def test_simple_case(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])
    
    def test_single_element_list(self):
        self.assertEqual(intersperse([5], 10), [5])
    
    def test_multiple_delimiters(self):
        self.assertEqual(intersperse([1, 2, 3, 4, 5], 6), [1, 6, 2, 6, 3, 6, 4, 6, 5])
    
    def test_negative_numbers(self):
        self.assertEqual(intersperse([-3, -2, -1], -4), [-3, -4, -2, -4, -1])
    
    def test_zero(self):
        self.assertEqual(intersperse([0, 1, 2], 0), [0, 0, 1, 0, 2])
    
    def test_float_numbers(self):
        self.assertRaises(TypeError, intersperse, [3.5, 4.6, 7.8], 9)
        
if __name__ == '__main__':
    unittest.main()