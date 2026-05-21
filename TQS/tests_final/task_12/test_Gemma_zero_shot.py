import unittest

from TQS.tests_final.task_12.longest import longest


class TestLongestString(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_string(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')


if __name__ == '__main__':
    unittest.main()