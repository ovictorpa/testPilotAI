import unittest
from greatest_common_divisor import greatest_common_divisor

class TestGCD(unittest.TestCase):
    
    def test_greatest_common_divisor(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)