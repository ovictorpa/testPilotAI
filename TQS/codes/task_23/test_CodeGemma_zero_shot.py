from cal_electbill import *
import unittest

class TestCalElectbill(unittest.TestCase):

    def test_units_less_than_50(self):
        units = 40
        expected_total = 104.0
        total = cal_electbill(units)
        self.assertEqual(total, expected_total)

    def test_units_between_50_and_100(self):
        units = 75
        expected_total = 262.5
        total = cal_electbill(units)
        self.assertEqual(total, expected_total)

    def test_units_between_100_and_200(self):
        units = 150
        expected_total = 437.5
        total = cal_electbill(units)
        self.assertEqual(total, expected_total)

    def test_units_greater_than_200(self):
        units = 250
        expected_total = 744.0
        total = cal_electbill(units)
        self.assertEqual(total, expected_total)

if __name__ == '__main__':
    unittest.main()