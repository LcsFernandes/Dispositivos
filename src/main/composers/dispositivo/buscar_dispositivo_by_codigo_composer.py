from src.infra.database.repositories.dispositivo_repository import DispositivoRepository
from src.data.use_cases.dispositivo.buscar_dispositivo_by_codigo import BuscarDispositivoByCodigo
from src.presentation.controllers.dispositivo_controller import BuscarDispositivosByCodigoController

def buscar_dispositivo_by_codigo_composer():
    repository = DispositivoRepository()
    use_case = BuscarDispositivoByCodigo(repository)
    controller = BuscarDispositivosByCodigoController(use_case)

    return controller.handle