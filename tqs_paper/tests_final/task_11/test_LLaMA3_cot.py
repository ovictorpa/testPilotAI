import unittest
from TQS.tests_final.task_11.all_prefixes import all_prefixes  # replace 'your_module' with actual module name

class TestAllPrefixes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), [])

    def test_single_character_string(self):
        self.assertEqual(all_prefixes('a'), ['a'])

    def test_multiple_characters_string(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

    def test_repeated_characters_string(self):
        self.assertEqual(all_prefixes('aaa'), ['a', 'aa', 'aaa'])

    def test_input_none_type(self):
        with self.assertRaises(TypeError):
            all_prefixes(None)

    def test_input_not_string_type(self):
        with self.assertRaises(TypeError):
            all_prefixes(123)  # or any other non-string type

if __name__ == '__main__':
    unittest.main()