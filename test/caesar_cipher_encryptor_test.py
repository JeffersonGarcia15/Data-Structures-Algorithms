import unittest
from PairBoard import caesar_cipher_encryptor

class TestCaesarCipherEncrypt(unittest.TestCase):
    def test_caesar_cipher_encryptor(self):
        string = 'xyz'
        key = 2
        actual = caesar_cipher_encryptor.caesarCipherEncryptor(string, key)
        expected = 'zab'
        self.assertEqual(actual, expected)
        
    def test_caesar_cipher_encryptor_2(self):
        string = 'abc'
        key = 0
        actual = caesar_cipher_encryptor.caesarCipherEncryptor(string, key)
        expected = 'abc'
        self.assertEqual(actual, expected)
        
    def test_caesar_cipher_encryptor_3(self):
        string = 'abc'
        key = 3
        actual = caesar_cipher_encryptor.caesarCipherEncryptor(string, key)
        expected = 'def'
        self.assertEqual(actual, expected)
        
    def test_caesar_cipher_encryptor_4(self):
        string = 'xyz'
        key = 5
        actual = caesar_cipher_encryptor.caesarCipherEncryptor(string, key)
        expected = 'cde'
        self.assertEqual(actual, expected)

    def test_caesar_cipher_encryptor_5(self):
        string = 'abc'
        key = 26
        actual = caesar_cipher_encryptor.caesarCipherEncryptor(string, key)
        expected = 'abc'
        self.assertEqual(actual, expected)

    def test_caesar_cipher_encryptor_6(self):
        string = 'abc'
        key = 52
        actual = caesar_cipher_encryptor.caesarCipherEncryptor(string, key)
        expected = 'abc'
        self.assertEqual(actual, expected)

    def test_caesar_cipher_encryptor_7(self):
        string = 'abc'
        key = 57
        actual = caesar_cipher_encryptor.caesarCipherEncryptor(string, key)
        expected = 'fgh'
        self.assertEqual(actual, expected)
    
    def test_caesar_cipher_encryptor_8(self):
        string = 'iwufqnkqkqoolxzzlzihqfm'
        key = 25
        actual = caesar_cipher_encryptor.caesarCipherEncryptor(string, key)
        expected = 'hvtepmjpjpnnkwyykyhgpel'
        self.assertEqual(actual, expected)
