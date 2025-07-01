from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.data.dto.dispositivo.buscar_dispositivo_dto import BuscarDispositivoDTO
from src.domain.use_cases.dispositivo.buscar_posicao_dispositivo import BuscarPosicaoDispositivo as BuscarPosicaoDispositivoInterface
from src.errors.types import HttpBadRequestError, HttpNotFoundError
from typing import Dict


class BuscarPosicaoDispositivo(BuscarPosicaoDispositivoInterface):

    def __init__(self, dispositivo_repository: DispositivoRepositoryInterface):
        self.__dispositivo_repository = dispositivo_repository
        
    def buscar_posicao_dispositivo(self, dto: BuscarDispositivoDTO) -> Dict:
        self.__valida_codigo_dispositivo(dto.codigo)

        dispositivo = self.__dispositivo_repository.get_dispositivo_by_codigo(dto.codigo)

        if not dispositivo:
            raise HttpNotFoundError(f"Dispositivo com codigo {dto.codigo} nao encontrado.")

        posicao_dispositivo = self.__dispositivo_repository.buscar_posicao_dispositivo(dto.codigo)

        if not posicao_dispositivo:
            raise HttpNotFoundError(f"Dispositivo com codigo {dto.codigo} nao movimentado em nenhuma vaga.")

        return self.__formatar_resposta(posicao_dispositivo.dispositivo, posicao_dispositivo.vaga)

    @staticmethod
    def __valida_codigo_dispositivo(codigo: str) -> None:
        if not isinstance(codigo, str) or not codigo.strip():
            raise HttpBadRequestError("Codigo do dispositivo e obrigatorio e deve ser uma string valida.")

    @staticmethod
    def __formatar_resposta(dispositivo: str, vaga: str) -> Dict:
        return {
            "type": "Dispositivos",
            "data": {
                "dispositivo": dispositivo,
                "vaga": vaga
            }
        }

        