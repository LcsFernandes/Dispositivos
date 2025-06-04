from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.domain.entities.dispositivo import Dispositivo
from src.domain.use_cases.dispositivo.excluir_dispositivo import ExcluirDispositivo as ExcluirDispositivoInterface
from typing import Dict, List

class ExcluirDispositivo(ExcluirDispositivoInterface):
   
    def __init__ (self, dispositivo_repository: DispositivoRepositoryInterface):
        self.__dispositivo_repository = dispositivo_repository

    def excluir_dispositivo(self, codigo: str) -> None:
        
        dispositivo = self.__dispositivo_repository.get_dispositivo(codigo)
        
        if not dispositivo:
            raise Exception(f"Dispositivo {codigo} nao encontrado")
        
        self.__dispositivo_repository.excluir_dispositivo(codigo)
        
            