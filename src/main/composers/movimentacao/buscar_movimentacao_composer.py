from src.infra.database.repositories.movimentacao_repository import MovimentacaoRepository
from src.data.use_cases.movimentacao.buscar_movimentacao import BuscarMovimentacao
from src.presentation.controllers.movimentacao_controller import BuscarMovimentacaoController

def buscar_movimentacao_composer():
    repository = MovimentacaoRepository()
    use_case = BuscarMovimentacao(repository)
    controller = BuscarMovimentacaoController(use_case)

    return controller.handle