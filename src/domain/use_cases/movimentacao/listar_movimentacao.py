from abc import ABC, abstractmethod
from src.domain.entities.movimentacao import Movimentacao
from typing import List


class ListarMovimentacao(ABC):
    @abstractmethod
    def listar_movimentacao(self) -> List[Movimentacao]:
        pass