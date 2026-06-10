from .base import BaseCipher


class CaesarCipher(BaseCipher):
    def __init__(self, shift: int = 3):
        self.shift = shift

    def encrypt(self, text: str) -> str:
        result = []
        for char in text:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                result.append(chr((ord(char) - base + self.shift) % 26 + base))
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, text: str) -> str:
        result = []
        for char in text:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                result.append(chr((ord(char) - base - self.shift) % 26 + base))
            else:
                result.append(char)
        return "".join(result)

    @property
    def name(self) -> str:
        return f"Caesar Cipher (shift={self.shift})"
