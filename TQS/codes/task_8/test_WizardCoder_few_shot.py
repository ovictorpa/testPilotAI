from has_close_elements import *
class TestCloseElements(unittest.TestCase):
    def test_has_close_elements_with_single_element(self):
        self.assertFalse(has_close_elements([1], 0.5))
        
    def test_has_close_elements_with_no_threshold(self):
        self.assertRaises(TypeError, has_close_elements, [1, 2])
        
    def test_has_close_elements_with_negative_threshold(self):
        self.assertFalse(has_close_elements([1, 2], -0.5)
        
    def test_has_close_elements_with_zero_threshold(self):
        self.assertFalse(has_close_elements([1, 2], 0)
        
    def test_has_close_elements_with_positive_threshold(self):
        self.assertTrue(has_close_elements([1, 3, 4, 5], 1)
        
    def test_has_close_elements_with_multiple_elements(self):
        self.assertFalse(has_close_elements([1, 2, 4, 6, 8], 2) # No two elements are closer than 2
        
    def test_has_close_elements_with_negative_distance(self):
        self.assertTrue(has_close_elements([-3, -1, 1], 0.5) # -3 and -1 are closer than threshold of 0.5
        
    def test_has_close_elements_with_positive_distance(self):
        self.assertTrue(has_close_elements([-3, 1, 4], 2) # 1 and 4 are closer than threshold of 2