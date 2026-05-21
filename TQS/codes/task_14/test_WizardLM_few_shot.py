import unittest

from filter_by_prefix import filter_by_prefix  # Replace 'your_module' with the actual name of the module where filter_by_prefix is defined.

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix(['apple', 'banana'], 'a'), [])

    def test_no_prefix_match(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'x'), [])

    def test_all_strings_start_with_prefix(self):
        self.assertEqual(filter_by_prefix(['apple', 'apricot', 'avocado'], 'a'), ['apple', 'apricot', 'avocado'])

    def test_some_strings_start_with_prefix(self):
        self.assertEqual(filter_by_prefix(['banana', 'apple', 'cherry'], 'a'), ['apple'])

    def test_case_sensitive_match(self):
        self.assertEqual(filter_by_prefix(['Orange', 'Banana', 'APPLE', 'kiwi'], 'O'), ['Orange', 'APPLE'])

    def test_empty_prefix(self):
        self.assertEqual(filter_by_prefix(['cat', 'dog', 'mouse'], ''), ['cat', 'dog', 'mouse'])

    def test_strings_with_prefix_followed_by_numbers(self):
        self.assertEqual(filter_by_prefix(['1apple', '2orange', '3kiwi', 'apple', 'orange'], 'a'), ['apple', 'orange'])

    def test_case_insensitive_match(self):
        self.assertEqual(filter_by_prefix(['Orange', 'Banana', 'APPLE', 'KiWI'], 'o'), ['Orange', 'APPLE', 'KiWI'])

    def test_strings_with_leading_spaces(self):
        self.assertEqual(filter_by_prefix([' apple ', 'banana', ' cherry '], 'a'), [' apple ', 'banana'])

    def test_multiple_prefixes(self):
        self.assertEqual(filter_by_prefix(['apple', 'appletree', 'banana', 'grape', 'orange'], 'a'), ['apple', 'banana'])

    def test_strings_with_non_alphabetic_characters(self):
        self.assertEqual(filter_by_prefix(['123apple456', '!orange@', '789kiwi012'], 'a'), ['123apple456'])

if __name__ == '__main__':
    unittest.main()