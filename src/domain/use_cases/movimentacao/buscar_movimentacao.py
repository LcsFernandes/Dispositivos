from abc import ABC, abstractmethod

class BuscarMovimentacao(ABC):

    @abstractmethod
    def buscar_movimentacao(self, id_movimentacao: int) -> dict:
        pass