from abc import ABC, abstractmethod

class LoginUsuario(ABC):

    @abstractmethod
    def login_usuario(self, re: str, senha: str):
        pass