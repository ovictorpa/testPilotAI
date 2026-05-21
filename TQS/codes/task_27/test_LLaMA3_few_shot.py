import unittest
from remove_multiple_spaces import remove_multiple_spaces  # Replace 'your_module' with the actual name of your module

class TestRemoveMultipleSpaces(unittest.TestCase):

    def test_remove_multiple_spaces(self):
        self.assertEqual(remove_multiple_spaces("Hello   World"), "Hello World")

    def test_remove_leading_trailing_spaces(self):
        self.assertEqual(remove_multiple_spaces("   Hello   World  "), "Hello World")

    def test_empty_string(self):
        self.assertEqual(remove_multiple_spaces(""), "")

    def test_single_space(self):
        self.assertEqual(remove_multiple_spaces(" "), " ")

    def test_no_multiple_spaces(self):
        self.assertEqual(remove_multiple_spaces("HelloWorld"), "HelloWorld")

if __name__ == '__main__':
    unittest.main()