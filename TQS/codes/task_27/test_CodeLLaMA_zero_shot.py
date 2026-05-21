from remove_multiple_spaces import *
import unittest
import re

class TestRemoveMultipleSpaces(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(re.sub(' +', ' ', ''), '')

    def test_single_space(self):
        self.assertEqual(re.sub(' +', ' ', ' '), ' ')

    def test_multiple_spaces(self):
        self.assertEqual(re.sub(' +', ' ', '  '), ' ')

    def test_mixed_string(self):
        self.assertEqual(re.sub(' +', ' ', 'hello  world'), 'hello world')