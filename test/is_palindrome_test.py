import unittest
from Strings import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        string = 'abcba'
        expected = True
        actual = is_palindrome.is_palindrome(string)
        self.assertEqual(expected, actual)

    def test_is_palindrome_2(self):
        string = 'Jefferson'
        expected = False
        actual = is_palindrome.is_palindrome(string)
        self.assertEqual(expected, actual)

    def test_is_palindrome_3(self):
        string = 'abcdcba'
        expected = True
        actual = is_palindrome.is_palindrome(string)
        self.assertEqual(expected, actual)

    def test_is_palindrome_4(self):
        string = 'a'
        expected = True
        actual = is_palindrome.is_palindrome(string)
        self.assertEqual(expected, actual)

    def test_is_palindrome_5(self):
        string = 'ab'
        expected = False
        actual = is_palindrome.is_palindrome(string)
        self.assertEqual(expected, actual)

    def test_is_palindrome_6(self):
        string = 'aba'
        expected = True
        actual = is_palindrome.is_palindrome(string)
        self.assertEqual(expected, actual)

    def test_is_palindrome_7(self):
        string = 'abb'
        expected = False
        actual = is_palindrome.is_palindrome(string)
        self.assertEqual(expected, actual)

    def test_is_palindrome_7(self):
        string = 'abcdefghhgfedcba'
        expected = True
        actual = is_palindrome.is_palindrome(string)
        self.assertEqual(expected, actual)
