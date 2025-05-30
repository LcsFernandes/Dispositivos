from abc import ABC, abstractmethod

class AlterarVaga(ABC):

    @abstractmethod
    def alterar_vaga(self, id_vaga: int, identificacao: str) -> None:
        pass