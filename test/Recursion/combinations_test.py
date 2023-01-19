import unittest
from Recursion import combinations


class TestCombinations(unittest.TestCase):
    def test_combinations_when_n_is_3_and_k_is_1(self):
        n = 3
        k = 1
        expected = 3
        actual = combinations.combinations(n, k)
        self.assertEqual(actual, expected)

    def test_combinations_when_n_is_3_and_k_is_2(self):
        n = 3
        k = 2
        expected = 3
        actual = combinations.combinations(n, k)
        self.assertEqual(actual, expected)
    
    def test_combinations_when_n_is_3_and_k_is_3(self):
        n = 3
        k = 3
        expected = 1
        actual = combinations.combinations(n, k)
        self.assertEqual(actual, expected)
        
    def test_combinations_when_n_is_4_and_k_is_2(self):
        n = 4
        k = 2
        expected = 6
        actual = combinations.combinations(n, k)
        self.assertEqual(actual, expected)
    
    def test_combinations_when_n_is_4_and_k_is_3(self):
        n = 4
        k = 3
        expected = 4
        actual = combinations.combinations(n, k)
        self.assertEqual(actual, expected)