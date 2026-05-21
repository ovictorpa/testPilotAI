from filter_by_prefix import *
import unittest
from typing import List

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        input = []
        expected_output = []
        self.assertListEqual(filter_by_prefix(input, 'a'), expected_output)

    def test_non_empty_list(self):
        input = ['abc', 'bcd', 'cde']
        expected_output = ['abc', 'bcd']
        self.assertListEqual(filter_by_prefix(input, 'a'), expected_output)

if __name__ == '__main__':
    unittest.main()