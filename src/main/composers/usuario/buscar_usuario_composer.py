from src.infra.database.repositories.usuario_repository import UsuarioRepository
from src.data.use_cases.usuario.buscar_usuario import BuscarUsuario
from src.presentation.controllers.usuario_controller import BuscarUsarioController

def buscar_usuario_composer():
    repository = UsuarioRepository()
    use_case = BuscarUsuario(repository)
    controller = BuscarUsarioController(use_case)

    return controller.handle