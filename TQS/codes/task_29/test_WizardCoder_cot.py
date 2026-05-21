import unittest
from concatenate_nested import concatenate_nested

class TestConcatenation(unittest.TestCase):
  def test_simple_concatenation(self):
    """Test that two tuples are correctly concatenated"""
    self.assertEqual((1,2,3,4),(concatenate_nested((1,2), (3,4)))
    
    self.assertEqual((1,2,3,4,5,6,7)(concatenate_nested((1,2,(3,4),5,(6,7))
    
  def test_empty_tuples(self):
    """Test that concatenation works with empty tuples"""
    self.assertEqual((), (concatenate_nested(()))
    
  def test_mixed_types(self):
    """Test that concatenation works when one tuple has nested tuples"""
    self.assertEqual((1,2,3,4),(concatenate_nested((1,2), (3,(4)
    self.assertEqual((1,"a",2,("b"),3,True)(concatenate_nested((1,"a")(2,("b"),(3,True))
  
  def test_nested_tuples(self):
    """Test that concatenation works when both tuples have nested tuples"""
    self.assertEqual((1,2,3,(4,5),(6,7),8)(concatenate_nested((1,2)((3,(4,5)), (6,7,8)
  
if __name__ == '__main__':
  unittest.main()