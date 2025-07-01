from src.domain.use_cases.movimentacao.buscar_movimentacao import BuscarMovimentacao as BuscarMovimentacaoInterface
from src.data.interfaces.movimentacao_repository import MovimentacaoRepositoryInterface
from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.data.dto.movimentacao.buscar_movimentacao_dto import BuscarMovimentacaoDTO
from src.domain.entities.movimentacao import Movimentacao
from src.errors.types import HttpBadRequestError
from typing import Dict

class BuscarMovimentacao(BuscarMovimentacaoInterface):
    
    def __init__(self, movimentacao_repository: MovimentacaoRepositoryInterface, dispositivo_repository: DispositivoRepositoryInterface):
        self.__movimentacao_repository = movimentacao_repository
        self.__dispositivo_repository = dispositivo_repository

    def buscar_movimentacao(self, dto: BuscarMovimentacaoDTO):
        self.__valida_codigo(dto.codigo)
        self.__validar_page(dto.page)
        self.__validar_page_size(dto.page_size)
        
        dispositivo = self.__dispositivo_repository.get_dispositivo_by_codigo(dto.codigo)

        if not dispositivo:
            raise HttpBadRequestError("Dispositivo nao encontrado")
        

        page, page_size = self.__calcular_paginacao(dto.page, dto.page_size)

        movimentacao = self.__movimentacao_repository.get_movimentacao_por_dispositivo(dto.codigo, page, page_size)

        if movimentacao:
            response = self.__formatar_resposta(movimentacao)
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
    def __valida_codigo(codigo: str) -> None:
        if not codigo:
            raise HttpBadRequestError("codigo do dispositivo é um campo obrigatorio")
        
        if not isinstance(codigo, str) or len(codigo.strip()) <= 3:
            raise HttpBadRequestError("Codigo do dispositivo invalido")


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