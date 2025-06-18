from src.infra.database.repositories.movimentacao_repository import MovimentacaoRepository
from src.infra.database.repositories.dispositivo_repository import DispositivoRepository
from src.infra.database.repositories.vaga_repository import VagaRepository
from src.data.use_cases.movimentacao.registrar_movimentacao import RegistrarMovimentacao
from src.presentation.controllers.movimentacao_controller import RegistrarMovimentacaoController

def registrar_movimentacao_composer():
    movimentacao_repository = MovimentacaoRepository()
    dispositivo_repository = DispositivoRepository()
    vaga_repository = VagaRepository()
    use_case = RegistrarMovimentacao(movimentacao_repository, dispositivo_repository, vaga_repository)
    controller = RegistrarMovimentacaoController(use_case)

    return controller.handle