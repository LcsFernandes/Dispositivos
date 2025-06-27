from src.infra.database.repositories.usuario_repository import UsuarioRepository
from src.infra.services.senha_service import SenhaService
from src.infra.services.token_service import TokenService
from src.data.use_cases.usuario.login_usuario import LoginUsuario
from src.presentation.controllers.usuario_controller import LoginUsuarioController

def login_usuario_composer():
    repository = UsuarioRepository()
    senha_service = SenhaService()
    token_service = TokenService()
    use_case = LoginUsuario(repository, senha_service, token_service)
    controller = LoginUsuarioController(use_case)

    return controller.handle