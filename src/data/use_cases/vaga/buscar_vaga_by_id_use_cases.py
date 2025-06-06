from src.domain.use_cases.vaga.buscar_vaga_by_identificacao import BuscarVagaByIdentificacao as BuscarVagaByIdentificacaoInterface
from src.data.interfaces.vaga_repository import VagaRepositoryInterface
from src.domain.entities.vaga import Vaga
from typing import Dict

class BuscarVagaByIdentificacao(BuscarVagaByIdentificacaoInterface):

    def __init__(self, vaga_repository: VagaRepositoryInterface):
        self.__vaga_repository = vaga_repository

    def buscar_vaga_by_identififcacao(self, identificacao: str):
        self.__valida_identificacao(identificacao)

        vaga = self.__vaga_repository.get_vaga_by_identificacao(identificacao)

        if vaga:
            response = self.__formatar_resposta(vaga)
            return response

    @classmethod
    def __valida_identificacao(cls, identificacao: str) -> None:
        if not identificacao:
            raise Exception("identificacao da vaga é um campo obrigatorio")
        
        if len(identificacao) < 3:
            raise Exception("Identificacao incorreta")
        
    
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