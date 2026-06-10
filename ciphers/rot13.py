from .base import BaseCipher


class ROT13Cipher(BaseCipher):
    def encrypt(self, text: str) -> str:
        result = []
        for char in text:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                result.append(chr((ord(char) - base + 13) % 26 + base))
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, text: str) -> str:
        return self.encrypt(text)

    @property
    def name(self) -> str:
        return "ROT13 Cipher"
