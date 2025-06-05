from abc import ABC, abstractmethod
from src.domain.entities.dispositivo import Dispositivo


class BuscarDispositivosById(ABC):
    
    @abstractmethod
    def buscar_dispositivo_by_id(self, id: int) -> Dispositivo:
        pass