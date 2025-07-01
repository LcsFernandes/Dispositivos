from abc import ABC, abstractmethod

class AlterarSenhaUsuario(ABC):
    
    @abstractmethod
    def alterar_senha_usuario(self, re: str, senha: str):
        pass