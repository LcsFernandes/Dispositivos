from abc import ABC, abstractmethod
from src.domain.entities.vaga import Vaga

class BuscarVaga(ABC):

    @abstractmethod
    def buscar_vaga(self, id_vaga: int) -> Vaga:
        pass