from abc import ABC, abstractmethod
from src.domain.entities.dispositivo import Dispositivo
from datetime import datetime

class AlterarDispositivo(ABC):

    @abstractmethod
    def alterar_dispositivo(id: int, codigo: str, tipo: int, descricao: str, vaga: str, status: int, data_fabricacao: datetime) -> None:
        pass