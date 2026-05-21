import unittest
from greatest_common_divisor import greatest_common_divisor

class TestGreatestCommonDivisor(unittest.TestCase):
    
    def test_greatest_common_divisor(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)
        self.assertEqual(greatest_common_divisor(-10, -20), 5)
        self.assertNotEqual(greatest_common_divisor(3, 4), 2)
        
if __name__ == '__main__':
    unittest.main()