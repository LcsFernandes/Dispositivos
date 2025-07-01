from src.presentation.interfaces.controller_interface import ControllerInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.domain.use_cases.movimentacao.buscar_movimentacao import BuscarMovimentacao as BuscarMovimentacaoInterface
from src.domain.use_cases.movimentacao.listar_movimentacao import ListarMovimentacao as ListarMovimentacaoInterface
from src.domain.use_cases.movimentacao.registrar_movimentacao import RegistrarMovimentacao as RegistrarMovimentacaoInterface
from src.data.dto.movimentacao.buscar_movimentacao_dto import BuscarMovimentacaoDTO
from src.data.dto.movimentacao.registrar_movimentacao_dto import RegistrarMovimentacaoDTO
from src.data.dto.movimentacao.listar_movimentacao_dto import ListarMovimentacaoDTO


class BuscarMovimentacaoController(ControllerInterface):

    def __init__(self, use_case: BuscarMovimentacaoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        codigo = http_request.path_params["codigo_dispositivo"]
        page = int(http_request.query_params.get("page", 1))
        page_size = int(http_request.query_params.get("page_size", 10))

        dto = BuscarMovimentacaoDTO(codigo=codigo, page=page, page_size=page_size)

        response = self.__use_case.buscar_movimentacao(dto)

        if not response:
            return HttpResponse(status_code=204, body=None)

        return HttpResponse(status_code=200, body=response)
    
class ListarMovimentacaoController(ControllerInterface):

    def __init__(self, use_case: ListarMovimentacaoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        page = int(http_request.query_params.get("page", 1))
        page_size = int(http_request.query_params.get("page_size", 10))

        dto = ListarMovimentacaoDTO(page=page, page_size=page_size)
        
        response = self.__use_case.listar_movimentacao(dto)

        if not response:
            return HttpResponse(status_code=204, body=None)


        return HttpResponse(status_code=200, body=response)
    
class RegistrarMovimentacaoController(ControllerInterface):

    def __init__(self, use_case: RegistrarMovimentacaoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        codigo = http_request.body["codigo_dispositivo"]
        local_origem = http_request.body["local_origem"]
        local_destino = http_request.body["local_destino"]
        user_id = http_request.id_user

        dto = RegistrarMovimentacaoDTO(codigo=codigo, local_origem=local_origem, local_destino=local_destino, user_id=user_id)
        response = self.__use_case.registrar_movimentacao(dto)

        return HttpResponse(status_code=201, body=response)