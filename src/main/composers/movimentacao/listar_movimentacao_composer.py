from src.infra.database.repositories.movimentacao_repository import MovimentacaoRepository
from src.data.use_cases.movimentacao.listar_movimentacao import ListarMovimentacao
from src.presentation.controllers.movimentacao_controller import ListarMovimentacaoController

def listar_movimentacao_composer():
    repository = MovimentacaoRepository()
    use_case = ListarMovimentacao(repository)
    controller = ListarMovimentacaoController(use_case)

    return controller.handle