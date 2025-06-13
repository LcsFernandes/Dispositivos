from src.infra.database.repositories.vaga_repository import VagaRepository
from src.data.use_cases.vaga.alterar_vaga import AlterarVaga
from src.presentation.controllers.vaga_controller import AlterarVagaController

def alterar_vaga_composer():
    repository = VagaRepository()
    use_case = AlterarVaga(repository)
    controller = AlterarVagaController(use_case)

    return controller.handle