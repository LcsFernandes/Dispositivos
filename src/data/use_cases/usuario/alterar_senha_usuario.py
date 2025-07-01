from src.domain.use_cases.usuario.alterar_senha import AlterarSenhaUsuario as AlterarSenhaUsuarioInterface
from src.data.interfaces.usuario_repository import UsuarioRepositoryInterface
from src.data.dto.usuario.alterar_senha_usuario import AlterarSenhaUsuarioDTO
from src.domain.services.senha_service import SenhaServiceInterface
from src.errors.types import HttpUnauthorizedError, HttpBadRequestError

class AlterarSenhaUsuario(AlterarSenhaUsuarioInterface):

    def __init__(self, usuario_repository: UsuarioRepositoryInterface, senha_service: SenhaServiceInterface):
        self.__usuario_repository = usuario_repository
        self.__senha_service = senha_service

    def alterar_senha_usuario(self, dto: AlterarSenhaUsuarioDTO):
        self.__valida_re(dto.re)
        self.__valida_senha(dto.senha)
        self.__valida_senha(dto.senha_atual)

        usuario = self.__usuario_repository.get_usuario(dto.re)

        if not usuario:
            raise HttpBadRequestError(f"usuario com {dto.re} nao encontrado")

        if not self.__senha_service.verificar_senha(dto.senha_atual, usuario.senha):
            raise HttpUnauthorizedError("Senha atual não coincide com a ultima senha cadastrada")
        
        senha_hash = self.__senha_service.hash_senha(dto.senha)

        self.__usuario_repository.alterar_senha_usuario(dto.re, senha_hash)


    @staticmethod
    def __valida_re(re: int):
        if not isinstance(re, int) or len(str(re)) > 6:
            raise HttpBadRequestError("RE invalido")

    @staticmethod
    def __valida_senha(senha: str):
        if not isinstance(senha, str) or len(senha.strip()) < 6:
            raise HttpBadRequestError("Senha invalida.")  

