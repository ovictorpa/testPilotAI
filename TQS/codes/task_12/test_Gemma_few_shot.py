from longest import *
import unittest


def longest(strings: List[str]) -> Optional[str]:

    if not strings:
        return None

    maxlen = max(len(x) for x in strings)

    for s in strings:
        if len(s) == maxlen:
            return s


def test_longest():
    test_cases = [
        ([], None),
        (['a', 'b', 'c'], 'a'),
        (['a', 'bb', 'ccc'], 'ccc'),
        (['aa', 'bb', 'c', 'cc'], 'aa'),
    ]

    for input_, expected in test_cases:
        with unittest.subTest(f"input: {input_}, expected: {expected}"):
            result = longest(input_)
            unittest.assertEqual(result, expected)


class TestLongest(unittest.TestCase):
    def test_basic(self):
        self.assertIsNone(longest([]))

    def test_empty_list(self):
        self.assertIsNone(longest([""]))

    def test_single_element(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_elements(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_longer_strings(self):
        self.assertEqual(longest(['aa', 'bb', 'c', 'cc']), 'aa')


if __name__ == '__main__':
    unittest.main()