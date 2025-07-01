from abc import ABC, abstractmethod
from src.domain.entities.movimentacao import Movimentacao
from typing import List
from datetime import datetime


class MovimentacaoRepositoryInterface(ABC):

    @abstractmethod
    def get_movimentacao_por_dispositivo(self, codigo: int) -> List[Movimentacao]:
        pass

    @abstractmethod
    def get_all_movimentacoes(self, page: int, page_size: int) -> List[Movimentacao]:
        pass

    @abstractmethod
    def registrar_movimentacao(self, codigo: str, local_origem: str, local_destino: str, data_movimentacao: datetime, user_id: int) -> None:
        pass