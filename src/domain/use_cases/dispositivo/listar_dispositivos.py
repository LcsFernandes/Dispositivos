from abc import ABC, abstractmethod
from src.domain.entities.dispositivo import Dispositivo
from typing import List

class ListarDispositivo:

    @abstractmethod
    def listar_dispositivo(self) -> List[Dispositivo]:
        pass