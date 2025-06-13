from src.infra.database.repositories.dispositivo_repository import DispositivoRepository
from src.data.use_cases.dispositivo.excluir_dispositivo import ExcluirDispositivo
from src.presentation.controllers.dispositivo_controller import ExcluirDispositivoController

def excluir_dispositivo_composer():
    repository = DispositivoRepository()
    use_case = ExcluirDispositivo(repository)
    controller = ExcluirDispositivoController(use_case)

    return controller.handle