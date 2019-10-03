from unittest import TestCase

from palindrome.app import is_palindrome, is_palindrome_recursive


class TestIs_palindrome(TestCase):
    def test_is_palindrome_valid_even(self):
        self.assertTrue(is_palindrome('otto'))

    def test_is_palindrome_valid_odd(self):
        self.assertTrue(is_palindrome('racecar'))

    def test_is_palindrome_valid_ignore_case(self):
        self.assertTrue(is_palindrome('Racecar'))

    def test_is_palindrome_valid_ignoare_space(self):
        self.assertTrue(is_palindrome('Race car'))

    def test_is_palindrome_valid_url_encoded(self):
        self.assertTrue(is_palindrome('Race%20car'))

    def test_is_palindrome_invalid(self):
        self.assertFalse(is_palindrome('toyboat'))

class TestIs_palindrome_recursive(TestCase):
    def test_is_palindrome_valid_even(self):
        self.assertTrue(is_palindrome_recursive('otto'))

    def test_is_palindrome_valid_odd(self):
        self.assertTrue(is_palindrome_recursive('racecar'))

    def test_is_palindrome_valid_ignore_case(self):
        self.assertTrue(is_palindrome_recursive('Racecar'))

    def test_is_palindrome_valid_ignoare_space(self):
        self.assertTrue(is_palindrome_recursive('Race car'))

    def test_is_palindrome_valid_url_encoded(self):
        self.assertTrue(is_palindrome_recursive('Race%20car'))

    def test_is_palindrome_invalid(self):
        self.assertFalse(is_palindrome_recursive('toyboat'))
