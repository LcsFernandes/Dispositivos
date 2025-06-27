from abc import ABC, abstractmethod

class UsuarioRepositoryInterface(ABC):

    @abstractmethod
    def criar_usuario(self, re: str, nome: str, senha: str):
        pass

    @abstractmethod
    def get_usuario(self, re: str):
        pass