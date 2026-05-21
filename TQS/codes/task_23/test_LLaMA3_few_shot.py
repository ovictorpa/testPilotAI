import unittest
from cal_electbill import cal_electbill # replace 'your_module' with actual name of where you defined your cal_electbill function

class TestCalElectBill(unittest.TestCase):

    def test_small_units(self):
        self.assertEqual(cal_electbill(1), 55.25)

    def test_medium_units(self):
        self.assertEqual(cal_electbill(50), 130 + 162.5 + 25)
        
    def test_large_units(self):
        self.assertEqual(cal_electbill(100), 275 + 35)
        
    def test_even_larger_units(self):
        self.assertEqual(cal_electbill(200), 550 + 45)
        
    def test_max_units(self):
        self.assertEqual(cal_electbill(300), 1360.25)

    def test_zero_units(self):
        self.assertEqual(cal_electbill(0), 130)

if __name__ == '__main__':
    unittest.main()