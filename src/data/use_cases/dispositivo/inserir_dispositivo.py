from src.domain.use_cases.dispositivo.inserir_dispositivo import InserirDispositivo as InserirDispositivoInterface
from src.data.dto.dispositivo.inserir_dipositivo_dto import InserirDispositivoDTO
from src.infra.database.repositories.dispositivo_repository import DispositivoRepository
from datetime import date

class InserirDispositivo(InserirDispositivoInterface):

    def __init__ (self, dispositivo_repository: DispositivoRepository):
        self.__dispositivo_repository = dispositivo_repository

    def inserir_dispositivo(self, dto: InserirDispositivoDTO):
        if dto.codigo:
            self.__valida_codigo(dto.codigo)
        if dto.tipo: 
            self.__valida_tipo(dto.tipo)
        if dto.descricao:
            self.__valida_descricao(dto.descricao)
        if dto.vaga:
            self.__valida_vaga(dto.vaga)
        if dto.status:
            self.__valida_status(dto.status)
        if dto.data_fabricacao:
            self.__valida_data_fabricacao(dto.data_fabricacao)

        self.__dispositivo_repository.adicionar_dispositivo(dto.codigo, dto.tipo, dto.descricao, dto.vaga, dto.status, dto.data_fabricacao, dto.cliente)
        
    
    @staticmethod
    def __valida_codigo(codigo: str) -> None:
        if not codigo:
            raise Exception("O codigo é obrigatorio para inserir o dispositivo")
    
    @staticmethod
    def __valida_tipo(tipo: int) -> None:
        if not tipo:
            raise Exception("O tipo é um parametro obrigatorio")
    
        if not isinstance(tipo, int):
            raise Exception("O tipo deve ser integer")
    
    @staticmethod
    def __valida_descricao(descricao: str) -> None:
        if not descricao or not descricao.strip():
            raise Exception("A descrição é obrigatória")

    
    def __valida_vaga(self, vaga: str) -> None:
        if vaga is None:
            raise Exception("A vaga é obrigatória")
        
        if not isinstance(vaga, str):
            raise Exception("A vaga deve ser uma string")
        
        if len(vaga) < 3:
            raise Exception("Nome inválido para vaga")
        
        vaga = self.__dispositivo_repository.get_vaga_by_identificacao(vaga)

        if vaga:
            raise Exception(f"A vaga {vaga} já esta cadastrada")
        

    @staticmethod
    def __valida_status(status: str) -> None:
        if not status:
            raise Exception("O status é obrigatório")
        if status not in [1, 0]: 
            raise Exception("Status inválido. Valores aceitos: 1 = 'ativo' ou 0 = 'inativo'")

    @staticmethod
    def __valida_data_fabricacao(data_fabricacao: date) -> None:
        
        if not data_fabricacao:
            raise Exception("A data de fabricação é obrigatória")
        if not isinstance(data_fabricacao, date):
            raise Exception("A data de fabricação deve ser uma data válida")
        
        if data_fabricacao > date.today():
            raise Exception("A data de fabricação Não pode ser maior do que a data atual")
