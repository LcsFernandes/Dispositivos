from src.data.interfaces.movimentacao_repository import MovimentacaoRepositoryInterface
from src.domain.use_cases.movimentacao.listar_movimentacao import ListarMovimentacao as ListarMovimentacaoInterface
from src.domain.entities.movimentacao import Movimentacao
from typing import List, Dict

class ListarMovimentacao(ListarMovimentacaoInterface):

    def __init__(self, movimentacao_repository: MovimentacaoRepositoryInterface):
        self.__movimentacao_repository = movimentacao_repository

    def listar_movimentacao(self) -> List[Movimentacao]:
        movimentacoes = self.__movimentacao_repository.get_all_movimentacoes()

        if movimentacoes:
            response = self.__formatar_resposta(movimentacoes)
            return response
        
        return None
   
    @staticmethod
    def __formatar_resposta(movimentacoes: Movimentacao) -> Dict:
        lista_movimentacoes = []
        for movimentacao in movimentacoes:
            lista_movimentacoes.append({
                    "id": movimentacao.id,
                    "id_dispositivo": movimentacao.id_dispositivo,
                    "local_origem": movimentacao.local_origem,
                    "local_destino": movimentacao.local_destino,
                    "data_movimentacao": movimentacao.data_movimentacao.strftime('%Y-%m-%d %H:%M:%S'),
                    "login_id": movimentacao.login_id
                })
             
        return {
            "type": "Movimentacao",
            "data": lista_movimentacoes
        }