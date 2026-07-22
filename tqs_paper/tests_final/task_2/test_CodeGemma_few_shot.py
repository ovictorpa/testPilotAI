from how_many_times import *
import unittest

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times("", "a"), 0)


if __name__ == '__main__':
    unittest.main()