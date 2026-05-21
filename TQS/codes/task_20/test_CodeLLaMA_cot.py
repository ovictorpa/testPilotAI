from freq_element import *
import unittest
from collections import Counter
from itertools import chain

class TestFreqElement(unittest.TestCase):
    def test_empty_input(self):
        nums = []
        result = freq_element(nums)
        self.assertEqual(result, {})
    
    def test_single_element_input(self):
        nums = [1]
        result = freq_element(nums)
        self.assertEqual(result, Counter({1: 1}))
    
    def test_multiple_elements_input(self):
        nums = [1, 2, 3, 2, 1]
        result = freq_element(nums)
        self.assertEqual(result, Counter({1: 2, 2: 2, 3: 1}))
    
    def test_negative_numbers_input(self):
        nums = [-1, -2, -3, -2, -1]
        result = freq_element(nums)
        self.assertEqual(result, Counter({-1: 2, -2: 2, -3: 1}))
    
    def test_positive_and_negative_numbers_input(self):
        nums = [1, 2, -3, -2, 1]
        result = freq_element(nums)
        self.assertEqual(result, Counter({1: 2, 2: 2, -3: 1}))