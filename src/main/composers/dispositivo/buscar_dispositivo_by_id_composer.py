from src.infra.database.repositories.dispositivo_repository import DispositivoRepository
from src.data.use_cases.dispositivo.buscar_dispositivo_by_id import BuscarDispositivoById
from src.presentation.controllers.dispositivo_controller import BuscarDispositivoByIdController

def buscar_dispositivo_by_id_composer():
    repository = DispositivoRepository()
    use_case = BuscarDispositivoById(repository)
    controller = BuscarDispositivoByIdController(use_case)

    return controller.handle