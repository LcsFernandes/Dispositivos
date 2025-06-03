from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.domain.entities.dispositivo import Dispositivo
from src.domain.use_cases.dispositivo.buscar_dispositivo import BuscarDispositivos

class BuscarDispositivo(DispositivoRepositoryInterface):

    def __init__(self, dispositivo_repository: DispositivoRepositoryInterface):
        self.__dispositivo_repository = dispositivo_repository
        
    def buscar_dispositivo(self, codigo: str) -> Dispositivo:
        