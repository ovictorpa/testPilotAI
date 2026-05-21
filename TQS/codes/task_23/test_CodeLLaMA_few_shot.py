from cal_electbill import *
import unittest

class TestCalcElectricBill(unittest.TestCase):
    def test_small_usage(self):
        self.assertEqual(cal_electric_bill(25), 63)

    def test_medium_usage(self):
        self.assertEqual(cal_electric_bill(105), 475)

    def test_large_usage(self):
        self.assertEqual(cal_electric_bill(300), 1295)