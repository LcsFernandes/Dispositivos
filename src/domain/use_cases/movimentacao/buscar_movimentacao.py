from abc import ABC, abstractmethod
from src.domain.entities.movimentacao import Movimentacao
from typing import List

class BuscarMovimentacao(ABC):

    @abstractmethod
    def buscar_movimentacao(self, id_dispositivo: int) -> List[Movimentacao]:
        pass
