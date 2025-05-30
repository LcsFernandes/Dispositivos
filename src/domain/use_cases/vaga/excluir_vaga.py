from abc import ABC, abstractmethod

class ExcluirVaga(ABC):

    @abstractmethod
    def excluir_vaga(self, id_vaga: int) -> None:
        pass