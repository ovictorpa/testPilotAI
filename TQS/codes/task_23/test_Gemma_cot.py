from cal_electbill import *
import unittest

class TestCalElectbill(unittest.TestCase):

    def test_basic_billing(self):
        units = 30
        expected_amount = 30 * 2.60
        actual_amount = cal_electbill(units)
        self.assertEqual(actual_amount, expected_amount)

    def test_small_surcharge(self):
        units = 40
        expected_amount = 40 * 2.60 + 25
        actual_amount = cal_electbill(units)
        self.assertEqual(actual_amount, expected_amount)

    def test_medium_billing(self):
        units = 80
        expected_amount = 130 + (80 - 50) * 3.25 + 35
        actual_amount = cal_electbill(units)
        self.assertEqual(actual_amount, expected_amount)

    def test_large_billing(self):
        units = 250
        expected_amount = 130 + 162.50 + 526 + (250 - 200) * 8.45 + 75
        actual_amount = cal_electbill(units)
        self.assertEqual(actual_amount, expected_amount)

    def test_negative_units(self):
        with self.assertRaises(ValueError):
            cal_electbill(-10)

if __name__ == '__main__':
    unittest.main()