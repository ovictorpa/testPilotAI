import unittest
from filter_by_prefix import filter_by_prefix  # Replace 'your_module' with the actual name of the module

class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_single_element_list(self):
        result = filter_by_prefix(['abc', 'bcd', 'cde'], 'a')
        expected_result = ['abc']
        self.assertEqual(result, expected_result)

    def test_multi_element_list(self):
        result = filter_by_prefix(['abc', 'bcd', 'def'], 'b')
        expected_result = ['bcd']
        self.assertEqual(result, expected_result)

    def test_empty_prefix(self):
        self.assertEqual(filter_by_prefix(['a', 'ab', 'abc'], ''), [])

    def test_non_string_input_in_list(self):
        with self.assertRaises(TypeError):
            filter_by_prefix(['abc', 123, 'def'], 'b')

if __name__ == '__main__':
    unittest.main()