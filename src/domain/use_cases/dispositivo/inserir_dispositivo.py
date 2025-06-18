from abc import ABC, abstractmethod
from src.domain.entities.dispositivo import Dispositivo
from datetime import datetime

class InserirDispositivo(ABC):
    
    @abstractmethod
    def inserir_dispositivo(self, codigo: str, tipo: int, descricao: str, status: int, data_fabricacao: datetime, cliente: str) -> None:
        pass