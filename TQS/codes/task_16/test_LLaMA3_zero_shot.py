from remove_Occ import *
import unittest
from io import StringIO
import sys

def remove_Occ(s, ch):
    # your function implementation here...

class TestRemoveOccFunction(unittest.TestCase):

    def test_remove_occ_from_start(self):
        s = "hello world"
        ch = 'l'
        self.assertEqual(remove_Occ(s, ch), "helow ")

    def test_remove_occ_from_end(self):
        s = "hello world"
        ch = 'd'
        self.assertEqual(remove_Occ(s, ch), "hell o")

    def test_remove_occ_from_middle(self):
        s = "hello world"
        ch = 'l'
        self.assertEqual(remove_Occ(s, ch), "heo worl ")

    def test_no_occurrence(self):
        s = "hello world"
        ch = '!'

        # since you didn't provide the implementation for remove_Occ,
        # we assume it will throw an exception when no occurrence is found
        with self.assertRaises(ValueError):
            remove_Occ(s, ch)

    def test_empty_string(self):
        s = ""
        ch = 'a'
        expected_output = ""

        self.assertEqual(remove_Occ(s, ch), expected_output)

if __name__ == '__main__':
    unittest.main()