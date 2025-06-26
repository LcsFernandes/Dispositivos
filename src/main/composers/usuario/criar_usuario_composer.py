from src.infra.database.repositories.usuario_repository import UsuarioRepository
from src.infra.services.senha_service import SenhaService
from src.data.use_cases.usuario.criar_usuario import CriarUsuario
from src.presentation.controllers.usuario_controller import CriarUsarioController

def criar_usuario_composer():
    repository = UsuarioRepository()
    senha_service = SenhaService()
    use_case = CriarUsuario(repository, senha_service)
    controller = CriarUsarioController(use_case)

    return controller.handle