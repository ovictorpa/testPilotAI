from is_happy import *
import unittest

class TestIsHappyFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(is_happy(""))

    def test_short_string(self):
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("aa"))

    def test_happy_string(self):
        self.assertTrue(is_happy("abcd"))
        self.assertTrue(is_happy("adb"))
        self.assertTrue(is_happy("xyz"))

    def test_not_happy_string(self):
        self.assertFalse(is_happy("aabb"))
        self.assertFalse(is_happy("xyy"))
        self.assertFalse(is_happy("aaab"))

    def test_edge_case(self):
        self.assertTrue(is_happy("a" * 3))

if __name__ == '__main__':
    unittest.main()