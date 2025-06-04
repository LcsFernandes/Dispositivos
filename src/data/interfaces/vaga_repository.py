from abc import ABC, abstractmethod
from src.domain.entities.vaga import Vaga
from typing import List

class VagaRepositoryInterface(ABC):

    @abstractmethod
    def get_vaga(self, identificacao: str) -> Vaga:
        pass

    @abstractmethod
    def listar_vagas(self) -> List[Vaga]:
        pass
    
    @abstractmethod
    def inserir_vaga(self, deposito_id: int, identificacao: str) -> None:
        pass

    @abstractmethod
    def atualizar_vaga(self, id: int, deposito_id: int, identificacao: str) -> None:
        pass
