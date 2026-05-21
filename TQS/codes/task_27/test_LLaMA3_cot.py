from remove_multiple_spaces import *
import unittest
import re

def remove_multiple_spaces(text1):
    return (re.sub(' +',' ',text1))

class TestRemoveMultipleSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_multiple_spaces(''), '')

    def test_single_space(self):
        self.assertEqual(remove_multiple_spaces(' '), ' ')

    def test_valid_input(self):
        self.assertEqual(remove_multiple_spaces('  hello world  '), 'hello world')

    def test_multiple_spaces_separated_by_other_chars(self):
        self.assertEqual(remove_multiple_spaces('  hello,  world!  '), 'hello, world!')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_multiple_spaces(123)

if __name__ == '__main__':
    unittest.main()