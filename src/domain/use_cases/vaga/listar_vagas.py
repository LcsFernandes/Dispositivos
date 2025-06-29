from abc import ABC, abstractmethod
from src.domain.entities.vaga import Vaga
from typing import List


class ListarVagas(ABC):

    @abstractmethod
    def listar_vagas(self) -> List[Vaga]:
        pass