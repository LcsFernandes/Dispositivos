from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.dispositivo.alterar_dispositivo import AlterarDispositivo as AlterarDispositivoInterface
from src.domain.use_cases.dispositivo.buscar_dispositivo_by_codigo import BuscarDispositivosByCodigo as BuscarDispositivoByCodigoInterface
from src.domain.use_cases.dispositivo.buscar_dispositivo_by_id import BuscarDispositivosById as BuscarDispositivoByIdInterface
from src.domain.use_cases.dispositivo.excluir_dispositivo import ExcluirDispositivo as ExcluirDispositivoInterface
from src.domain.use_cases.dispositivo.inserir_dispositivo import InserirDispositivo as InserirDispositivoInterface
from src.domain.use_cases.dispositivo.listar_dispositivos import ListarDispositivos as ListarDispositivoInterface
from src.domain.use_cases.dispositivo.verificar_status_dispositivo import VerificarStatusDispositivo as VerificarStatusDispositivoInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class AlterarDispositivoController(ControllerInterface):
    
    def __init__(self, use_case: AlterarDispositivoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.body["id"]
        codigo = http_request.body["codigo"]
        tipo = http_request.body["tipo"]
        descricao = http_request.body["descricao"]
        vaga = http_request.body["vaga"]
        status = http_request.body["status"]
        data_fabricacao = http_request.body["data_fabricacao"]

        response = self.__use_case.alterar_dispositivo(id, codigo, tipo, descricao, vaga, status, data_fabricacao)

        return HttpResponse(status_code=201, body={response})

class BuscarDispositivosByCodigoController(ControllerInterface):
    
    def __init__(self, use_case: BuscarDispositivoByCodigoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        codigo = http_request.path_params["codigo"]

        response = self.__use_case.alterar_dispositivo(codigo)

        return HttpResponse(status_code=200, body={response})
    
class BuscarDispositivoByIdController(ControllerInterface):
    
    def __init__(self, use_case: BuscarDispositivoByIdInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.path_params["id"]

        response = self.__use_case.buscar_dispositivo_by_id(id)

        return  HttpResponse(status_code=200, body={response})
    
class ExcluirDispositivoController(ControllerInterface):
    
    def __init__(self, use_case: ExcluirDispositivoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        codigo = http_request.path_params["codigo"]

        response = self.__use_case.excluir_dispositivo(codigo)

        return HttpResponse(status_code=204, body={response})
    
class InserirDispositivoController(ControllerInterface):
    
    def __init__ (self, use_case: InserirDispositivoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        codigo = http_request.body["codigo"]
        tipo = http_request.body["tipo"]
        descricao = http_request.body["descricao"]
        vaga = http_request.body["vaga"]
        status = http_request.body["status"]
        data_fabricacao = http_request.body["data_fabricacao"]
        cliente = http_request.body["cliente"]

        response = self.__use_case.inserir_dispositivo(codigo, tipo, descricao, vaga, status, data_fabricacao, cliente)

        return HttpResponse(status_code=201, body={response})

class ListarDispositivoController(ControllerInterface):

    def __init__(self, use_case: ListarDispositivoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest)-> HttpResponse:
        
        response = self.__use_case.listar_dispositivos()
 
        return HttpResponse(status_code=200, body={response})
    
class VerificarStatusDispositivoController(ControllerInterface):

    def __init__(self, use_case: VerificarStatusDispositivoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        codigo = http_request.query_params["codigo"]

        response = self.__use_case(codigo)

        return HttpResponse(status_code=200, body={response})
