from abc import ABC, abstractmethod

class SenhaServiceInterface(ABC):

    @abstractmethod
    def hash_senha(self, senha: str) -> str:
        pass
    
    @abstractmethod
    def verificar_senha(self, senha: str, hash_armazenado: str) -> bool:
        pass