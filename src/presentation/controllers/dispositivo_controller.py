from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.dispositivo.alterar_dispositivo import AlterarDispositivo as AlterarDispositivoInterface
from src.domain.use_cases.dispositivo.buscar_dispositivo_by_codigo import BuscarDispositivosByCodigo as BuscarDispositivoByCodigoInterface
from src.domain.use_cases.dispositivo.buscar_dispositivo_by_id import BuscarDispositivosById as BuscarDispositivoByIdInterface
from src.domain.use_cases.dispositivo.excluir_dispositivo import ExcluirDispositivo as ExcluirDispositivoInterface
from src.domain.use_cases.dispositivo.inserir_dispositivo import InserirDispositivo as InserirDispositivoInterface
from src.domain.use_cases.dispositivo.listar_dispositivos import ListarDispositivos as ListarDispositivoInterface
from src.domain.use_cases.dispositivo.verificar_status_dispositivo import VerificarStatusDispositivo as VerificarStatusDispositivoInterface
from src.domain.use_cases.dispositivo.buscar_posicao_dispositivo import BuscarPosicaoDispositivo as BuscarPosicaoDispositivoInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.data.dto.dispositivo.alterar_dispositivo_dto import AlterarDispositivoDTO
from src.data.dto.dispositivo.buscar_dispositivo_dto import BuscarDispositivoDTO
from src.data.dto.dispositivo.excluir_dispositivo_dto import ExcluirDispositivoDTO
from src.data.dto.dispositivo.inserir_dipositivo_dto import InserirDispositivoDTO
from src.data.dto.dispositivo.verificar_status_dispositivos_dto import VerificarStatusDispositivoDTO 


class AlterarDispositivoController(ControllerInterface):
    
    def __init__(self, use_case: AlterarDispositivoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.path_params["id_dispositivo"]
        codigo = http_request.body.get("codigo")
        tipo = http_request.body.get("tipo")
        descricao = http_request.body.get("descricao")
        status = http_request.body.get("status")
        data_fabricacao = http_request.body.get("data_fabricacao")
        cliente = http_request.body.get("cliente")

        dto = AlterarDispositivoDTO(id=id, codigo=codigo, tipo=tipo, descricao=descricao, status=status, data_fabricacao=data_fabricacao, cliente=cliente)

        response = self.__use_case.alterar_dispositivo(dto)

        return HttpResponse(status_code=201, body=response)

class BuscarDispositivosByCodigoController(ControllerInterface):
    
    def __init__(self, use_case: BuscarDispositivoByCodigoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        codigo = http_request.path_params["codigo_dispositivo"]

        dto = BuscarDispositivoDTO(codigo=codigo)

        response = self.__use_case.buscar_dispositivo_by_codigo(dto)

        return HttpResponse(status_code=200, body=response)
    
class BuscarDispositivoByIdController(ControllerInterface):
    
    def __init__(self, use_case: BuscarDispositivoByIdInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.path_params["id_dispositivo"]

        dto = BuscarDispositivoDTO(id=id)

        response = self.__use_case.buscar_dispositivo_by_id(dto)

        return  HttpResponse(status_code=200, body=response)
    
class ExcluirDispositivoController(ControllerInterface):
    
    def __init__(self, use_case: ExcluirDispositivoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        codigo = http_request.path_params["codigo_dispositivo"]

        dto = ExcluirDispositivoDTO(codigo=codigo)

        response = self.__use_case.excluir_dispositivo(dto)

        return HttpResponse(status_code=204, body=response)
    
class InserirDispositivoController(ControllerInterface):
    
    def __init__ (self, use_case: InserirDispositivoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        codigo = http_request.body["codigo"]
        tipo = http_request.body["tipo"]
        descricao = http_request.body["descricao"]
        status = http_request.body["status"]
        data_fabricacao = http_request.body["data_fabricacao"]
        cliente = http_request.body.get("cliente")

        dto = InserirDispositivoDTO(codigo=codigo, tipo=tipo, descricao=descricao, status=status, data_fabricacao=data_fabricacao, cliente=cliente)

        response = self.__use_case.inserir_dispositivo(dto)

        return HttpResponse(status_code=201, body=response)

class ListarDispositivoController(ControllerInterface):

    def __init__(self, use_case: ListarDispositivoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest)-> HttpResponse:
        
        response = self.__use_case.listar_dispositivos()
 
        return HttpResponse(status_code=200, body=response)
    
class VerificarStatusDispositivoController(ControllerInterface):

    def __init__(self, use_case: VerificarStatusDispositivoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        codigo = http_request.query_params["codigo_dispositivo"]

        dto = VerificarStatusDispositivoDTO(codigo=codigo)

        response = self.__use_case.verificar_status_dispositivo(dto)

        return HttpResponse(status_code=200, body=response)
    
class BuscarPosicaoDispositivoController(ControllerInterface):

    def __init__(self, use_case: BuscarPosicaoDispositivoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        codigo = http_request.query_params["codigo_dispositivo"]

        dto = BuscarDispositivoDTO(codigo=codigo)

        response = self.__use_case.buscar_posicao_dispositivo(dto)

        return HttpResponse(status_code=200, body=response)
