from abc import ABC, abstractmethod
from src.domain.entities.Dispositivo import Dispositivo
import datetime

class InserirDispositivos(ABC):
    
    @abstractmethod
    def inserir_dispositivo(codigo: str, tipo: int, descricao: str, vaga: str, status: int, data_fabricacao: datetime, cliente: str) -> any:
        pass