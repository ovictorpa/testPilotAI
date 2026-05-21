from cal_electbill import *
[PYTHON]
import unittest

class TestCalcElectricBill(unittest.TestCase):
    def test_calculate_bill_less_than_50_units(self):
        self.assertEqual(cal_electbill(49), 108)

    def test_calculate_bill_more_than_50_but_less_than_or_equal_to_100_units(self):
        self.assertEqual(cal_electbill(50), 260)
        self.assertEqual(cal_electbill(101), 391)

    def test_calculate_bill_more_than_100_but_less_than_or_equal_to_200_units(self):
        self.assertEqual(cal_electbill(102), 783)
        self.assertEqual(cal_electbill(199), 1519)
        self.assertEqual(cal_electbill(201), 1541)

    def test_calculate_bill_more_than_200_units(self):
        self.assertEqual(cal_electbill(202), 3163)
        self.assertEqual(cal_electbill(399), 5749)
        self.assertEqual(cal_electbill(401), 5771)

if __name__ == '__main__':
    unittest.main()