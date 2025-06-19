from src.domain.use_cases.vaga.alterar_vaga import AlterarVaga as AlterarvagaInterface
from src.data.dto.vaga.alterar_vaga_dto import AlterarVagaDTO
from src.data.interfaces.vaga_repository import VagaRepositoryInterface
from src.errors.types import HttpBadRequestError


class AlterarVaga(AlterarvagaInterface):

    def __init__(self, vaga_repository: VagaRepositoryInterface):
        self.__vaga_repository = vaga_repository

    def alterar_vaga(self, dto: AlterarVagaDTO) -> None:
        self.__valida_id(dto.id)
        self.__valida_deposito_id(dto.deposito_id)
        self.__valida_identificacao(dto.identificacao)

        self.__vaga_repository.atualizar_vaga(dto.id, dto.deposito_id, dto.identificacao)
    
    @staticmethod 
    def __valida_id(id: int):
        if not id or not isinstance(id, int) or id < 0:
            raise HttpBadRequestError("o id e um campo obrigatorio inteiro positivo")
        
    @staticmethod   
    def __valida_deposito_id(deposito_id: int):
        if not deposito_id or not isinstance(deposito_id, int) or deposito_id < 0:
            raise HttpBadRequestError("o deposito_id e um campo obrigatorio inteiro positivo")
        if deposito_id != 74:
            raise HttpBadRequestError("deposito_id informado nao pertence ao armazem de dispositivos")
    
    @staticmethod
    def __valida_identificacao(identificacao: str):
        if not identificacao:
            raise HttpBadRequestError("identificacao da vaga e um campo obrigatorio")
        if len(identificacao) < 3:
            raise HttpBadRequestError("Nome de identificacao para vaga invalido")