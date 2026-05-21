import unittest
from all_prefixes import all_prefixes  # replace 'your_module' with the actual name of the module where the function is defined

class TestAllPrefixes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), [''])

    def test_single_char(self):
        self.assertEqual(all_prefixes('a'), ['a'])

    def test_multiple_chars(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

    def test_longer_string(self):
        self.assertEqual(all_prefixes('abcdefg'), ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg'])

    def test_repeated_chars(self):
        self.assertEqual(all_prefixes('aaaa'), ['a', 'aa', 'aaa', 'aaaa'])

    def test_string_with_spaces(self):
        self.assertEqual(all_prefixes('hello world'), [' ', 'hel', 'hell', 'hello', 'hello w', 'hello wo', 'hello worl', 'hello word', 'hello world'])

if __name__ == '__main__':
    unittest.main()