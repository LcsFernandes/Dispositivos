from src.domain.use_cases.dispositivo.inserir_dispositivo import InserirDispositivo as InserirDispositivoInterface
from src.data.dto.dispositivo.inserir_dipositivo_dto import InserirDispositivoDTO
from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.data.interfaces.vaga_repository import VagaRepositoryInterface
from src.errors.types import HttpBadRequestError
from datetime import datetime, date


class InserirDispositivo(InserirDispositivoInterface):

    def __init__ (self, dispositivo_repository: DispositivoRepositoryInterface):
        self.__dispositivo_repository = dispositivo_repository

    def inserir_dispositivo(self, dto: InserirDispositivoDTO):  
        self.__valida_codigo(dto.codigo)    
        self.__valida_tipo(dto.tipo)    
        self.__valida_descricao(dto.descricao)     
        self.__valida_status(dto.status)    
        self.__valida_data_fabricacao(dto.data_fabricacao)

        self.__dispositivo_repository.adicionar_dispositivo(dto.codigo, dto.tipo, dto.descricao, dto.status, dto.data_fabricacao, dto.cliente)
        
    
    
    def __valida_codigo(self, codigo: str) -> None:
        if not codigo:
            raise HttpBadRequestError("O codigo e obrigatorio para inserir o dispositivo")
        
        dispositivo = self.__dispositivo_repository.get_dispositivo_by_codigo(codigo)

        if dispositivo:
            raise HttpBadRequestError(f"O dispositivo {codigo} ja esta cadastrado")
    
    @staticmethod
    def __valida_tipo(tipo: int) -> None:
        if not tipo:
            raise HttpBadRequestError("O tipo e um parametro obrigatorio")
    
        if not isinstance(tipo, int):
            raise HttpBadRequestError("O tipo deve ser integer")
    
    @staticmethod
    def __valida_descricao(descricao: str) -> None:
        if not descricao or not descricao.strip():
            raise HttpBadRequestError("A descricao e obrigatória")

    @staticmethod
    def __valida_status(status: str) -> None:
        if not status:
            raise HttpBadRequestError("O status e obrigatorio")
        if status not in [1, 2]: 
            raise HttpBadRequestError("Status invalido. Valores aceitos: 1 = 'ativo' ou 2 = 'inativo'")

    @staticmethod
    def __valida_data_fabricacao(data_fabricacao: date) -> None:
        
        if not data_fabricacao:
            raise HttpBadRequestError("A data de fabricacao é obrigatoria")
        
        try:
            data_fabricacao = datetime.strptime(data_fabricacao, "%Y-%m-%d").date()
        except ValueError:
            raise HttpBadRequestError("A data de fabricacao deve estar no formato YYYY-MM-DD")

        if not isinstance(data_fabricacao, date):
            raise HttpBadRequestError("A data de fabricacao deve ser uma data valida")
        
        if data_fabricacao > date.today():
            raise HttpBadRequestError("A data de fabricaçao nao pode ser maior do que a data atual")
