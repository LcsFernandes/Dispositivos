from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.data.dto.dispositivo.buscar_dispositivo_dto import BuscarDispositivoDTO
from src.domain.entities.dispositivo import Dispositivo
from src.domain.use_cases.dispositivo.buscar_dispositivo_by_id import BuscarDispositivosById as BuscarDispositivosByIdInterface
from src.errors.types import HttpBadRequestError, HttpNotFoundError
from typing import Dict


class BuscarDispositivoById(BuscarDispositivosByIdInterface):

    def __init__(self, dispositivo_repository: DispositivoRepositoryInterface):
        self.__dispositivo_repository = dispositivo_repository
        
    def buscar_dispositivo_by_id(self, dto: BuscarDispositivoDTO) -> Dispositivo:
        self.__valida_id_dispositivo(dto.id)
        
        dispositivo = self.__dispositivo_repository.get_dispositivo_by_id(dto.id)
        if not dispositivo:
            raise HttpNotFoundError(f"Dispositivo com id {dto.id} nao encontrado.")
        
        response = self.__formatar_resposta(dispositivo)
        
        return response
    
    
    @staticmethod
    def __valida_id_dispositivo(id: int) -> None:
        if not id or id < 0:
            raise HttpBadRequestError("id do dispositivo e um parametro obrigatorio inteiro positivo")
        
        
    @staticmethod
    def __formatar_resposta(dispositivo: Dispositivo) -> Dict:
        return {
            "type": "Dispositivos",
            "data": {
                    "id": dispositivo.id,
                    "codigo": dispositivo.codigo,
                    "tipo": dispositivo.tipo,
                    "descricao": dispositivo.descricao,
                    "status": dispositivo.status,
                    "data_fabricacao": dispositivo.data_fabricacao.strftime('%Y-%m-%d'),
                    "cliente": dispositivo.cliente
                }
        }

        