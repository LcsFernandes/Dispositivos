from abc import ABC, abstractmethod
from src.domain.entities.dispositivo import Dispositivo
from datetime import datetime
from typing import List

class DispositivoRepositoryInterface(ABC):

    @abstractmethod
    def get_dispositivo(self, codigo: str) -> Dispositivo:
        pass

    @abstractmethod
    def get_all_dispositivos(self) -> List[Dispositivo]:
        pass

    @abstractmethod
    def adicionar_dispositivo(self, codigo: str, tipo: int, descricao: str, vaga: str, status: int, data_fabricacao: datetime) -> None:
        pass

    @abstractmethod
    def atualizar_dispositivo(self, codigo: str, tipo: int, descricao: str, vaga: str, status: int, data_fabricacao: datetime) -> None:
        pass

    @abstractmethod
    def excluir_dispositivo(self, codigo: str) -> None:
        pass

    @abstractmethod
    def verificar_status_dispositivo(self, codigo: str) -> bool:
        pass