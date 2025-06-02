from abc import ABC, abstractmethod
from datetime import datetime

class RegistrarMovimentacao(ABC):

    @abstractmethod
    def registrar_movimentacao(self, id_dispositivo: int, local_origem: int, local_destino: int, data_movimentacao: datetime, usuario_id: int, tipo: int) -> None:
        pass
