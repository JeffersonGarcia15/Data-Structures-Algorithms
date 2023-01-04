import unittest
from Sorting import quick_sort_hoare_partitioning


class SelectionSortTest(unittest.TestCase):
    def test_quick_sort_hoare_partitioning(self):
        input = [3, 4, 1, 6, 2, 5, 7]
        expected = [1, 2, 3, 4, 5, 6, 7]
        actual = quick_sort_hoare_partitioning.quick_sort_hoare_partitioning(input)
        self.assertEqual(expected, actual)
    
    def test_quick_sort_hoare_partitioning_reversed_sorted(self):
        input = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = quick_sort_hoare_partitioning.quick_sort_hoare_partitioning(input)
        self.assertEqual(expected, actual)
        
    def test_quick_sort_hoare_partitioning_already_sorted(self):
        input = [1, 2, 3, 4, 5, 6, 7]
        expected = [1, 2, 3, 4, 5, 6, 7]
        actual = quick_sort_hoare_partitioning.quick_sort_hoare_partitioning(input)
        self.assertEqual(expected, actual)
        
    def test_quick_sort_hoare_partitioning_negative_input(self):
        input = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
        expected = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
        actual = quick_sort_hoare_partitioning.quick_sort_hoare_partitioning(input)
        self.assertEqual(expected, actual)