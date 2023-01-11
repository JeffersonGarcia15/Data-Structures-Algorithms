import unittest
from Sorting import two_number_sum_sort_version

class TestTwoNumberSumSortVersionTest(unittest.TestCase):
    def test_two_number_sum_possible(self):
        input = [1, 2, 3, 4, 5]
        target = 5
        actual = two_number_sum_sort_version.two_number_sum_sort_version(input, target)
        self.assertTrue(actual == [1, 4] or actual == [4, 1] or actual == [2, 3] or actual == [3, 2])
    
    def test_two_number_sum_not_possible(self):
        input = [1, 2, 3, 4, 5]
        target = 11
        actual = two_number_sum_sort_version.two_number_sum_sort_version(input, target)
        self.assertTrue(actual == [])
        
    def test_two_number_sum_negative_array(self):
        input = [-1, -2, -3, -4, -5]
        target = -7
        actual = two_number_sum_sort_version.two_number_sum_sort_version(input, target)
        self.assertTrue(actual == [-2, -5] or actual == [-5, -2] or actual == [-3, -4] or actual == [-4, -3])