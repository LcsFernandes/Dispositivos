from src.domain.use_cases.usuario.login import LoginUsuario as LoginUsuarioInterface
from src.data.interfaces.usuario_repository import UsuarioRepositoryInterface
from src.infra.services.senha_service import SenhaService
from src.infra.services.token_service import TokenService
from src.data.dto.usuario.login_usuario_dto import LoginUsuarioDTO
from src.errors.types import HttpUnauthorizedError, ConfigurationError


class LoginUsuario(LoginUsuarioInterface):

    def __init__(self, usuario_repository: UsuarioRepositoryInterface, senha_service: SenhaService, token_service: TokenService):
        self.__usuario_repository = usuario_repository
        self.__senha_service = senha_service
        self.__token_service = token_service

    def login_usuario(self, dto: LoginUsuarioDTO):
        
            usuario = self.__valida_usuario(dto.re, dto.senha)

            try:
                token = self.__token_service.criar_token({"user_id": usuario.id})
            except Exception:
                raise ConfigurationError("Erro ao gerar token.")
            

            response = self.__formata_resposta(token)
            
            return response
    
    def __valida_usuario(self, re: str, senha: str):
        self.__valida_re(re)
        self.__valida_senha(senha)

        usuario = self.__usuario_repository.get_usuario(re)

        if not usuario:
            raise HttpUnauthorizedError(f"Credencias Invalidas")
        
        if not self.__senha_service.verificar_senha(senha, usuario.senha):
            raise HttpUnauthorizedError("Credencias Invalidas")
        
        return usuario

    @staticmethod
    def __valida_re(re: str):
        if not isinstance(re, str) or len(re.strip()) != 6:
            raise HttpUnauthorizedError("Credencias Invalidas")

    @staticmethod
    def __valida_senha(senha: str):
        if not isinstance(senha, str) or len(senha.strip()) < 6:
            raise HttpUnauthorizedError("Credencias invalidas.")    
        
        
    @staticmethod
    def __formata_resposta(token: str):
        return {
                "access_token": token,
                "token_type": "bearer"
            }

        


    