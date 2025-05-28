from abc import ABC, abstractmethod
from src.domain.entities.Dispositivo import Dispositivo


class BuscarDispositivos(ABC):
    
    @abstractmethod
    def buscar_dispositivo(codigo: str) -> Dispositivo:
        pass