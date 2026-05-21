import unittest
from all_prefixes import all_prefixes  # replace 'your_module' with the actual name of the module where the function is defined

class TestAllPrefixes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), [''])

    def test_single_character(self):
        self.assertEqual(all_prefixes('a'), ['a'])

    def test_multiple_characters(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

    def test_longer_string(self):
        self.assertEqual(len(all_prefixes('abcdefghijklmnopqrstuvwxyz')), 27)

    def test_no_duplicated_prefixes(self):
        self.assertEqual(set(all_prefixes('abcdef')), set(['a', 'ab', 'abc', 'abcd', 'abcde']))

if __name__ == '__main__':
    unittest.main()