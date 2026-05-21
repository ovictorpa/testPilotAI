from all_prefixes import *
import unittest


def all_prefixes(string: str) -> List[str]:

    result = []

    for i in range(len(string)):
        result.append(string[:i + 1])

    return result


class TestAllPrefixes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), [])

    def test_single_letter(self):
        self.assertEqual(all_prefixes('a'), ['a'])

    def test_multiple_letters(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])


if __name__ == '__main__':
    unittest.main()