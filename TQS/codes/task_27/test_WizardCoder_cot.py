import unittest
from remove_multiple_spaces import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):
  def test_empty_string(self):
    self.assertEqual(remove_multiple_spaces(""), "")
  
  def test_single_word(self):
    self.assertEqual(remove_multiple_spaces("hello"), "hello")
  
  def test_multiple_words(self):
    self.assertEqual(remove_multiple_spaces("   hello world   "), "hello world")
    self.assertEqual(remove_multiple_spaces("  this is a     test  "), "this is a test")
    
  def test_numbers(self):
    self.assertEqual(remove_multiple_spaces("12345       67890"), "12345 67890")
    self.assertEqual(remove_multiple_spaces("  123     456        7890"), "123 456 7890")
    
  def test_special_characters(self):
    self.assertEqual(remove_multiple_spaces("!!!@#$%^&*()_+-="), "!!!@#$%^&*()_+-=")
    self.assertEqual(remove_multiple_spaces("#$%%@    #$%@^&"), "#$%%@ #$%@^&")
  
  def test_mixed_string(self):
    self.assertEqual(remove_multiple_spaces("hello world   how are you"), "hello world how are you")
    self.assertEqual(remove_multiple_spaces("#$$$##%^&*()@&&*()&^%^^^^    testing 123"), "#$$$##%^&*()@&&*()&^%^^^^ testing 123")
    
if __name__ == '__main__':
    unittest.main()