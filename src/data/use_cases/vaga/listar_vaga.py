from src.domain.use_cases.vaga.listar_vagas import ListarVagas as ListarVagasInterface
from src.data.interfaces.vaga_repository import VagaRepositoryInterface
from src.domain.entities.vaga import Vaga
from typing import Dict

class ListarVaga(ListarVagasInterface):

    def __init__(self, vaga_repository: VagaRepositoryInterface):
        self.__vaga_repository = vaga_repository

    def listar_vagas(self):
        vagas = self.__vaga_repository.listar_vagas()

        if vagas:
            response = self.__formatar_resposta(vagas)
            return response
        
        return None


    @staticmethod
    def __formatar_resposta(vagas: Vaga) -> Dict:
        lista_vagas = []
        for vaga in vagas:
            lista_vagas.append({
                    "id": vaga.id,
                    "deposito_id": vaga.deposito_id,
                    "identificacao": vaga.identificacao
                    
                })
             
        return {
            "type": "Vaga",
            "data": lista_vagas
        }
    