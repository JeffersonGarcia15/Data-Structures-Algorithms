import unittest
from Strings import anagrams


class TestAnagrams(unittest.TestCase):
    def test_anagrams(self):
        # result = anagrams.anagrams('restful', 'fluster')
        # self.assertTrue(result)
        s1 = 'restful'
        s2 = 'fluster'
        expected = True
        actual = anagrams.anagrams(s1, s2)
        self.assertEqual(actual, expected)

    def test_anagrams_2(self):
        # result = anagrams.anagrams('cats', 'tocs')
        # self.assertFalse(result)
        s1 = 'cats'
        s2 = 'tocs'
        expected = False
        actual = anagrams.anagrams(s1, s2)
        self.assertEqual(actual, expected)

    def test_anagrams_3(self):
        s1 = 'monkeyswrite'
        s2 = 'newyorktimes'
        expected = True
        actual = anagrams.anagrams(s1, s2)
        self.assertEqual(actual, expected)

    def test_anagrams_4(self):
        s1 = 'paper'
        s2 = 'reapa'
        expected = False
        actual = anagrams.anagrams(s1, s2)
        self.assertEqual(actual, expected)

    def test_anagrams_5(self):
        s1 = 'elbow'
        s2 = 'below'
        expected = True
        actual = anagrams.anagrams(s1, s2)
        self.assertEqual(actual, expected)

    def test_anagrams_6(self):
        s1 = 'tax'
        s2 = 'taxi'
        expected = False
        actual = anagrams.anagrams(s1, s2)
        self.assertEqual(actual, expected)

    def test_anagrams_6(self):
        s1 = 'taxi'
        s2 = 'tax'
        expected = False
        actual = anagrams.anagrams(s1, s2)
        self.assertEqual(actual, expected)

    def test_anagrams_7(self):
        s1 = 'night'
        s2 = 'thing'
        expected = True
        actual = anagrams.anagrams(s1, s2)
        self.assertEqual(actual, expected)

    def test_anagrams_8(self):
        s1 = 'abbc'
        s2 = 'aabc'
        expected = False
        actual = anagrams.anagrams(s1, s2)
        self.assertEqual(actual, expected)
