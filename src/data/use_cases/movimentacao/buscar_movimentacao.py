from src.domain.use_cases.movimentacao.buscar_movimentacao import BuscarMovimentacao as BuscarMovimentacaoInterface
from src.data.interfaces.movimentacao_repository import MovimentacaoRepositoryInterface
from src.data.dto.movimentacao.buscar_movimentacao_dto import BuscarMovimentacaoDTO
from src.domain.entities.movimentacao import Movimentacao
from src.errors.types import HttpBadRequestError
from typing import Dict

class BuscarMovimentacao(BuscarMovimentacaoInterface):
    
    def __init__(self, movimentacao_repository: MovimentacaoRepositoryInterface):
        self.__movimentacao_repository = movimentacao_repository

    def buscar_movimentacao(self, dto: BuscarMovimentacaoDTO):
        self.__valida_id(dto.id_dispositivo)

        movimentacao = self.__movimentacao_repository.get_movimentacao_por_dispositivo(dto.id_dispositivo)

        if movimentacao:
            response = self.__formatar_resposta(movimentacao)
            return response
        
        return None

    @staticmethod
    def __valida_id(id_dispositivo: int) -> None:
        if not id_dispositivo:
            raise HttpBadRequestError("id da movimentacao e um campo obrigatorio")
        
        if not isinstance(id_dispositivo, int) or id_dispositivo < 0:
            raise HttpBadRequestError("o id e um campo obrigatorio inteiro positivo")


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