from concatenate_nested import *
import unittest
class TestConcatenateNested(unittest.TestCase):
    def test_concatenate_nested(self):
        self.assertEqual(concatenate_nested((1,2), (3,4)), (1,2,3,4))
        
    def test_concatenate_nested_empty(self):
        self.assertEqual(concatenate_nested(()), ())
        
    def test_concatenate_nested_one_argument(self):
        with self.assertRaises(TypeError):
            concatenate_nested((1,2))
            
    def test_concatenate_nested_wrong_type(self):
        with self.assertRaises(TypeError):
            concatenate_nested("hello", 4)
        
    def test_concatenate_nested_same_size(self):
        t1 = [(1,2), (3,4)]
        t2 = [(5,6), (7,8)]
        self.assertEqual(concatenate_nested(*t1, *t2), ((1,2),(3,4),(5,6),(7,8))