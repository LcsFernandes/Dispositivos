from abc import ABC, abstractmethod

class VerificarStatusDispositivo(ABC):

    @abstractmethod
    def verificar_status_dispositivo(self, id_dispositivo: int) -> bool:
        pass