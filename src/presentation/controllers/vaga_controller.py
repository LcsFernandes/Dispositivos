from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.vaga.alterar_vaga import AlterarVaga as AlterarVagaInterface
from src.domain.use_cases.vaga.buscar_vaga_by_id import BuscarVagaById as BuscarVagaByIdInterface
from src.domain.use_cases.vaga.buscar_vaga_by_identificacao import BuscarVagaByIdentificacao as BuscarVagaByIdentificacaoInterface
from src.domain.use_cases.vaga.inserir_vaga import InserirVaga as InserirVagaInterface
from src.domain.use_cases.vaga.listar_vagas import ListarVagas as ListarVagasInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.data.dto.vaga.alterar_vaga_dto import AlterarVagaDTO
from src.data.dto.vaga.buscar_vaga_by_id_dto import BuscarVagaByIdDTO
from src.data.dto.vaga.buscar_vaga_by_identificacao_dto import BuscarVagaByIdentificacaoDTO
from src.data.dto.vaga.inserir_vaga_dto import InserirVagaDTO


class AlterarVagaController(ControllerInterface):

    def __init__ (self, use_case: AlterarVagaInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.body.get("id")
        identificacao = http_request.body.get("identificacao")

        dto = AlterarVagaDTO(id=id, identificacao=identificacao)
        response = self.__use_case.alterar_vaga(dto)

        return HttpResponse(status_code=201, body =response)
    
class BuscarVagaByIdController(ControllerInterface):

    def __init__(self, use_case: BuscarVagaByIdInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.path_params["id_vaga"]

        dto = BuscarVagaByIdDTO(id=id)

        response = self.__use_case.buscar_vaga_by_id(dto)

        return HttpResponse(status_code=200, body=response)
    
class BuscarVagaByIdentificacaoController(ControllerInterface):
    def __init__(self, use_case: BuscarVagaByIdentificacaoInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        identificacao = http_request.path_params["identificacao"]

        dto = BuscarVagaByIdentificacaoDTO(identificacao=identificacao)

        response = self.__use_case.buscar_vaga_by_identificacao(dto)

        return HttpResponse(status_code=200, body=response)
    
class ListarVagasController(ControllerInterface):
    def __init__(self, use_case: ListarVagasInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        response = self.__use_case.listar_vagas()

        return HttpResponse(status_code=200, body=response)
    
class InserirVagaController(ControllerInterface):
    def __init__(self, use_case: InserirVagaInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        deposito_id = http_request.body["deposito_id"]
        identificacao = http_request.body["identificacao"]

        dto = InserirVagaDTO(deposito_id=deposito_id, identificacao=identificacao)

        response = self.__use_case.inserir_vaga(dto)

        return HttpResponse(status_code=201, body=response)

