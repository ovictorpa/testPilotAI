from is_happy import *
import unittest

class TestIsHappy(unittest.TestCase):
    
    def test_is_happy_false(self):
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("aa"))
        self.assertFalse(is_happy("abcd"))
        self.assertFalse(is_happy("aabb"))
    
    def test_is_happy_true(self):
        self.assertTrue(is_happy("adb"))
        self.assertTrue(is_happy("xyy"))
        self.assertTrue(is_happy("xyz"))