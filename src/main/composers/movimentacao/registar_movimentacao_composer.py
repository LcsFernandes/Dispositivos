from src.infra.database.repositories.movimentacao_repository import MovimentacaoRepository
from src.data.use_cases.movimentacao.registrar_movimentacao import RegistrarMovimentacao
from src.presentation.controllers.movimentacao_controller import RegistrarMovimentacaoController

def registrar_movimentacao_composer():
    repository = MovimentacaoRepository()
    use_case = RegistrarMovimentacao(repository)
    controller = RegistrarMovimentacaoController(use_case)

    return controller.handle