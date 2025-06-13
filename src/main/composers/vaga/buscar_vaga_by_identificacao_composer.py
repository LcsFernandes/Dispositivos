from src.infra.database.repositories.vaga_repository import VagaRepository
from src.data.use_cases.vaga.buscar_vaga_by_identificacao import BuscarVagaByIdentificacao
from src.presentation.controllers.vaga_controller import BuscarVagaByIdentificacaoController

def buscar_vaga_by_identificacao_composer():
    repository = VagaRepository()
    use_case = BuscarVagaByIdentificacao(repository)
    controller = BuscarVagaByIdentificacaoController(use_case)

    return controller.handle