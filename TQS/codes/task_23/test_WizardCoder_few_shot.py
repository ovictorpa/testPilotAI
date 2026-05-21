import unittest
from cal_electbill import cal_electbill

class TestCalElectBill(unittest.TestCase):
    def test_cal_electbill(self):
        self.assertEqual(cal_electbill(25), 130 + 25)
        self.assertAlmostEqual(cal_electbill(50), 130.00, delta=0.01)
        self.assertAlmostEqual(cal_electbill(75), 130.00 + (75-50)*3.25 + 35, delta=0.01)
        self.assertAlmostEqual(cal_electbill(100), 130.00 + 84.05, delta=0.01)
        self.assertAlmostEqual(cal_electbill(150), 130.00 + 162.50 + (150-100)*5.26 + 45, delta=0.01)