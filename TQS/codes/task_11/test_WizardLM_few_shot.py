import unittest

from all_prefixes import all_prefixes  # Replace 'your_module' with the name of the module where the function is defined

class TestAllPrefixes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), [''])

    def test_single_character_string(self):
        self.assertListEqual(all_prefixes('a'), ['a'])
        self.assertListEqual(all_prefixes('b'), ['b'])
        self.assertListEqual(all_prefixes('c'), ['c'])

    def test_multiple_character_string(self):
        self.assertListEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])
        self.assertListEqual(all_prefixes('abcd'), ['a', 'ab', 'abc', 'abcd'])
        self.assertListEqual(all_prefixes('hello'), ['h', 'he', 'hel', 'hello'])

    def test_string_with_repeated_characters(self):
        self.assertListEqual(all_prefixes('aaa'), ['a', 'aa', 'aaa'])
        self.assertListEqual(all_prefixes('bbbb'), ['b', 'bb', 'bbb', 'bbbb'])

    def test_case_sensitivity(self):
        self.assertListEqual(all_prefixes('Abc'), ['A', 'Ab', 'Abc', 'abc'])
        self.assertListEqual(all_prefixes('abc', case_sensitive=True), ['a', 'ab', 'abc'])  # If the function supports case sensitivity as an argument

    def test_string_with_whitespace(self):
        self.assertListEqual(all_prefixes('hi there'), ['h', 'hi', 'hi t', 'hi there', 'there'])

    def test_non_alphabetic_string(self):
        self.assertListEqual(all_prefixes('123'), ['1', '12', '123'])
        self.assertListEqual(all_prefixes('abc123'), ['a', 'ab', 'abc1', 'abc12', 'abc123'])

    def test_string_with_special_characters(self):
        self.assertListEqual(all_prefixes('hi!'), ['h', 'hi', 'hi!', 'h!', 'i!'])

    def test_very_long_string(self):
        very_long_string = 'a' * 1000  # Assuming the function can handle strings of this size
        self.assertListEqual(all_prefixes(very_long_string), list(range(1, len(very_long_string) + 1)))

if __name__ == '__main__':
    unittest.main()