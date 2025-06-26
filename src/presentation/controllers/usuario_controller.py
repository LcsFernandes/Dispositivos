from src.presentation.interfaces.controller_interface import ControllerInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.domain.use_cases.usuario.criar_usuario import CriarUsuario as CriarUsuarioInterface
from src.data.dto.usuario.criar_usuario_dto import CriarUsuarioDTO
from src.data.dto.movimentacao.registrar_movimentacao_dto import RegistrarMovimentacaoDTO


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