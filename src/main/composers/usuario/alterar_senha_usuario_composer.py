from src.infra.database.repositories.usuario_repository import UsuarioRepository
from src.data.use_cases.usuario.alterar_senha_usuario import AlterarSenhaUsuario
from src.infra.services.senha_service import SenhaService
from src.presentation.controllers.usuario_controller import AlterarSenhaUsuarioController

def alterar_senha_usuario_composer():
    repository = UsuarioRepository()
    senha_service = SenhaService()
    use_case = AlterarSenhaUsuario(repository, senha_service)
    controller = AlterarSenhaUsuarioController(use_case)

    return controller.handle