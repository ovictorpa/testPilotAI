import unittest
from how_many_times import how_many_times  # Replace 'your_module' with the actual module name where the function is defined

class TestHowManyTimes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_empty_substring(self):
        self.assertEqual(how_many_times('abcde', ''), 0)

    def test_exact_match(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_overlapping_matches(self):
        self.assertEqual(how_many_times('ababc', 'ab'), 2)

    def test_substring_at_beginning(self):
        self.assertEqual(how_many_times('abcdef', 'abcdef'), 1)

    def test_substring_at_end(self):
        self.assertEqual(how_many_times('abcdef', 'fed'), 1)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('abcde', 'f'), 0)

    def test_case_sensitivity(self):
        self.assertEqual(how_many_times('HelloWorld', 'hello').lower(), 1)
        self.assertEqual(how_many_times('HELLOWORLD', 'hello').lower(), 0)

    def test_mixed_case_substring(self):
        self.assertEqual(how_many_times('HelloWorld', 'HeLLo'), 1)
        self.assertEqual(how_many_times('HelloWorld', 'WORLD'), 1)

    def test_non_overlapping_matches(self):
        self.assertEqual(how_many_times('ababab', 'ab'), 2)

    def test_whitespace_and_special_characters(self):
        self.assertEqual(how_many_times('Hello, World!', ', Wo'), 1)

    def test_different_character_encodings(self):
        # This test assumes the function is designed to handle different encodings
        self.assertEqual(how_many_times('Buenos Aires', 'buenos ares'), 1)
        self.assertEqual(how_many_times('Buenos\nAires', 'buenos\naires'), 1)

    def test_substring_partially_matched(self):
        self.assertEqual(how_many_times('abcabc', 'bc'), 2)

if __name__ == '__main__':
    unittest.main()