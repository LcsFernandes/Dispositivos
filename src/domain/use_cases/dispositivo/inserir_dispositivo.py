from abc import ABC, abstractmethod
from src.domain.entities.dispositivo import Dispositivo
from datetime import datetime

class InserirDispositivos(ABC):
    
    @abstractmethod
    def inserir_dispositivo(self, codigo: str, tipo: int, descricao: str, vaga: str, status: int, data_fabricacao: datetime, cliente: str) -> any:
        pass