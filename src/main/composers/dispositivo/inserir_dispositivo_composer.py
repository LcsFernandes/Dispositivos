from src.infra.database.repositories.dispositivo_repository import DispositivoRepository
from src.data.use_cases.dispositivo.inserir_dispositivo import InserirDispositivo
from src.presentation.controllers.dispositivo_controller import InserirDispositivoController

def inserir_dispositivo_composer():
    repository = DispositivoRepository()
    use_case = InserirDispositivo(repository)
    controller = InserirDispositivoController(use_case)

    return controller.handle