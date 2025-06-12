from src.domain.use_cases.dispositivo.inserir_dispositivo import InserirDispositivo as InserirDispositivoInterface
from src.data.dto.dispositivo.inserir_dipositivo_dto import InserirDispositivoDTO
from src.infra.database.repositories.dispositivo_repository import DispositivoRepository
from src.errors.types import HttpBadRequestError, HttpNotFoundError
from datetime import date

class InserirDispositivo(InserirDispositivoInterface):

    def __init__ (self, dispositivo_repository: DispositivoRepository):
        self.__dispositivo_repository = dispositivo_repository

    def inserir_dispositivo(self, dto: InserirDispositivoDTO):  
        self.__valida_codigo(dto.codigo)    
        self.__valida_tipo(dto.tipo)    
        self.__valida_descricao(dto.descricao)  
        self.__valida_vaga(dto.vaga)    
        self.__valida_status(dto.status)    
        self.__valida_data_fabricacao(dto.data_fabricacao)

        self.__dispositivo_repository.adicionar_dispositivo(dto.codigo, dto.tipo, dto.descricao, dto.vaga, dto.status, dto.data_fabricacao, dto.cliente)
        
    
    
    def __valida_codigo(self, codigo: str) -> None:
        if not codigo:
            raise HttpBadRequestError("O codigo é obrigatorio para inserir o dispositivo")
        
        dispositivo = self.__dispositivo_repository.get_dispositivo_by_codigo(codigo)

        if dispositivo:
            raise HttpBadRequestError(f"O dispositivo {codigo} ja esta cadastrado")
    
    @staticmethod
    def __valida_tipo(tipo: int) -> None:
        if not tipo:
            raise HttpBadRequestError("O tipo é um parametro obrigatorio")
    
        if not isinstance(tipo, int):
            raise HttpBadRequestError("O tipo deve ser integer")
    
    @staticmethod
    def __valida_descricao(descricao: str) -> None:
        if not descricao or not descricao.strip():
            raise HttpBadRequestError("A descrição é obrigatória")

    
    def __valida_vaga(self, vaga: str) -> None:
        if vaga is None:
            raise HttpBadRequestError("A vaga é obrigatória")
        
        if not isinstance(vaga, str):
            raise HttpBadRequestError("A vaga deve ser uma string")
        
        if len(vaga) < 3:
            raise HttpBadRequestError("Nome inválido para vaga")
        
        vaga = self.__dispositivo_repository.get_vaga_by_identificacao(vaga)

        if vaga:
            raise HttpBadRequestError(f"A vaga {vaga} já esta cadastrada")
        

    @staticmethod
    def __valida_status(status: str) -> None:
        if not status:
            raise HttpBadRequestError("O status é obrigatório")
        if status not in [1, 0]: 
            raise HttpBadRequestError("Status inválido. Valores aceitos: 1 = 'ativo' ou 0 = 'inativo'")

    @staticmethod
    def __valida_data_fabricacao(data_fabricacao: date) -> None:
        
        if not data_fabricacao:
            raise HttpBadRequestError("A data de fabricação é obrigatória")
        if not isinstance(data_fabricacao, date):
            raise HttpBadRequestError("A data de fabricação deve ser uma data válida")
        
        if data_fabricacao > date.today():
            raise HttpBadRequestError("A data de fabricação Não pode ser maior do que a data atual")
