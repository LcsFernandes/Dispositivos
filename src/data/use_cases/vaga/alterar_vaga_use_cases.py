from src.domain.use_cases.vaga.alterar_vaga import AlterarVaga as AlterarvagaInterface
from src.data.interfaces.vaga_repository import VagaRepositoryInterface


class AlterarVaga(AlterarvagaInterface):

    def __init__(self, vaga_repository: VagaRepositoryInterface):
        self.__vaga_repository = vaga_repository

    def alterar_vaga(self, id: int, deposito_id: int, identificacao: str) -> None:
        self.__valida_id(id)
        self.__valida_deposito_id(deposito_id)
        self.__valida_identificacao(identificacao)

        self.__vaga_repository.atualizar_vaga(id, deposito_id, identificacao)
    
    def __valida_id(self, id: int):
        if not id or not isinstance(id, int) or id < 0:
            raise Exception("o id é um campo obrigatorio inteiro positivo")
        
    @classmethod    
    def __valida_deposito_id(cls, deposito_id: int):
        if not deposito_id or not isinstance(id, int) or deposito_id < 0:
            raise Exception("o deposito_id é um campo obrigatorio inteiro positivo")
        if deposito_id != 74:
            raise Exception("deposito_id informado nao pertence ao armazem de dispositivos")
    
    @classmethod
    def __valida_identificacao(cls, identificacao: str):
        if not identificacao:
            raise Exception("identificacao da vaga é um campo obrigatorio")
        if len(identificacao) < 3:
            raise Exception("Nome de identificacao para vaga invalido")