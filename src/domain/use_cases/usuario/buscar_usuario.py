from abc import ABC, abstractmethod

class BuscarUsuario(ABC):
    
    @abstractmethod
    def buscar_usuario(self, re: str):
        pass