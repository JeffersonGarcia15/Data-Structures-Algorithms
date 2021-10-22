import unittest
from Strings import halves_are_alike


class TestHalvesAreAlike(unittest.TestCase):
    def test_halves_are_alike(self):
        string = "book"
        expected = True
        actual = halves_are_alike.halvesAreAlike(string)
        self.assertEqual(actual, expected)

    def test_halves_are_alike_2(self):
        string = "textbook"
        expected = False
        actual = halves_are_alike.halvesAreAlike(string)
        self.assertEqual(actual, expected)

    def test_halves_are_alike_3(self):
        string = "MerryChristmas"
        expected = False
        actual = halves_are_alike.halvesAreAlike(string)
        self.assertEqual(actual, expected)

    def test_halves_are_alike_4(self):
        string = "AbCdEfGh"
        expected = True
        actual = halves_are_alike.halvesAreAlike(string)
        self.assertEqual(actual, expected)
