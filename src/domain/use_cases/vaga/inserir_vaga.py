from abc import ABC, abstractmethod

class InserirVaga(ABC):

    @abstractmethod
    def inserir_vaga(self, idenfificacao: int) -> None:
        pass