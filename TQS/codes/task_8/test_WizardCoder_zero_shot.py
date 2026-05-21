from has_close_elements import *
from typing import List
import unittest 

class TestHasCloseElements(unittest.TestCase):
    
    def test_has_close_elements_false(self):
        self.assertEqual(False, has_close_elements([1.0, 2.0, 3.0], 0.5))
        
    def test_has_close_elements_true(self):
        self.assertEqual(True, has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))
        
    def test_has_close_elements_false2(self):
        self.assertEqual(False, has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.9) )
        
    def test_has_close_elements_true2(self):
        self.assertEqual(True, has_close_elements([1.0, 2.0, 3.0, 4.0, 6.0], 0.5))
        
    def test_has_close_elements_false3(self):
        self.assertEqual(False, has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 1) )
        
if __name__ == '__main__':
    unittest.main()