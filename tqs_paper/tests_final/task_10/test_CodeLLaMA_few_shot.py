from TQS.tests_final.task_10.sum_product import *
import unittest
from typing import List, Tuple

class TestSumProduct(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element(self):
        self.assertEqual(sum_product([1]), (1, 1))

    def test_multiple_elements(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))