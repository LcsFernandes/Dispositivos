from abc import ABC, abstractmethod


class ExcluirDispositivo(ABC):

    @abstractmethod
    def excluir_dispositivo(self, codigo: str) -> None:
        pass