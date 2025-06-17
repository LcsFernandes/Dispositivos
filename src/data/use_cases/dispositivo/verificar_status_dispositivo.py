from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.data.dto.dispositivo.verificar_status_dispositivos_dto import VerificarStatusDispositivoDTO
from src.domain.use_cases.dispositivo.verificar_status_dispositivo import VerificarStatusDispositivo as VerificarStatusDispositivoInterface
from src.errors.types import HttpBadRequestError, HttpNotFoundError
from typing import Dict

class VerificarStatusDispositivo(VerificarStatusDispositivoInterface):

    def __init__(self, dispositivo_repository: DispositivoRepositoryInterface):
        self.__dispositivo_repository = dispositivo_repository

    def verificar_status_dispositivo(self, dto: VerificarStatusDispositivoDTO):
        self.__valida_codigo_dispositivo(dto.codigo)

        dispositivo = self.__dispositivo_repository.get_dispositivo_by_codigo(dto.codigo)

        if not dispositivo:
            raise HttpNotFoundError("Dispositivo nao encontrado")
        
        status_dispositivo = self.__dispositivo_repository.verificar_status_dispositivo(dto.codigo)
        
        if status_dispositivo is not None:
            
            response = self.__formatar_resposta(dto.codigo, status_dispositivo[0])
            return response

    @staticmethod
    def __valida_codigo_dispositivo(codigo: str):
        if not codigo or not isinstance(codigo, str):
            raise HttpBadRequestError("codigo do dispositivo é um campo tipo string obrigatorio")
    
    @staticmethod
    def __formatar_resposta(codigo: str, status: bool) -> Dict:
        return {
            "type": "Dispositivo",
            "data": {
                    "codigo": codigo,
                    "status": status
                }
        }
        

        