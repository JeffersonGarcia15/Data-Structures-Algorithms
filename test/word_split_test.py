import unittest
from Recursion import word_split

class TestWordSplit(unittest.TestCase):
    def test_word_split(self):
        phrase = "themanran"
        listOfWords = ['the', 'man', 'ran']
        expected = ['the', 'man', 'ran']
        actual = word_split.wordSplit(phrase, listOfWords)
        self.assertEqual(expected, actual)
        
    def test_word_split_2(self):
        phrase = "ilovedogsJohn"
        listOfWords = ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']
        expected = ['i', 'love', 'dogs', 'John']
        actual = word_split.wordSplit(phrase, listOfWords)
        self.assertEqual(expected, actual)
        
    def test_word_split_3(self):
        phrase = "themanran"
        listOfWords = ['clown', 'ran', 'man']
        expected = []
        actual = word_split.wordSplit(phrase, listOfWords)
        self.assertEqual(expected, actual)
