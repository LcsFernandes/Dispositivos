from abc import ABC, abstractmethod
from src.domain.entities.dispositivo import Dispositivo
from typing import List

class ListarDispositivos:

    @abstractmethod
    def listar_dispositivos(self, page: int, page_size: int) -> List[Dispositivo]:
        pass