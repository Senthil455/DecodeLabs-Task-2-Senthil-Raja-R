import unittest
from ciphers import CaesarCipher, VigenereCipher, ROT13Cipher


class TestCaesarCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = CaesarCipher(shift=3)

    def test_encrypt_basic(self):
        self.assertEqual(self.cipher.encrypt("HELLO"), "KHOOR")

    def test_decrypt_basic(self):
        self.assertEqual(self.cipher.decrypt("KHOOR"), "HELLO")

    def test_roundtrip(self):
        plain = "CyberSecurity"
        self.assertEqual(self.cipher.decrypt(self.cipher.encrypt(plain)), plain)

    def test_preserves_non_alpha(self):
        result = self.cipher.encrypt("Hello, World!")
        self.assertIn(",", result)
        self.assertIn(" ", result)
        self.assertIn("!", result)

    def test_lowercase(self):
        self.assertEqual(self.cipher.encrypt("abc"), "def")

    def test_uppercase(self):
        self.assertEqual(self.cipher.encrypt("XYZ"), "ABC")

    def test_wraparound(self):
        cipher = CaesarCipher(shift=25)
        self.assertEqual(cipher.encrypt("B"), "A")
        self.assertEqual(cipher.decrypt("A"), "B")

    def test_empty_string(self):
        self.assertEqual(self.cipher.encrypt(""), "")
        self.assertEqual(self.cipher.decrypt(""), "")

    def test_negative_shift_encrypt(self):
        cipher = CaesarCipher(shift=-3)
        self.assertEqual(cipher.encrypt("KHOOR"), "HELLO")

    def test_negative_shift_decrypt(self):
        cipher = CaesarCipher(shift=-3)
        self.assertEqual(cipher.decrypt("HELLO"), "KHOOR")


class TestVigenereCipher(unittest.TestCase):
    def test_encrypt_basic(self):
        cipher = VigenereCipher(key="KEY")
        result = cipher.encrypt("HELLO")
        self.assertEqual(result, "RIJVS")

    def test_decrypt_basic(self):
        cipher = VigenereCipher(key="KEY")
        self.assertEqual(cipher.decrypt("RIJVS"), "HELLO")

    def test_roundtrip(self):
        cipher = VigenereCipher(key="SECRET")
        plain = "VigenereCipher"
        self.assertEqual(cipher.decrypt(cipher.encrypt(plain)), plain)

    def test_preserves_non_alpha(self):
        cipher = VigenereCipher(key="KEY")
        result = cipher.encrypt("Hello, World!")
        self.assertIn(",", result)
        self.assertIn(" ", result)
        self.assertIn("!", result)

    def test_empty_string(self):
        cipher = VigenereCipher(key="KEY")
        self.assertEqual(cipher.encrypt(""), "")
        self.assertEqual(cipher.decrypt(""), "")

    def test_case_preservation(self):
        cipher = VigenereCipher(key="Key")
        plain = "Hello"
        result = cipher.encrypt(plain)
        self.assertEqual(result[0].isupper(), plain[0].isupper())
        self.assertEqual(result[1].islower(), plain[1].islower())

    def test_invalid_key_empty(self):
        with self.assertRaises(ValueError):
            VigenereCipher(key="")

    def test_invalid_key_non_alpha(self):
        with self.assertRaises(ValueError):
            VigenereCipher(key="123")


class TestROT13Cipher(unittest.TestCase):
    def setUp(self):
        self.cipher = ROT13Cipher()

    def test_encrypt(self):
        self.assertEqual(self.cipher.encrypt("HELLO"), "URYYB")

    def test_decrypt_same_as_encrypt(self):
        self.assertEqual(self.cipher.decrypt("URYYB"), "HELLO")

    def test_roundtrip(self):
        plain = "ROT13IsFun"
        self.assertEqual(self.cipher.decrypt(self.cipher.encrypt(plain)), plain)

    def test_preserves_non_alpha(self):
        result = self.cipher.encrypt("Hello, World!")
        self.assertIn(",", result)
        self.assertIn(" ", result)
        self.assertIn("!", result)

    def test_empty_string(self):
        self.assertEqual(self.cipher.encrypt(""), "")
        self.assertEqual(self.cipher.decrypt(""), "")

    def test_double_encrypt_returns_original(self):
        plain = "TestMessage"
        self.assertEqual(self.cipher.encrypt(self.cipher.encrypt(plain)), plain)


if __name__ == "__main__":
    unittest.main()
