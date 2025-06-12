from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.movimentacao.buscar_movimentacao import BuscarMovimentacao as BuscarMovimentacaoInterface
from src.domain.use_cases.movimentacao.listar_movimentacao import ListarMovimentacao as ListarMovimentacaoInterface
from src.domain.use_cases.movimentacao.registrar_movimentacao import RegistrarMovimentacao as RegistrarMovimentacaoInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class BuscarMovimentacaoController(ControllerInterface):

    def __init__(self, use_case: BuscarMovimentacaoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id_dispositivo = http_request.path_params["id_dispositivo"]

        response = self.__use_case.buscar_movimentacao(id_dispositivo)

        return HttpResponse(status_code=200, body={response})
    
class ListarMovimentacaoController(ControllerInterface):

    def __init__(self, use_case: ListarMovimentacaoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        
        response = self.__use_case.listar_movimentacao()

        return HttpResponse(status_code=200, body={response})
    
class RegistrarMovimentacaoController(ControllerInterface):

    def __init__(self, use_case: RegistrarMovimentacaoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id_dispositivo = http_request.body["id_dispositivo"]
        local_origem = http_request.body["local_origem"]
        local_destino = http_request.body["local_destino"]
        data_movimentacao = http_request.body["data_movimentacao"]
        usuario_id = http_request.body["usuario_id"]
        tipo = http_request.body["tipo"]


        response = self.__use_case.registrar_movimentacao(id_dispositivo, local_origem, local_destino, data_movimentacao, usuario_id, tipo)

        return HttpResponse(status_code=201, body={response})