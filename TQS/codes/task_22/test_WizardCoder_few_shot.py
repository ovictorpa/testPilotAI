from freq_count import *
import unittest
from collections import Counter

class TestFreqCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(freq_count([]), {})
    
    def test_non_empty_list(self):
        self.assertEqual(freq_count([1,2,3]), Counter({1: 1, 2: 1, 3: 1}))
        
    def test_duplicates_in_list(self):
        self.assertEqual(freq_count([1,2,3,2,4,5,3]), Counter({1: 1, 2: 2, 3: 2, 4: 1, 5: 1}))
    
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            freq_count("not a list")
        with self.assertRaises(AttributeError):
            freq_count({"not a list"})
    
    def test_empty_dict(self):
        self.assertEqual(freq_count([1,2]), {})
        
if __name__ == '__main__':
    unittest.main()