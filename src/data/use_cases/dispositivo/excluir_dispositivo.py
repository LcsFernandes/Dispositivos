from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.data.dto.dispositivo.excluir_dispositivo_dto import ExcluirDispositivoDTO
from src.domain.entities.dispositivo import Dispositivo
from src.domain.use_cases.dispositivo.excluir_dispositivo import ExcluirDispositivo as ExcluirDispositivoInterface
from src.errors.types import HttpBadRequestError
from typing import Dict, List

class ExcluirDispositivo(ExcluirDispositivoInterface):
   
    def __init__ (self, dispositivo_repository: DispositivoRepositoryInterface):
        self.__dispositivo_repository = dispositivo_repository

    def excluir_dispositivo(self, dto: ExcluirDispositivoDTO) -> None:
        
        self.__valida_codigo_dispositivo(dto.codigo)

        dispositivo = self.__dispositivo_repository.get_dispositivo(dto.codigo)
        
        if not dispositivo:
            raise HttpBadRequestError(f"Dispositivo {dto.codigo} nao encontrado")
        
        self.__dispositivo_repository.excluir_dispositivo(dto.codigo)
    
    @staticmethod
    def __valida_codigo_dispositivo(codigo: str) -> None:
        if not codigo:
            raise HttpBadRequestError("codigo do dispositivo é obrigatorio")
            