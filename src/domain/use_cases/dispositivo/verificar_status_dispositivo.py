from abc import ABC, abstractmethod

class VerificarStatusDispositivo(ABC):

    @abstractmethod
    def verificar_status_dispositivo(self, codigo: str) -> bool:
        pass