from src.data.interfaces.movimentacao_repository import MovimentacaoRepositoryInterface
from src.domain.use_cases.movimentacao.listar_movimentacao import ListarMovimentacao as ListarMovimentacaoInterface
from src.domain.entities.movimentacao import Movimentacao
from src.data.dto.movimentacao.listar_movimentacao_dto import ListarMovimentacaoDTO
from src.errors.types import HttpBadRequestError
from typing import List, Dict

class ListarMovimentacao(ListarMovimentacaoInterface):

    def __init__(self, movimentacao_repository: MovimentacaoRepositoryInterface):
        self.__movimentacao_repository = movimentacao_repository

    def listar_movimentacao(self, dto: ListarMovimentacaoDTO) -> List[Movimentacao]:
        self.__validar_page(dto.page)
        self.__validar_page_size(dto.page_size)
        
        page, page_size = self.__calcular_paginacao(dto.page, dto.page_size)

        movimentacoes = self.__movimentacao_repository.get_all_movimentacoes(page, page_size)
    
        if movimentacoes:
            response = self.__formatar_resposta(movimentacoes)
            return response
        
        return None
    
    def __calcular_paginacao(self, page: int, page_size: int):
        
        if page == 1:
            page = 0
        else:
            page = page - 1
            page = (page * page_size)

        return page, page_size
    
    @staticmethod
    def __validar_page(page: int):
        if not isinstance(page, int) or page <= 0:
            raise HttpBadRequestError("page deve ser um numero inteiro positivo")
    
    @staticmethod
    def __validar_page_size(page_size: int):
        if not isinstance(page_size, int) or page_size <= 0:
            raise HttpBadRequestError("page_size deve ser um numero inteiro positivo")
   
    @staticmethod
    def __formatar_resposta(movimentacoes: Movimentacao) -> Dict:
        lista_movimentacoes = []
        for movimentacao in movimentacoes:
            lista_movimentacoes.append({
                    "id": movimentacao.id,
                    "codigo_dispositivo": movimentacao.codigo,
                    "local_origem": movimentacao.local_origem,
                    "local_destino": movimentacao.local_destino,
                    "data_movimentacao": movimentacao.data_movimentacao.strftime('%Y-%m-%d %H:%M:%S'),
                    "re_usuario": movimentacao.usuario
                })
             
        return {
            "type": "Movimentacao",
            "data": lista_movimentacoes
        }