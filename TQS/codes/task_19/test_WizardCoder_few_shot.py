from check_Equality import *
import unittest
from unittest.mock import Mock, patch

class TestCountSubstring(unittest.TestCase):
    
    @patch('__main__.check_Equality', return_value=True)
    def test_all_equal(self, mocked_check_equility):
        self.assertEqual(count_Substring_With_Equal_Ends("hello"), 1)

    @patch('__main__.check_Equality', side_effect=[False, True])
    def test_all_not_equal(self, mocked_check_equility):
        self.assertEqual(count_Substring_With_Equal_Ends("heelo"), 1)

    @patch('__main__.check_Equality', side_effect=[True, False])
    def test_all_not_equal2(self, mocked_check_equility):
        self.assertEqual(count_Substring_With_Equal_Ends("world"), 0)

    @patch('__main__.check_Equality', return_value=False)
    def test_all_not_equal3(self, mocked_check_equility):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    @patch('__main__.check_Equality', side_effect=[True, True])
    def test_odd_length(self, mocked_check_equility):
        self.assertEqual(count_Substring_With_Equal_Ends("world"), 1)

    @patch('__main__.check_Equality', side_effect=[True, True, False])
    def test_odd_length2(self, mocked_check_equility):
        self.assertEqual(count_Substring_With_Equal_Ends("world"), 1)

    @patch('__main__.check_Equality', side_effect=[False, True])
    def test_even_length(self, mocked_check_equility):
        self.assertEqual(count_Substring_With_Equal_Ends("hello"), 2)