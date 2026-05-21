from cal_electbill import *
import unittest

class TestCalElectbill(unittest.TestCase):

    def test_units_less_than_50(self):
        units = 40
        expected_total = 104
        self.assertEqual(cal_electbill(units), expected_total)

    def test_units_between_50_and_100(self):
        units = 75
        expected_total = 272.5
        self.assertEqual(cal_electbill(units), expected_total)

    def test_units_between_100_and_200(self):
        units = 150
        expected_total = 487.5
        self.assertEqual(cal_electbill(units), expected_total)

    def test_units_greater_than_200(self):
        units = 250
        expected_total = 845
        self.assertEqual(cal_electbill(units), expected_total)

    def test_negative_units(self):
        units = -50
        with self.assertRaises(ValueError):
            cal_electbill(units)

    def test_zero_units(self):
        units = 0
        expected_total = 25
        self.assertEqual(cal_electbill(units), expected_total)

if __name__ == '__main__':
    unittest.main()