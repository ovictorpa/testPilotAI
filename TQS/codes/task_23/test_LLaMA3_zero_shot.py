from cal_electbill import *
import unittest

class TestCalE ElectBill(unittest.TestCase):

    def test_small_units(self):
        # Test for units < 50
        self.assertEqual(cal_electbill(40), 65.2, "Incorrect amount for small units")

    def test_medium_units(self):
        # Test for units <= 100
        self.assertEqual(cal_electbill(60), 171.5, "Incorrect amount for medium units")
        self.assertEqual(cal_electbill(50), 165.0, "Incorrect amount for medium units")

    def test_large_units(self):
        # Test for units <= 200
        self.assertEqual(cal_electbill(150), 561.45, "Incorrect amount for large units")
        self.assertEqual(cal_electbill(100), 455.0, "Incorrect amount for large units")

    def test_largest_units(self):
        # Test for units > 200
        self.assertEqual(cal_electbill(250), 1431.65, "Incorrect amount for largest units")
        self.assertEqual(cal_electbill(201), 1216.45, "Incorrect amount for largest units")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            cal_electbill("invalid")

if __name__ == '__main__':
    unittest.main()