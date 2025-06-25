from abc import ABC, abstractmethod

class UsuarioRepositoryInterface(ABC):

    @abstractmethod
    def login_usuario(self, re: str, senha: str):
        pass