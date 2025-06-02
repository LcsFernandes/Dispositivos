from abc import ABC, abstractmethod
from src.domain.entities.movimentacao import Movimentacao
from typing import List
from datetime import datetime


class MovimentacaoRepository(ABC):

    @abstractmethod
    def get_movimentacao(self, id: int) -> Movimentacao:
        pass

    @abstractmethod
    def get_movimentacao_por_dispositivo(self, id_dispositivo: int) -> List[Movimentacao]:
        pass

    @abstractmethod
    def get_all_movimentacoes(self) -> List[Movimentacao]:
        pass

    @abstractmethod
    def registrar_movimentacao(self, id_dispositivo: int, local_origem: int, local_destino: int, data_movimentacao: datetime, usuario_id: int, tipo: int) -> None:
        pass