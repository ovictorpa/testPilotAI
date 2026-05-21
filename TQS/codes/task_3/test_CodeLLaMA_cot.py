from is_happy import *
import unittest

class TestIsHappy(unittest.TestCase):
    def test_empty_string(self):
        self.assertFalse(is_happy(''))

    def test_length_2_or_less(self):
        for length in range(2, 4):
            self.assertFalse(is_happy('a' * length))

    def test_single_character_no_duplicates(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertTrue(is_happy(char))

    def test_single_character_duplicates(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertFalse(is_happy(char * 2))

    def test_multiple_non_consecutive_letters_distinct(self):
        for i in range(3, 10):
            string = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(i))
            self.assertTrue(is_happy(string))

    def test_multiple_non_consecutive_letters_not_distinct(self):
        for i in range(3, 10):
            string = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(i))
            self.assertFalse(is_happy(string[::-1]))

    def test_multiple_consecutive_letters_distinct(self):
        for i in range(3, 10):
            string = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(i))
            self.assertTrue(is_happy(string + string[::-1]))

    def test_multiple_consecutive_letters_not_distinct(self):
        for i in range(3, 10):
            string = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(i))
            self.assertFalse(is_happy(string + string[::-1][1:]))