import unittest
from Recursion import raise_int_to_power


class TestRaiseIntToPower(unittest.TestCase):
    def test_raise_int_to_power_when_n_is_2_and_k_is_6(self):
        n = 2
        k = 6
        expected = 64
        actual = raise_int_to_power.raise_int_to_power(n, k)
        self.assertEqual(actual, expected)
    
    def test_raise_int_to_power_when_n_is_3_and_k_is_3(self):
        n = 3
        k = 3
        expected = 27
        actual = raise_int_to_power.raise_int_to_power(n, k)
        self.assertEqual(actual, expected)
        
    def test_raise_int_to_power_when_n_is_4_and_k_is_4(self):
        n = 4
        k = 5
        expected = 1024
        actual = raise_int_to_power.raise_int_to_power(n, k)
        self.assertEqual(actual, expected)