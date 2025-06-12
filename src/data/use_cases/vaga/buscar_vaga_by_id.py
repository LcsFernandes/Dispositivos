from src.domain.use_cases.vaga.buscar_vaga_by_id import BuscarVagaById as BuscarVagaByIdInterface
from src.data.dto.vaga.buscar_vaga_by_id_dto import BuscarVagaByIdDTO
from src.data.interfaces.vaga_repository import VagaRepositoryInterface
from src.errors.types import HttpBadRequestError
from src.domain.entities.vaga import Vaga
from typing import Dict

class BuscarVagaById(BuscarVagaByIdInterface):

    def __init__(self, vaga_repository: VagaRepositoryInterface):
        self.__vaga_repository = vaga_repository

    def buscar_vaga_by_id(self, dto: BuscarVagaByIdDTO):
        self.__valida_id(dto.id)

        vaga = self.__vaga_repository.get_vaga_by_id(dto.id)

        if vaga:
            response = self.__formatar_resposta(vaga)
            return response
        
        return None

    @staticmethod
    def __valida_id(id: int) -> None:
        if not id:
            raise HttpBadRequestError("id da vaga é um campo obrigatorio")
        
        if not isinstance(id, int) or id < 0:
            raise HttpBadRequestError("o id é um campo obrigatorio inteiro positivo")
        
    
    @staticmethod
    def __formatar_resposta(vaga: Vaga) -> Dict:
        return {
            "type": "Vaga",
            "data": {
                    "id": vaga.id,
                    "deposito_id": vaga.deposito_id,
                    "identificacao": vaga.identificacao
                }
        }