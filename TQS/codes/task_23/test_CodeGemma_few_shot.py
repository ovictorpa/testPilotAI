from cal_electbill import *
import unittest

class TestCalElectbill(unittest.TestCase):

    def test_units_less_than_50(self):
        self.assertEqual(cal_electbill(40), 105)

    def test_units_between_50_and_100(self):
        self.assertEqual(cal_electbill(70), 285)

    def test_units_between_100_and_200(self):
        self.assertEqual(cal_electbill(150), 537.5)

    def test_units_greater_than_200(self):
        self.assertEqual(cal_electbill(250), 957.5)

if __name__ == '__main__':
    unittest.main()