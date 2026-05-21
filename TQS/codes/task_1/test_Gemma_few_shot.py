from intersperse import *
import unittest


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    if not numbers:
        return []
    result = []
    for n in numbers[:-1]:
        result.append(n)
        result.append(delimiter)
    result.append(numbers[-1])
    return result


class TestInterpose(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_basic_interspersion(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_delimiter_as_zero(self):
        self.assertEqual(intersperse([1, 2, 3], 0), [1, 2, 3])

    def test_delimiter_as_negative_one(self):
        with self.assertRaises(ValueError):
            intersperse([1, 2, 3], -1)


if __name__ == '__main__':
    unittest.main()