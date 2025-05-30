from abc import ABC, abstractmethod
from src.domain.entities.vaga import Vaga

class InserirVaga(ABC):

    @abstractmethod
    def inserir_vaga(self, deposito_id: int, idenfificacao: int) -> None:
        pass