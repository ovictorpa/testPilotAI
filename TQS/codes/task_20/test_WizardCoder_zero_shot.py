import unittest
from freq_element import freq_element
from collections import Counter
from itertools import chain

class TestFreqElement(unittest.TestCase):
    
    def test_freq_element_empty_input(self):
        self.assertEqual(freq_element([]), {})
    
    def test_freq_element_single_input(self):
        nums = [1,2]
        self.assertDictEqual(freq_element([nums]), Counter({1: 1, 2: 1})
    
    def test_freq_element_multiple_input(self):
        nums = [[1,2],[3,4],[5]]
        self.assertDictEqual(freq_element(nums), Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
    
    def test_freq_element_with_repeated_elements(self):
        nums = [[1,2],[3,4,2],[5]]
        self.assertDictEqual(freq_element(nums), Counter({1: 1, 2: 2, 3: 1, 4: 1, 5: 1})
    
if __name__ == '__main__':
    unittest.main()