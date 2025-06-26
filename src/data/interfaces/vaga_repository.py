from abc import ABC, abstractmethod
from src.domain.entities.vaga import Vaga
from typing import List

class VagaRepositoryInterface(ABC):

    @abstractmethod
    def get_vaga_by_identificacao(self, identificacao: str) -> Vaga:
        pass

    @abstractmethod
    def get_vaga_by_id(self, id: int) -> Vaga:
        pass

    @abstractmethod
    def listar_vagas(self) -> List[Vaga]:
        pass
    
    @abstractmethod
    def inserir_vaga(self, identificacao: str) -> None:
        pass

    @abstractmethod
    def atualizar_vaga(self, id: int, identificacao: str) -> None:
        pass
