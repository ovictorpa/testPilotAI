from cal_electbill import *
import unittest

class TestElectricBillCalculation(unittest.TestCase):
    def test_units_below_50(self):
        self.assertEqual(cal_electbill(40), 104.00)  # 40 units * $2.60 each + $25 surcharge

    def test_units_between_50_and_100(self):
        self.assertEqual(cal_electbill(80), 237.00)  # 80 units (50+30) * $3.25 each + $35 surcharge

    def test_units_between_100_and_200(self):
        self.assertEqual(cal_electbill(150), 496.75)  # 100 units * $3.25 + 50 units * $5.26 each + $45 surcharge

    def test_units_above_200(self):
        self.assertEqual(cal_electbill(250), 1418.75)  # 200 units * $8.45 + 50 units * $5.26 each + $75 surcharge

    def test_units_exactly_at_threshold_50(self):
        self.assertEqual(cal_electbill(50), 185.00)  # 50 units * $2.60 each + $25 surcharge

    def test_units_exactly_at_threshold_100(self):
        self.assertEqual(cal_electbill(100), 325.00)  # 50 units * $2.60 + 50 units * $3.25 each + $35 surcharge

    def test_units_exactly_at_threshold_200(self):
        self.assertEqual(cal_electbill(200), 1193.75)  # 100 units * $3.25 + 100 units * $5.26 + 50 units * $8.45 each + $75 surcharge

    def test_zero_units(self):
        self.assertEqual(cal_electbill(0), 25.00)  # No amount for zero units + $25 surcharge

    def test_negative_units(self):
        with self.assertRaises(ValueError):
            cal_electbill(-10)  # Should raise an error for negative units

    def test_units_greater_than_200(self):
        with self.assertRaises(ValueError):
            cal_electbill(300)  # Should raise an error for units exceeding 200

    def test_units_zero(self):
        self.assertEqual(cal_electbill(0), 0.00)  # No charge for zero usage

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            cal_electbill(-50)  # Invalid input should raise an error

if __name__ == '__main__':
    unittest.main()