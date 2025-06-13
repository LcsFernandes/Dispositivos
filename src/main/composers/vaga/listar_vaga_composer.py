from src.infra.database.repositories.vaga_repository import VagaRepository
from src.data.use_cases.vaga.listar_vaga import ListarVaga
from src.presentation.controllers.vaga_controller import ListarVagasController

def listar_vaga_composer():
    repository = VagaRepository()
    use_case = ListarVaga(repository)
    controller = ListarVagasController(use_case)

    return controller.handle