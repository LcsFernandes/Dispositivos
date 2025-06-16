from src.infra.database.repositories.dispositivo_repository import DispositivoRepository
from src.infra.database.repositories.vaga_repository import VagaRepository
from src.data.use_cases.dispositivo.inserir_dispositivo import InserirDispositivo
from src.presentation.controllers.dispositivo_controller import InserirDispositivoController

def inserir_dispositivo_composer():
    dispositivo_repository = DispositivoRepository()
    vaga_repository = VagaRepository()
    use_case = InserirDispositivo(dispositivo_repository, vaga_repository)
    controller = InserirDispositivoController(use_case)

    return controller.handle