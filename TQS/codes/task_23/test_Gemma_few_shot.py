from cal_electbill import *
import unittest

class TestCalElectBill(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(cal_electbill(20), 89)

    def test_midrange(self):
        self.assertEqual(cal_electbill(80), 238)

    def test_large(self):
        self.assertEqual(cal_electbill(250), 483)

    def test_units_less_than_50(self):
        self.assertEqual(cal_electbill(40), 104)

    def test_units_greater_than_200(self):
        self.assertEqual(cal_electbill(260), 683)

if __name__ == '__main__':
    unittest.main()