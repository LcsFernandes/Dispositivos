from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.data.dto.dispositivo.buscar_dispositivo_dto import BuscarDispositivoDTO
from src.domain.entities.dispositivo import Dispositivo
from src.domain.use_cases.dispositivo.buscar_dispositivo_by_codigo import BuscarDispositivosByCodigo as BuscarDispositivosByCodigoInterface
from src.errors.types import HttpBadRequestError, HttpNotFoundError
from typing import Dict


class BuscarDispositivoByCodigo(BuscarDispositivosByCodigoInterface):

    def __init__(self, dispositivo_repository: DispositivoRepositoryInterface):
        self.__dispositivo_repository = dispositivo_repository
        
    def buscar_dispositivo_by_codigo(self, dto: BuscarDispositivoDTO) -> Dict:
        self.__valida_codigo_dispositivo(dto.codigo)

        dispositivo = self.__dispositivo_repository.get_dispositivo_by_codigo(dto.codigo)
        if not dispositivo:
            raise HttpNotFoundError(f"Dispositivo com codigo {dto.codigo} nao encontrado.")

        return self.__formatar_resposta(dispositivo)

    @staticmethod
    def __valida_codigo_dispositivo(codigo: str) -> None:
        if not isinstance(codigo, str) or not codigo.strip():
            raise HttpBadRequestError("Codigo do dispositivo e obrigatorio e deve ser uma string valida.")

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

        