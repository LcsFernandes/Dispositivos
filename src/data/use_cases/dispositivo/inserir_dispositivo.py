from src.domain.use_cases.dispositivo.inserir_dispositivo import InserirDispositivo as InserirDispositivoInterface
from src.infra.database.repositories.dispositivo_repository import DispositivoRepository
from datetime import date

class InserirDispositivo(InserirDispositivoInterface):

    def __init__ (self, dispositivo_repository: DispositivoRepository):
        self.__dispositivo_repository = dispositivo_repository

    def inserir_dispositivo(self, codigo, tipo, descricao, vaga, status, data_fabricacao, cliente):
        self.__valida_codigo
        self.__valida_tipo
        self.__valida_descricao
        self.__valida_vaga
        self.__valida_status
        self.__valida_data_fabricacao

        self.__dispositivo_repository.adicionar_dispositivo(codigo, tipo, descricao, vaga, status, data_fabricacao, cliente)
    
    @classmethod
    def __valida_codigo(cls, codigo: str) -> None:
        if not codigo:
            raise Exception("O codigo é obrigatorio para inserir o dispositivo")
    
    @classmethod
    def __valida_tipo(cls, tipo: int) -> None:
        if not tipo:
            raise Exception("O tipo é um parametro obrigatorio")
    
        if not isinstance(tipo, int):
            raise Exception("O tipo deve ser integer")
    
    @classmethod
    def __valida_descricao(cls, descricao: str) -> None:
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
        

    @classmethod
    def __valida_status(cls, status: str) -> None:
        if not status:
            raise Exception("O status é obrigatório")
        if status not in [1, 0]: 
            raise Exception("Status inválido. Valores aceitos: 1 = 'ativo' ou 0 = 'inativo'")

    @classmethod
    def __valida_data_fabricacao(cls, data_fabricacao) -> None:
        
        if not data_fabricacao:
            raise Exception("A data de fabricação é obrigatória")
        if not isinstance(data_fabricacao, date):
            raise Exception("A data de fabricação deve ser uma data válida")