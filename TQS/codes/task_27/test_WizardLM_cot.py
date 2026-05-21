from remove_multiple_spaces import *
import unittest
import re

def remove_multiple_spaces(text1):
    return re.sub(' +', ' ', text1)

class TestRemoveMultipleSpaces(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(remove_multiple_spaces("This  is a test"), "This is a test")
    
    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_multiple_spaces("   This   is   a test   "), "This is a test")
    
    def test_single_space(self):
        self.assertEqual(remove_multiple_spaces("This is a test"), "This is a test")
    
    def test_no_spaces(self):
        self.assertEqual(remove_multiple_spaces("NoSpacesHere"), "NoSpacesHere")
    
    def test_empty_string(self):
        self.assertEqual(remove_multiple_spaces(""), "")
    
    def test_punctuation_near_spaces(self):
        self.assertEqual(remove_multiple_spaces("This, is a test!"), "This, is a test!")
    
    def test_mixed_tabs_and_spaces(self):
        text_with_tabs = "Some\t text with  multiple spaces"
        self.assertEqual(remove_multiple_spaces(text_with_tabs), "Some	 text with multiple spaces")
    
    def test_unicode_spaces(self):
        text_with_whitespace = "\u00A0This\u3000is a test."
        self.assertEqual(remove_multiple_spaces(text_with_whitespace), "This	is a test.")
    
    def test_narrow_wide_spaces(self):
        text_with_narrow_spaces = "Use\uFEFFmultiple\u3000spaces"
        self.assertEqual(remove_multiple_spaces(text_with_narrow_spaces), "Use multiple spaces")
    
    def test_matched_and_unmatched_groups(self):
        text = "This...is a test with  several  multiple   spaces."
        self.assertEqual(remove_multiple_spaces(text), "This...is a test with several multiple spaces.")
    
    def test_regex_pattern_limitations(self):
        text = "This---is a test"
        self.assertEqual(remove_multiple_spaces(text), "This-is a test")
    
    def test_non_consecutive_spaces(self):
        text = "This  space is not  consecutive with the next one."
        self.assertEqual(remove_multiple_spaces(text), "This space is not consecutive with the next one.")

if __name__ == '__main__':
    unittest.main()