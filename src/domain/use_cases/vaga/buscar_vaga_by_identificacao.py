from abc import ABC, abstractmethod
from src.domain.entities.vaga import Vaga

class BuscarVagaByIdentificacao(ABC):

    @abstractmethod
    def buscar_vaga_by_identificacao(self, identificacao: str) -> Vaga:
        pass