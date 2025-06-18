from src.infra.database.repositories.dispositivo_repository import DispositivoRepository
from src.data.use_cases.dispositivo.buscar_posicao_dispositivo import BuscarPosicaoDispositivo
from src.presentation.controllers.dispositivo_controller import BuscarPosicaoDispositivoController

def buscar_posicao_dispositivo_composer():
    repository = DispositivoRepository()
    use_case = BuscarPosicaoDispositivo(repository)
    controller = BuscarPosicaoDispositivoController(use_case)

    return controller.handle