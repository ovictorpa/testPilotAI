from freq_count import *
import unittest
import collections

def freq_count(list1):

  freq_count= collections.Counter(list1)

  return freq_count

class TestFreqCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(freq_count([]), {})

    def test_single_element_list(self):
        self.assertEqual(freq_count([1]), {1: 1})

    def test_multiple_elements_list(self):
        self.assertEqual(freq_count([1, 2, 2, 3]), {1: 1, 2: 2, 3: 1})

    def test_non_integer_elements(self):
        self.assertEqual(freq_count(['a', 'b', 'c', 'a']), {'a': 2, 'b': 1, 'c': 1})

if __name__ == '__main__':
    unittest.main()