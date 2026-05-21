from cal_electbill import *
import unittest

def cal_electbill(units):
    if units < 50:
        amount = units * 2.60
        surcharge = 25
    elif units <= 100:
        amount = 130 + (units - 50) * 3.25
        surcharge = 35
    elif units <= 200:
        amount = 130 + 162.50 + (units - 100) * 5.26
        surcharge = 45
    else:
        amount = 130 + 162.50 + 526 + (units - 200) * 8.45
        surcharge = 75
    total = amount + surcharge
    return total

class TestCalculateElectricBill(unittest.TestCase):
    def test_below_50_units(self):
        self.assertEqual(cal_electbill(40), 104.00)

    def test_exactly_50_units(self):
        self.assertEqual(cal_electbill(50), 155.00)

    def test_between_50_and_100_units(self):
        self.assertEqual(cal_electbill(75), 268.75)

    def test_exactly_100_units(self):
        self.assertEqual(cal_electbill(100), 345.00)

    def test_between_100_and_200_units(self):
        self.assertEqual(cal_electbill(150), 647.50)

    def test_exactly_200_units(self):
        self.assertEqual(cal_electbill(200), 998.00)

    def test_above_200_units(self):
        self.assertEqual(cal_electbill(300), 2153.75)

    def test_negative_units(self):
        self.assertEqual(cal_electbill(-10), 26.00)

    def test_non_integer_units(self):
        self.assertAlmostEqual(cal_electbill(50.75), 159.38, places=2)

    def test_units_greater_than_200_with_discount(self):
        # Assuming there's a discount for using less than 300kWh
        self.assertEqual(cal_electbill(250), 1173.75)

if __name__ == '__main__':
    unittest.main()