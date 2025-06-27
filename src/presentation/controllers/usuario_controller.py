from src.presentation.interfaces.controller_interface import ControllerInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.domain.use_cases.usuario.criar_usuario import CriarUsuario as CriarUsuarioInterface
from src.domain.use_cases.usuario.buscar_usuario import BuscarUsuario as BuscarUsuarioInterface
from src.domain.use_cases.usuario.login import LoginUsuario as LoginUsuarioInterface
from src.data.dto.usuario.criar_usuario_dto import CriarUsuarioDTO
from src.data.dto.usuario.buscar_usuario_dto import BuscarUsuarioDTO
from src.data.dto.usuario.login_usuario_dto import LoginUsuarioDTO


class CriarUsarioController(ControllerInterface):

    def __init__(self, use_case: CriarUsuarioInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        re = http_request.body["re"]
        nome = http_request.body["nome"]
        senha = http_request.body["senha"]

        dto = CriarUsuarioDTO(re=re, nome=nome, senha=senha)

        response = self.__use_case.criar_usuario(dto)

        return HttpResponse(status_code=201, body=response)
    
class BuscarUsarioController(ControllerInterface):

    def __init__(self, use_case: BuscarUsuarioInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        re = http_request.path_params["re"]

        dto = BuscarUsuarioDTO(re=re)

        response = self.__use_case.buscar_usuario(dto)

        if not response:
            return HttpResponse(status_code=204, body=None)


        return HttpResponse(status_code=200, body=response)
    
class LoginUsuarioController(ControllerInterface):

    def __init__(self, use_case: LoginUsuarioInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        re = http_request.body["re"]
        senha = http_request.body["senha"]

        dto = LoginUsuarioDTO(re=re, senha=senha)

        response = self.__use_case.login_usuario(dto)

        return HttpResponse(status_code=200, body=response)