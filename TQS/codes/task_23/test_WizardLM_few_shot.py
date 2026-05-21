from cal_electbill import *
import unittest

def cal_electbill(units):
    if units < 50:
        amount = units * 2.60
        surcharge = 25
    elif units <= 100:
        amount = 130 + ((units - 50) * 3.25)
        surcharge = 35
    elif units <= 200:
        amount = 130 + 162.50 + ((units - 100) * 5.26)
        surcharge = 45
    else:
        amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
        surcharge = 75
    total = amount + surcharge
    return total

class TestCalElectBill(unittest.TestCase):
    def test_below_50_units(self):
        self.assertEqual(cal_electbill(40), 106.00)  # 40 units, should include base cost and surcharge

    def test_exactly_50_units(self):
        self.assertEqual(cal_electbill(50), 175.00)  # 50 units, should be exactly the threshold rate

    def test_up_to_100_units(self):
        self.assertEqual(cal_electbill(90), 347.50)   # 90 units, should include tier 1 + surcharge

    def test_up_to_200_units(self):
        self.assertEqual(cal_electbill(180), 865.00)  # 180 units, should include tier 1 & 2 + surcharge

    def test_above_200_units(self):
        self.assertEqual(cal_electbill(220), 1943.90) # 220 units, should include all tiers + surcharge

    def test_exact_200_units(self):
        self.assertEqual(cal_electbill(200), 865.00)   # 200 units, exactly at the threshold for tier 2

    def test_invalid_input_less_than_zero(self):
        with self.assertRaises(ValueError):
            cal_electbill(-10)  # Should raise an exception for negative input

    def test_invalid_input_not_a_number(self):
        with self.assertRaises(TypeError):
            cal_electbill('string')  # Should raise an exception for non-numeric input

if __name__ == '__main__':
    unittest.main()