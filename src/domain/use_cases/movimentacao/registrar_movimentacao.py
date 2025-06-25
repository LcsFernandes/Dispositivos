from abc import ABC, abstractmethod
from datetime import datetime

class RegistrarMovimentacao(ABC):

    @abstractmethod
    def registrar_movimentacao(self, codigo: str, local_origem: str, local_destino: str, data_movimentacao: datetime, login_id: int) -> None:
        pass
