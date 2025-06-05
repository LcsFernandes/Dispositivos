from abc import ABC, abstractmethod
from src.domain.entities.dispositivo import Dispositivo


class BuscarDispositivosByCodigo(ABC):
    
    @abstractmethod
    def buscar_dispositivo_by_codigo(self, codigo: str) -> Dispositivo:
        pass