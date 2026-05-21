from count_distinct_characters import *
import unittest
class TestCountDistinctCharacters(unittest.TestCase):
    
    def test_count_distinct_characters1(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        
    def test_count_distinct_characters2(self):
        self.assertEqual(count_distinct_characters('Jerry'), 4)
        
    def test_count_distinct_characters3(self):
        self.assertEqual(count_distinct_characters('Mississippi'), 5) # includes 'i' twice, but only counts it once
        
    def test_count_distinct_characters4(self):
        self.assertEqual(count_distinct_characters('Python is awesome!'), 9)
        
if __name__ == '__main__':
    unittest.main()