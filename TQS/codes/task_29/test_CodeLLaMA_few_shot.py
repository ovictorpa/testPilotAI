import unittest
from concatenate_nested import concatenate_nested

class TestConcatenateNested(unittest.TestCase):
    def test_concatenate_nested(self):
        test_tup1 = ("a", ("b", "c"))
        test_tup2 = ("d", ("e", "f"))
        expected = ("ad", ("be", "cf"))
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), expected)

    def test_concatenate_nested_empty(self):
        test_tup1 = ()
        test_tup2 = ()
        expected = ()
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), expected)

    def test_concatenate_nested_single(self):
        test_tup1 = ("a",)
        test_tup2 = ("b",)
        expected = ("ab",)
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), expected)

    def test_concatenate_nested_mixed(self):
        test_tup1 = ("a", ("b", "c"))
        test_tup2 = ("d", ("e", "f"))
        expected = ("ad", ("be", "cf"))
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), expected)

    def test_concatenate_nested_mixed_empty(self):
        test_tup1 = ()
        test_tup2 = ("d", ("e", "f"))
        expected = ("d", ("e", "f"))
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), expected)

    def test_concatenate_nested_mixed_single(self):
        test_tup1 = ("a",)
        test_tup2 = ("b", ("c", "d"))
        expected = ("ab", ("c", "d"))
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), expected)

if __name__ == '__main__':
    unittest.main()