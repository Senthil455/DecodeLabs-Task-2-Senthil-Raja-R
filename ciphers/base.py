from abc import ABC, abstractmethod


class BaseCipher(ABC):
    @abstractmethod
    def encrypt(self, text: str) -> str:
        ...

    @abstractmethod
    def decrypt(self, text: str) -> str:
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        ...
