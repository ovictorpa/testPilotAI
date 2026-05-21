import unittest

from TQS.tests_final.task_1.intersperse import intersperse

class TestIntersperse(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_two_element_list(self):
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2])

    def test_three_element_list(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_non_integer_delimiter(self):
        self.assertEqual(intersperse([1, 2], "a"), [1, "a", 2])

if __name__ == "__main__":
    unittest.main()