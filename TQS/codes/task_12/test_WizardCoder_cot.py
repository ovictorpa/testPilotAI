from longest import *
import unittest
from typing import List, Optional

class TestLongest(unittest.TestCase):
    def test_edge_cases(self):
        self.assertEqual(longest([]), None)
        self.assertEqual(longest(['a']), 'a')

    def test_normal_scenario(self):
        self.assertEqual(longest(['aa', 'ccc']), 'aa')
        
if __name__ == "__main__":
    unittest.main()