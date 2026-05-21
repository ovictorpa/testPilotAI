from cal_electbill import *
import unittest

class TestCalcElectBill(unittest.TestCase):
    def test_cal_electbill(self):
        self.assertEqual(cal_electbill(50), 130 + 25)
        self.assertEqual(cal_electbill(100), 130 + 162.50 + 35)
        self.assertEqual(cal_electbill(200), 130 + 162.50 + 526 + 45)
        self.assertEqual(cal_electbill(250), 130 + 162.50 + 526 + 8.45 * 50 + 75)