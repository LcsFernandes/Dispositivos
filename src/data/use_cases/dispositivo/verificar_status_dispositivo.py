from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.data.dto.dispositivo.verificar_status_dispositivos_dto import VerificarStatusDispositivoDTO
from src.domain.use_cases.dispositivo.verificar_status_dispositivo import VerificarStatusDispositivo as VerificarStatusDispositivoInterface


class VerificarStatusDispositivo(VerificarStatusDispositivoInterface):

    def __init__(self, dispositivo_repository: DispositivoRepositoryInterface):
        self.__dispositivo_repository = dispositivo_repository

    def verificar_status_dispositivo(self, dto: VerificarStatusDispositivoDTO):
        self.__valida_codigo_dispositivo(dto.codigo)

        dispositivo = self.__dispositivo_repository.get_dispositivo_by_codigo(dto.codigo)

        if not dispositivo:
            raise Exception("Dispositivo nao encontrado")
        
        response = self.__dispositivo_repository.verificar_status_dispositivo(dto.codigo)

        return response

    
    def __valida_codigo_dispositivo(self, codigo: str):
        if not codigo or not isinstance(codigo, str):
            raise Exception("codigo do dispositivo é um campo tipo string obrigatorio")
    
        

        