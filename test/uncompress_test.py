import unittest
from Strings import uncompress


class TestUncompress(unittest.TestCase):
    def test_uncompress(self):
        string = "2c3a1t"
        expected = "ccaaat"
        actual = uncompress.uncompress(string)
        self.assertEqual(expected, actual)

    def test_uncompress_2(self):
        string = "4s2b"
        expected = "ssssbb"
        actual = uncompress.uncompress(string)
        self.assertEqual(expected, actual)

    def test_uncompress_3(self):
        string = "2p1o5p"
        expected = "ppoppppp"
        actual = uncompress.uncompress(string)
        self.assertEqual(expected, actual)

    def test_uncompress_4(self):
        string = "3n12e2z"
        expected = "nnneeeeeeeeeeeezz"
        actual = uncompress.uncompress(string)
        self.assertEqual(expected, actual)

    def test_uncompress_5(self):
        def helper(value):
            return ''.join(['y' for _ in range(value)])
        string = "127y"
        expected = helper(127)
        actual = uncompress.uncompress(string)
        self.assertEqual(expected, actual)
