from src.infra.database.repositories.dispositivo_repository import DispositivoRepository
from src.data.use_cases.dispositivo.listar_dispositivos import ListarDispositivo
from src.presentation.controllers.dispositivo_controller import ListarDispositivoController

def listar_dispositivo_composer():
    repository = DispositivoRepository()
    use_case = ListarDispositivo(repository)
    controller = ListarDispositivoController(use_case)

    return controller.handle