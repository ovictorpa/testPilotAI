import unittest
import re
from remove_multiple_spaces import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):

    def test_single_space(self):
        self.assertEqual(remove_multiple_spaces('Hello '), 'Hello')

    def test_multiple_spaces(self):
        self.assertEqual(remove_multiple_spaces('   Hello   '), 'Hello')

    def test_no_spaces(self):
        self.assertEqual(remove_multiple_spaces('Hello'), 'Hello')

    def test_empty_string(self):
        self.assertEqual(remove_multiple_spaces(''), '')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_multiple_spaces(123)

    def test_string_with_special_characters(self):
        self.assertEqual(remove_multiple_spaces('Hello, '), 'Hello, ')

if __name__ == '__main__':
    unittest.main()