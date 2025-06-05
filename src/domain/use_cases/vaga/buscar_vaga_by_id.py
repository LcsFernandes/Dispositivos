from abc import ABC, abstractmethod
from src.domain.entities.vaga import Vaga

class BuscarVagaById(ABC):

    @abstractmethod
    def buscar_vaga_by_id(self, id: int) -> Vaga:
        pass