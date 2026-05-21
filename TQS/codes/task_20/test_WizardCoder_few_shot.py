from freq_element import *
import unittest

class TestFreqElement(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(freq_element([]), {})
    
    def test_single_item_list(self):
        self.assertEqual(freq_element([1]), {1: 1})
    
    def test_multi_item_list_same(self):
        self.assertEqual(freq_element([2, 2, 2]), {2: 3}
    
    def test_multi_item_list_diff(self):
        self.assertEqual(freq_element([1, 2, 3, 4, 5, 6]), {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
    
    def test_multi_item_list_diff_freq(self):
        self.assertEqual(freq_element([1, 2, 3, 4, 5, 6, 7, 7]), {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 2}
    
    def test_string(self):
        self.assertEqual(freq_element("hello"), {'h': 1, 'e': 1, 'l': 3, 'o': 2})
        
if __name__ == '__main__':
    unittest.main()