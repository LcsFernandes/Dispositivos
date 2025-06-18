from abc import ABC, abstractmethod
from src.domain.entities.dispositivo import Dispositivo
from datetime import datetime
from typing import List, Dict

class DispositivoRepositoryInterface(ABC):

    @abstractmethod
    def get_dispositivo_by_codigo(self, codigo: str) -> Dispositivo:
        pass

    @abstractmethod
    def get_dispositivo_by_id(self, id: int) -> Dispositivo:
        pass

    @abstractmethod
    def get_all_dispositivos(self) -> List[Dispositivo]:
        pass

    @abstractmethod
    def adicionar_dispositivo(self, codigo: str, tipo: int, descricao: str, status: int, data_fabricacao: datetime, cliente: str) -> None:
        pass

    @abstractmethod
    def atualizar_dispositivo(self, codigo: str, tipo: int, descricao: str, status: int, data_fabricacao: datetime, cliente: str) -> None:
        pass

    @abstractmethod
    def excluir_dispositivo(self, codigo: str) -> None:
        pass

    @abstractmethod
    def verificar_status_dispositivo(self, codigo: str) -> bool:
        pass

    @abstractmethod
    def buscar_posicao_dispositivo(self, codigo: str) -> Dict:
        pass