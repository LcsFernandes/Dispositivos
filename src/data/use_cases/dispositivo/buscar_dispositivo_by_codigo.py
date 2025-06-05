from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.domain.entities.dispositivo import Dispositivo
from src.domain.use_cases.dispositivo.buscar_dispositivo_by_codigo import BuscarDispositivosByCodigo as BuscarDispositivosByCodigoInterface
from typing import Dict


class BuscarDispositivoByCodigo(BuscarDispositivosByCodigoInterface):

    def __init__(self, dispositivo_repository: DispositivoRepositoryInterface):
        self.__dispositivo_repository = dispositivo_repository
        
    def buscar_dispositivo_by_codigo(self, codigo: str) -> Dispositivo:
        self.__valida_codigo_dispositivo(codigo)
        
        dispositivo = self.__dispositivo_repository.get_dispositivo_by_codigo(codigo)
        if not dispositivo:
            raise Exception(f"Dispositivo com código {codigo} não encontrado.")
        
        response = self.__formatar_resposta(dispositivo)
        
        return response
    
    
    @classmethod
    def __valida_codigo_dispositivo(cls, codigo: str) -> None:
        if not codigo:
            raise Exception("codigo do dispositivo é obrigatorio")
        
        
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

        