from concatenate_nested import *
import unittest

class TestConcatenateNested(unittest.TestCase):
    def test_concatenate_nested(self):
        self.assertEqual(concatenate_nested((1, (2, 3)), (4, (5, 6))), (1, (2, 3), 4, (5, 6)))

    def test_non_nested_tuple(self):
        with self.assertRaises(TypeError):
            concatenate_nested(((1, 2), 3), (4, (5, 6)))

    def test_original_tuple(self):
        self.assertEqual(concatenate_nested((1, 2, 3), (4, 5, 6)), (1, 2, 3, 4, 5, 6))

    def test_deeply_nested_tuple(self):
        self.assertEqual(concatenate_nested(((1, (2, (3, 4))), ((5, 6), (7, 8)))), ((1, (2, (3, 4)), (5, 6), (7, 8))))