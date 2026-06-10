from .base import BaseCipher


class VigenereCipher(BaseCipher):
    def __init__(self, key: str):
        if not key or not key.isalpha():
            raise ValueError("Key must be non-empty and contain only letters")
        self.key = key.lower()

    def _extend_key(self, length: int) -> str:
        repeats = (length // len(self.key)) + 1
        return (self.key * repeats)[:length]

    def _transform(self, text: str, direction: int) -> str:
        result = []
        key_stream = self._extend_key(
            sum(1 for c in text if c.isalpha())
        )
        key_idx = 0
        for char in text:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                shift = ord(key_stream[key_idx]) - ord("a")
                result.append(chr((ord(char) - base + direction * shift) % 26 + base))
                key_idx += 1
            else:
                result.append(char)
        return "".join(result)

    def encrypt(self, text: str) -> str:
        return self._transform(text, 1)

    def decrypt(self, text: str) -> str:
        return self._transform(text, -1)

    @property
    def name(self) -> str:
        return f"Vigenère Cipher (key={self.key})"
