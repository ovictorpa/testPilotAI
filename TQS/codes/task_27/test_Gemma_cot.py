from remove_multiple_spaces import *
import unittest

class TestRemoveMultipleSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_multiple_spaces(''), '')

    def test_single_space(self):
        self.assertEqual(remove_multiple_spaces(' '), ' ')

    def test_multiple_spaces_in_row(self):
        self.assertEqual(remove_multiple_spaces('   hello   '), 'hello')

    def test_spaces_at_beginning_or_end(self):
        self.assertEqual(remove_multiple_spaces(' hello   '), 'hello')
        self.assertEqual(remove_multiple_spaces('   hello'), 'hello')

    def test_basic_text_with_multiple_spaces(self):
        text = 'This   sentence   has    multiple spaces.'
        self.assertEqual(remove_multiple_spaces(text), 'This sentence has multiple spaces.')

    def test_text_with_leading_and_trailing_spaces(self):
        text = '  This sentence has multiple spaces.  '
        self.assertEqual(remove_multiple_spaces(text), 'This sentence has multiple spaces.')


if __name__ == '__main__':
    unittest.main()