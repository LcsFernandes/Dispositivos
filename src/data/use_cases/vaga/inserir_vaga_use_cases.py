from src.domain.use_cases.vaga.inserir_vaga import InserirVaga as InserirVagaInterface
from src.data.interfaces.vaga_repository import VagaRepositoryInterface


class InserirVaga(InserirVagaInterface):

    def __init__(self, vaga_repository: VagaRepositoryInterface):
        self.__vaga_repository = vaga_repository

    
    def inserir_vaga(self, deposito_id: int, identificacao: str) -> None:
        self.__valida_deposito_id(deposito_id)
        self.__valida_identificacao(identificacao)

        self.__vaga_repository.inserir_vaga(deposito_id, identificacao)


    @classmethod    
    def __valida_deposito_id(cls, deposito_id: int):
        if not deposito_id or not isinstance(id, int) or deposito_id < 0:
            raise Exception("o deposito_id é um campo obrigatorio inteiro positivo")
        if deposito_id != 74:
            raise Exception("deposito_id informado nao pertence ao armazem de dispositivos")
        
    
    def __valida_identificacao(self, identificacao: str):
        if not identificacao:
            raise Exception("identificacao da vaga é um campo obrigatorio")
        if len(identificacao) < 3:
            raise Exception("Nome de identificacao para vaga invalido")
        
        vaga = self.__vaga_repository.get_vaga_by_identificacao(identificacao)

        if vaga:
            raise Exception(f"A vaga com a identificacao {vaga.identificacao} ja esta cadastrada")
        