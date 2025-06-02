from abc import ABC, abstractmethod
from src.domain.entities.movimentacao import Movimentacao
from typing import List

class BuscarMovimentacao(ABC):

    @abstractmethod
    def buscar_movimentacao(self, id: int) -> Movimentacao:
        pass

    @abstractmethod
    def buscar_movimentacao_por_dispositivo(self, id_dispositivo: int) -> List[Movimentacao]:
        pass
