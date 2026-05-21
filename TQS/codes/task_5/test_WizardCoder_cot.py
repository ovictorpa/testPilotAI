import unittest
from greatest_common_divisor import greatest_common_divisor

class TestGCD(unittest.TestCase):
    def test_edge_cases(self):
        self.assertEqual(greatest_common_divisor(0, 5), 0)
        self.assertEqual(greatest_common_divisor(5, 0), 0)
        
        with self.assertRaises(TypeError):
            greatest_common_divisor(1.5, 4)
            
        with self.assertRaises(TypeError):
            greatest_common_divisor("a", "b")
            
    # More edge cases to be added here...