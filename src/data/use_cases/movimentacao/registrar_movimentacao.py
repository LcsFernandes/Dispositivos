from src.data.interfaces.movimentacao_repository import MovimentacaoRepositoryInterface
from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.data.interfaces.vaga_repository import VagaRepositoryInterface
from src.domain.use_cases.movimentacao.registrar_movimentacao import RegistrarMovimentacao as RegistrarMovimentacaoInterface
from src.data.dto.movimentacao.registrar_movimentacao_dto import RegistrarMovimentacaoDTO
from src.errors.types import HttpBadRequestError
from datetime import datetime

class RegistrarMovimentacao(RegistrarMovimentacaoInterface):

    def __init__(self, movimentacao_repository: MovimentacaoRepositoryInterface, dispositivo_repository: DispositivoRepositoryInterface, vaga_repository: VagaRepositoryInterface):
        self.__movimentacao_repository = movimentacao_repository
        self.__dispositivo_repository = dispositivo_repository
        self.__vaga_repository = vaga_repository


    def registrar_movimentacao(self, dto: RegistrarMovimentacaoDTO):
        self.__valida_dispositivo(dto.id_dispositivo)
        self.__valida_local(dto.local_origem)
        self.__valida_local(dto.local_destino)
        self.__valida_usuario(dto.login_id)

        data_movimentacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.__movimentacao_repository.registrar_movimentacao(dto.id_dispositivo, dto.local_origem, dto.local_destino, data_movimentacao, dto.login_id)      
    
    
    def __valida_dispositivo(self, id_dispositivo: int):
        if not id_dispositivo or id_dispositivo < 0:
            raise HttpBadRequestError("id_dispositivo é um campo inteiro positivo obrigatório")
         
        dispositivo = self.__dispositivo_repository.get_dispositivo_by_id(id_dispositivo)
        
        if not dispositivo:
            raise HttpBadRequestError(f"Dispositivo id {id_dispositivo} nao encontrado")
    
    
    def __valida_local(self, local: int):
        if not local or not isinstance(local, int) or local < 0:
            raise HttpBadRequestError("local é um campo inteiro positivo obrigatório")
        
        vaga = self.__vaga_repository.get_vaga_by_id(local)

        if not vaga:
            raise HttpBadRequestError("Vaga nao encontrada")
    
    @staticmethod
    def __valida_usuario(login_id: int):
        if not isinstance(login_id, int) or login_id <= 0:
            raise HttpBadRequestError("login_id é um campo inteiro positivo obrigatório")