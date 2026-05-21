from cal_electbill import *
import unittest

class TestElectBillCalculation(unittest.TestCase):

    def test_negative_units(self):
        # Units cannot be negative, so the function should raise an exception.
        with self.assertRaises(ValueError):
            cal_electbill(-1)

    def test_zero_units(self):
        # Zero units should result in zero bill.
        self.assertEqual(cal_electbill(0), 0)

    def test_below_threshold(self):
        self.assertAlmostEqual(cal_electbill(49), 66.2)
        self.assertEqual(cal_electbill(50), 132)

    def test_between_thresholds(self):
        # Testing the charge per unit for units between 50 and 100.
        self.assertAlmostEqual(cal_electbill(51), 157.5)
        self.assertAlmostEqual(cal_electbill(99), 235.75)

    def test_above_higher_threshold(self):
        # Testing the cubic increase in charge beyond 200 units.
        self.assertAlmostEqual(cal_electbill(201), 1211.45)
        self.assertAlmostEqual(cal_electbill(202), 1294.55)

    def test_large_units(self):
        # Testing the cubic increase in charge for a very large number of units.
        self.assertAlmostEqual(cal_electbill(500), 5312.35)

if __name__ == '__main__':
    unittest.main()