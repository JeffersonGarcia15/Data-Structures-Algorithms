import unittest
from Sorting import bubble_sort


class SelectionSortTest(unittest.TestCase):
    def test_bubble_sortt(self):
        input = [3, 4, 1, 6, 2, 5, 7]
        expected = [1, 2, 3, 4, 5, 6, 7]
        actual = bubble_sort.bubble_sort(input)
        self.assertEqual(expected, actual)

    def test_bubble_sort_reversed_sorted(self):
        input = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = bubble_sort.bubble_sort(input)
        self.assertEqual(expected, actual)

    def test_bubble_sort_already_sorted(self):
        input = [1, 2, 3, 4, 5, 6, 7]
        expected = [1, 2, 3, 4, 5, 6, 7]
        actual = bubble_sort.bubble_sort(input)
        self.assertEqual(expected, actual)

    def test_bubble_sort_negative_input(self):
        input = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
        expected = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
        actual = bubble_sort.bubble_sort(input)
        self.assertEqual(expected, actual)
