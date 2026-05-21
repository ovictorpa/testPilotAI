from freq_element import *
import unittest
from collections import Counter, namedtuple
from itertools import chain

class TestFreqElement(unittest.TestCase):
  
  def test_freq_element(self):
    # empty list scenario
    self.assertEqual({}, freq_element([]))
    
    # single element list scenario
    self.assertEqual({1: 1}, freq_element([1]))
    
    # two elements with same frequency scenario
    self.assertEqual({2: 2, 3: 2}, freq_element([2, 2, 3, 3]))
    
    # multiple elements with different frequencies scenario
    self.assertEqual({1: 2, 2: 1}, freq_element([1, 2, 3, 2]))
    
    # empty iterable scenario
    try:
      freq_element(None)
    except TypeError as e:
      self.assertEqual('NoneType is not iterable', str(e))
    
    # list of lists scenario
    self.assertEqual({1: 2, 2: 3}, freq_element([[1, 2], [1, 2], [1]]))
    
    # list with float scenario
    try:
      freq_element([1.5])
    except TypeError as e:
      self.assertEqual('float is not iterable', str(e))
      
    # list of strings scenario
    self.assertEqual({'a': 1, 'b': 2}, freq_element(['a', 'b', 'b']))
    
    # nested lists scenario
    try:
      freq_element([[1, [2, 3]])
    except TypeError as e:
      self.assertEqual('list is not iterable', str(e))