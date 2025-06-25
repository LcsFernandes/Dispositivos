from src.infra.database.repositories.movimentacao_repository import MovimentacaoRepository
from src.infra.database.repositories.dispositivo_repository import DispositivoRepository
from src.data.use_cases.movimentacao.buscar_movimentacao import BuscarMovimentacao
from src.presentation.controllers.movimentacao_controller import BuscarMovimentacaoController

def buscar_movimentacao_composer():
    movimentacao_repository = MovimentacaoRepository()
    disposito_repository = DispositivoRepository()
    use_case = BuscarMovimentacao(movimentacao_repository, disposito_repository)
    controller = BuscarMovimentacaoController(use_case)

    return controller.handle