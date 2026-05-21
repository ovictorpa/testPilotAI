import unittest
from cal_electbill import cal_electbill # assuming the file name of the code to be tested is "electbill.py"

class TestCalElectBill(unittest.TestCase):
    
    def test_cal_electbill(self):
        self.assertEqual(cal_electbill(49), 108.6) # 2.6*49 = 117.2, surcharge = 25 (25 + 11.6 + 25)
        self.assertEqual(cal_electbill(50), 130 + 25) # 2.6*50 = 130, surcharge = 25
        self.assertAlmostEqual(cal_electbill(99), 187.14) # 2.6*45 = 117.2 + 3.25*5 (130 + 5*(130,25))
        self.assertAlmostEqual(cal_electbill(119), 287.36) # 2.6*45 + 1.25*5 = 130 + (162.5 + 5*(8.45))
        self.assertAlmostEqual(cal_electbill(199), 517.75) # 2.6*45 + 1.25*5 = 130 + (162.5 + 4*(8.45))
        self.assertAlmostEqual(cal_electbill(200), 907.75) # 130 + 162.5 + 526 + 8.45*5 (130 + 5*(8.45))
        self.assertAlmostEqual(cal_electbill(21), 52.17) # 2.6*21 = 52.6, surcharge = 25 (25 + 2.6)