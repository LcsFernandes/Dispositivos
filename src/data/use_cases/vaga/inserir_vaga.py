from src.domain.use_cases.vaga.inserir_vaga import InserirVaga as InserirVagaInterface
from src.data.dto.vaga.inserir_vaga_dto import InserirVagaDTO
from src.data.interfaces.vaga_repository import VagaRepositoryInterface
from src.errors.types import HttpBadRequestError


class InserirVaga(InserirVagaInterface):

    def __init__(self, vaga_repository: VagaRepositoryInterface):
        self.__vaga_repository = vaga_repository

    
    def inserir_vaga(self, dto: InserirVagaDTO) -> None:
        self.__valida_deposito_id(dto.deposito_id)
        self.__valida_identificacao(dto.identificacao)

        self.__vaga_repository.inserir_vaga(dto.deposito_id, dto.identificacao)


    @staticmethod    
    def __valida_deposito_id(deposito_id: int):
        if not deposito_id or not isinstance(deposito_id, int) or deposito_id < 0:
            raise HttpBadRequestError("o deposito_id e um campo obrigatorio inteiro positivo")
        if deposito_id != 74:
            raise HttpBadRequestError("deposito_id informado nao pertence ao armazem de dispositivos")
        
    
    def __valida_identificacao(self, identificacao: str):
        if not identificacao:
            raise HttpBadRequestError("identificacao da vaga e um campo obrigatorio")
        if len(identificacao) < 3:
            raise HttpBadRequestError("Nome de identificacao para vaga invalido")
        
        vaga = self.__vaga_repository.get_vaga_by_identificacao(identificacao)

        if vaga:
            raise HttpBadRequestError(f"A vaga com a identificacao {vaga.identificacao} ja esta cadastrada")
        