from longest import *
import unittest

from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)

    for s in strings:
        if len(s) == maxlen:
            return s

class TestLongest(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_element_list(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_elements_list(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'c')
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')