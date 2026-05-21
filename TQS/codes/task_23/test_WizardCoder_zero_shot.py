from cal_electbill import *
import unittest

class TestCalElectbill(unittest.TestCase):
    
    def test_electricity_bill(self):
        self.assertEqual(cal_electbill(5), 2.6) #for units < 50
        self.assertEqual(cal_electbill(10), 49.75) # for units between 50 and 100
        self.assertEqual(cal_electbill(50), 132.6) #for units = 50
        self.assertEqual(cal_electbill(100), 497.50) # for units between 100 and 200
        self.assertEqual(cal_electbill(200), 862.60) #for units = 200
        self.assertEqual(cal_electbill(300), 1574.15) #for units > 200
        
if __name__ == '__main__':
    unittest.main()