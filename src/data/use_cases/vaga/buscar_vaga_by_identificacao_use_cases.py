from src.domain.use_cases.vaga.buscar_vaga_by_id import BuscarVagaById as BuscarVagaByIdInterface
from src.infra.database.repositories.vaga_repository import VagaRepository
from src.domain.entities.vaga import Vaga
from typing import Dict

class BuscarVagaById(BuscarVagaByIdInterface):

    def __init__(self, vaga_repository: VagaRepository):
        self.__vaga_repository = vaga_repository

    def buscar_vaga_by_id(self, id: int):
        self.__valida_id(id)

        vaga = self.__vaga_repository.get_vaga_by_id(id)

        if vaga:
            response = self.__formatar_resposta(vaga)
            return response

    @classmethod
    def __valida_id(cls, id: int) -> None:
        if not id:
            raise Exception("id da vaga é um campo obrigatorio")
        
        if not isinstance(id, int) or id < 0:
            raise Exception("o id é um campo obrigatorio inteiro positivo")
        
    
    @classmethod
    def __formatar_resposta(cls, vaga: Vaga) -> Dict:
        return {
            "type": "Vaga",
            "data": {
                    "id": vaga.id,
                    "deposito_id": vaga.deposito_id,
                    "identificacao": vaga.identificacao
                }
        }