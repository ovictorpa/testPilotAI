from freq_count import *
import unittest
from collections import Counter

class TestFreqCount(unittest.TestCase):
    def test_freq_count(self):
        # Empty list
        self.assertEqual(Counter(), freq_count([]))

        # Single item list
        self.assertEqual(Counter({'a': 1}), freq_count(['a']))

        # Multiple items list
        self.assertEqual(Counter({'a': 2, 'b': 2}), freq_count(['a', 'b', 'a', 'b']))

        # Nested lists
        self.assertEqual(Counter({'a': 2, 'b': 2, 'c': 1}), freq_count([['a', 'b'], ['a', 'b'], ['c']]))

if __name__ == '__main__':
    unittest.main()