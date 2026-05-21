import unittest

from TQS.tests_final.task_14.filter_by_prefix import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_single_match(self):
        self.assertEqual(filter_by_prefix(['abc'], 'a'), ['abc'])

    def test_multiple_matches(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_no_matches(self):
        self.assertEqual(filter_by_prefix(['bcd', 'cde'], 'a'), [])

    def test_mixed_case(self):
        self.assertEqual(filter_by_prefix(['aBc', 'bCd'], 'a'), ['aBc'])

if __name__ == '__main__':
    unittest.main()