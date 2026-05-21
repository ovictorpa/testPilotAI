from cal_electbill import *
import unittest

class TestCalElectBill(unittest.TestCase):

    def test_small_units(self):
        self.assertEqual(cal_electbill(40), 104)

    def test_medium_units(self):
        self.assertEqual(cal_electbill(80), 190)

    def test_large_units(self):
        self.assertEqual(cal_electbill(150), 307.5)

    def test_very_large_units(self):
        self.assertEqual(cal_electbill(250), 482.5)

if __name__ == '__main__':
    unittest.main()