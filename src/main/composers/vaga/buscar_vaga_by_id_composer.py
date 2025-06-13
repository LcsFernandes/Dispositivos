from src.infra.database.repositories.vaga_repository import VagaRepository
from src.data.use_cases.vaga.buscar_vaga_by_id import BuscarVagaById
from src.presentation.controllers.vaga_controller import BuscarVagaByIdController

def buscar_vaga_by_id_composer():
    repository = VagaRepository()
    use_case = BuscarVagaById(repository)
    controller = BuscarVagaByIdController(use_case)

    return controller.handle