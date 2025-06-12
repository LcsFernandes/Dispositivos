from src.domain.use_cases.movimentacao.buscar_movimentacao import BuscarMovimentacao as BuscarMovimentacaoInterface
from src.data.interfaces.movimentacao_repository import MovimentacaoRepositoryInterface
from src.data.dto.movimentacao.buscar_movimentacao_dto import BuscarMovimentacaoDTO
from src.domain.entities.movimentacao import Movimentacao
from typing import Dict

class MovimentacaoRepository(BuscarMovimentacaoInterface):
    
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
            raise Exception("id da movimentacao é um campo obrigatorio")
        
        if not isinstance(id_dispositivo, int) or id_dispositivo < 0:
            raise Exception("o id é um campo obrigatorio inteiro positivo")


    @staticmethod
    def __formatar_resposta(movimentacao: Movimentacao) -> Dict:
        return {
            "type": "Movimentacao",
            "data": {
                    "id": movimentacao.id,
                    "id_dispositivo": movimentacao.id_dispositivo,
                    "local_origem": movimentacao.local_origem,
                    "local_destino": movimentacao.local_destino,
                    "data_movimentacao": movimentacao.data_movimentacao,
                    "usuario_id": movimentacao.usuario_id,
                    "tipo": movimentacao.tipo
                }
        }