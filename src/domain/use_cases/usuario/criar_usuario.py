from abc import ABC, abstractmethod

class CriarUsuario(ABC):
    
    @abstractmethod
    def criar_usuario(self, re: str, senha: str):
        pass