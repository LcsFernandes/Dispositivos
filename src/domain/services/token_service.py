from abc import ABC, abstractmethod

class TokenService(ABC):

    @abstractmethod
    def criar_token(data: dict):
        pass

    @abstractmethod
    def verificar_token(token: str):
        pass