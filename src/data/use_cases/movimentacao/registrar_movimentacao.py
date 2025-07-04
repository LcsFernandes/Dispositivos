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
        id_dispositivo = self.__validar_dispositivo(dto.codigo)
        id_vaga_origem = self.__validar_local_origem(dto.local_origem)
        self.__validar_posicao(dto.codigo, dto.local_origem)
        id_vaga_destino = self.__validar_local_destino(dto.local_destino)
        self.__validar_vagas_iguais(id_vaga_origem, id_vaga_destino)
        self.__validar_usuario(dto.user_id)
        data_movimentacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.__movimentacao_repository.registrar_movimentacao(id_dispositivo, id_vaga_origem, id_vaga_destino, data_movimentacao, dto.user_id)      
    
    
    def __validar_dispositivo(self, codigo: str):
        if not codigo or len(codigo.strip()) <= 3:
            raise HttpBadRequestError("Codigo do dispositivo inexistente ou invalido")
         
        dispositivo = self.__dispositivo_repository.get_dispositivo_by_codigo(codigo)
        
        if not dispositivo:
            raise HttpBadRequestError(f"Dispositivo {codigo} nao encontrado")
        
        if dispositivo.status != "Ativo":
            raise HttpBadRequestError(f"o dispositivo {dispositivo.codigo} nao esta ativo")
        
        return dispositivo.id
    
    
    def __validar_local_origem(self, local_origem: str):
        if not local_origem or not isinstance(local_origem, str) or len(local_origem.strip()) < 3:
            raise HttpBadRequestError("Local de origem inexistente ou invalido")
        
        vaga = self.__vaga_repository.get_vaga_by_identificacao(local_origem)

        if not vaga:
            raise HttpBadRequestError("Vaga de origem nao encontrada")
        
        return vaga.id
        
    def __validar_posicao(self, codigo: str, local_origem: str):

        posicao = self.__dispositivo_repository.buscar_posicao_dispositivo(codigo)
        
        if not posicao:
            return True
        
        if posicao[1] != local_origem:
            raise HttpBadRequestError("Dispositivo nao encontrado na vaga de origem. Nao e possivel realizar a movimentacao.")
    
    @staticmethod    
    def __validar_vagas_iguais(id_vaga_origem: int, id_vaga_destino: int):
        if id_vaga_origem == id_vaga_destino:
            raise HttpBadRequestError("A vaga de Destino deve ser diferente da vaga de Origem")

    def __validar_local_destino(self, local_destino: int):
        if not local_destino or not isinstance(local_destino, str) or len(local_destino.strip()) < 3:
            raise HttpBadRequestError("Local de destino inexistente ou invalido")
        
        vaga = self.__vaga_repository.get_vaga_by_identificacao(local_destino)

        if not vaga:
            raise HttpBadRequestError("Vaga de destino nao encontrada")
    
        return vaga.id
    
    @staticmethod
    def __validar_usuario(login_id: int):
        if not isinstance(login_id, int) or login_id <= 0:
            raise HttpBadRequestError("user_id e um campo inteiro positivo obrigatorio")