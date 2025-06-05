from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.domain.entities.dispositivo import Dispositivo
from src.domain.use_cases.dispositivo.buscar_dispositivo_by_id import BuscarDispositivosById as BuscarDispositivosByIdInterface
from typing import Dict


class BuscarDispositivoById(BuscarDispositivosByIdInterface):

    def __init__(self, dispositivo_repository: DispositivoRepositoryInterface):
        self.__dispositivo_repository = dispositivo_repository
        
    def buscar_dispositivo_by_id(self, id: int) -> Dispositivo:
        self.__valida_id_dispositivo(id)
        
        dispositivo = self.__dispositivo_repository.get_dispositivo_by_id(id)
        if not dispositivo:
            raise Exception(f"Dispositivo com id {id} não encontrado.")
        
        response = self.__formatar_resposta(dispositivo)
        
        return response
    
    
    @classmethod
    def __valida_id_dispositivo(cls, id: int) -> None:
        if not id or id < 0:
            raise Exception("id do dispositivo é um parametro obrigatório inteiro positivo")
        
        
    @classmethod
    def __formatar_resposta(cls, dispositivo: Dispositivo) -> Dict:
        return {
            "type": "Dispositivos",
            "data": {
                    "id": dispositivo.id,
                    "codigo": dispositivo.codigo,
                    "tipo": dispositivo.tipo,
                    "descricao": dispositivo.descricao,
                    "vaga": dispositivo.vaga,
                    "status": dispositivo.status,
                    "data_fabricacao": dispositivo.data_fabricacao
                }
        }

        