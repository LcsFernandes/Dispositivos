from abc import ABC, abstractmethod
from typing import Dict

class BuscarPosicaoDispositivo(ABC):

    @abstractmethod
    def buscar_posicao_dispositivo(self, codigo: str) -> Dict:
        pass