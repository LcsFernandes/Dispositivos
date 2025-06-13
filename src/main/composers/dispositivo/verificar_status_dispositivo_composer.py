from src.infra.database.repositories.dispositivo_repository import DispositivoRepository
from src.data.use_cases.dispositivo.verificar_status_dispositivo import VerificarStatusDispositivo
from src.presentation.controllers.dispositivo_controller import VerificarStatusDispositivoController

def verificar_status_dispositivo_composer():
    repository = DispositivoRepository()
    use_case = VerificarStatusDispositivo(repository)
    controller = VerificarStatusDispositivoController(use_case)

    return controller.handle