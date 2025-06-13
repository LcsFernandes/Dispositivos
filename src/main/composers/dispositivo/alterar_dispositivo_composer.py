from src.infra.database.repositories.dispositivo_repository import DispositivoRepository
from src.data.use_cases.dispositivo.alterar_dispositivo import AlterarDispositivo
from src.presentation.controllers.dispositivo_controller import AlterarDispositivoController

def alterar_dispositivo_composer():
    repository = DispositivoRepository()
    use_case = AlterarDispositivo(repository)
    controller = AlterarDispositivoController(use_case)

    return controller.handle
