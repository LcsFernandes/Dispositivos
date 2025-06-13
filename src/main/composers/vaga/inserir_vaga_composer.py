from src.infra.database.repositories.vaga_repository import VagaRepository
from src.data.use_cases.vaga.inserir_vaga import InserirVaga
from src.presentation.controllers.vaga_controller import InserirVagaController

def inserir_vaga_composer():
    repository = VagaRepository()
    use_case = InserirVaga(repository)
    controller = InserirVagaController(use_case)

    return controller.handle