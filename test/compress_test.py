import unittest
from Strings import compress


class TestCompress(unittest.TestCase):
    def test_compress(self):
        string = "ccaaatsss"
        expected = "2c3at3s"
        actual = compress.compress(string)
        self.assertEqual(expected, actual)

    def test_compress_2(self):
        string = "ssssbbz"
        expected = "4s2bz"
        actual = compress.compress(string)
        self.assertEqual(expected, actual)

    def test_compress_3(self):
        string = "ppoppppp"
        expected = "2po5p"
        actual = compress.compress(string)
        self.assertEqual(expected, actual)

    def test_compress_4(self):
        string = "nnneeeeeeeeeeeezz"
        expected = "3n12e2z"
        actual = compress.compress(string)
        self.assertEqual(expected, actual)

    def test_compress_5(self):
        def helper(value):
            return ''.join(['y' for _ in range(value)])
        expected = "127y"
        actual = compress.compress(helper(127))
        self.assertEqual(expected, actual)
