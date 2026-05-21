from intersperse import *
import unittest
from typing import List, Any

class TestIntersperseFunction(unittest.TestCase):
    def test_empty_list(self) -> None:
        self.assertEqual(intersperse([], 4), [])

    def test_single_element(self) -> None:
        self.assertEqual(intersperse([1], 0), [1, 0])
        self.assertEqual(intersperse([3.5], 9.2), [3.5, 9.2])

    def test_multiple_elements(self) -> None:
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])
        self.assertEqual(intersperse([5, -1, 6], '-'), ['5', '-', '-1', '-', '6'])

    def test_delimiter_is_an_element(self) -> None:
        self.assertEqual(intersperse([7, 8, 7], 7), [7, 8, 7])
        self.assertEqual(intersperse(['a', 'b', 'a'], 'a'), ['a', 'b', 'a'])

    def test_mixed_types_list(self) -> None:
        self.assertEqual(intersperse([1, 'hello', 3.5], '#'), [1, '#', 'hello', '#', 3.5])

    def test_duplicate_elements(self) -> None:
        self.assertEqual(intersperse([1, 2, 1, 3], '|'), [1, '|', 2, '|', 1, '|', 3])

    def test_non_hashable_types(self) -> None:
        with self.assertRaises(TypeError):
            intersperse([(1, 2)], 3)

    def test_delimiter_with_string_elements(self) -> None:
        self.assertEqual(intersperse(['apple', 'banana'], '-'), ['apple', '-', 'banana'])

    def test_negative_delimiter(self) -> None:
        self.assertEqual(intersperse([-1, 2, -1], -4), [-1, -4, 2, -4, -1])

    def test_non_integer_delimiter(self) -> None:
        self.assertEqual(intersperse([0, 1, 2, 3], 'X'), [0, 'X', 1, 'X', 2, 'X', 3])
        self.assertEqual(intersperse(['word', 'hello'], '#'), ['word', '#', 'hello', '#'])

    def test_mixed_delimiter_types(self) -> None:
        self.assertEqual(intersperse([1, 2], 'a'), [1, 'a', 2])
        self.assertEqual(intersperse(['a', 'b'], 1), ['a', 1, 'b'])

    def test_none_delimiter(self) -> None:
        self.assertIsNone(intersperse([], None))
        self.assertEqual(intersperse([0, 1, 2], None), [0, None, 1, None, 2])

if __name__ == '__main__':
    unittest.main()