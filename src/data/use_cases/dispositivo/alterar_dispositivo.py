from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.data.dto.dispositivo.alterar_dispositivo_dto import AlterarDispositivoDTO
from src.domain.use_cases.dispositivo.alterar_dispositivo import AlterarDispositivo as AlterarDispositivoInterface 
from src.errors.types import HttpBadRequestError
from datetime import date, datetime

class AlterarDispositivo(AlterarDispositivoInterface):

    def __init__ (self, dispositivo_repository: DispositivoRepositoryInterface):
        self.__dispositivo_repository = dispositivo_repository

    def alterar_dispositivo(self, dto: AlterarDispositivoDTO) -> None:
        self.__valida_id(dto.id)

        dispositivo = self.__dispositivo_repository.get_dispositivo_by_id(dto.id)
        
        if not dispositivo:
            raise HttpBadRequestError("dispositivo nao encontrado")

        if dto.codigo is not None:
            self.__valida_codigo(dto.codigo)
            dispositivo.codigo = dto.codigo

        if dto.tipo is not None:
            self.__valida_tipo(dto.tipo)
            dispositivo.tipo = dto.tipo

        if dto.descricao is not None:
            self.__valida_descricao(dto.descricao)
            dispositivo.descricao = dto.descricao

        if dto.status is not None:
            self.__valida_status(dto.status)
            dispositivo.status = dto.status

        if dto.data_fabricacao is not None:
            self.__valida_data_fabricacao(dto.data_fabricacao)
            dispositivo.data_fabricacao = dto.data_fabricacao

        
        self.__dispositivo_repository.atualizar_dispositivo(
            dispositivo.id,
            dispositivo.codigo,
            dispositivo.tipo,
            dispositivo.descricao,
            dispositivo.status,
            dispositivo.data_fabricacao,
            dispositivo.cliente
        )

    @staticmethod
    def __valida_id(id: int) -> None:
        if not isinstance(id, int) or id <= 0:
            raise HttpBadRequestError("O ID deve ser um inteiro positivo")

    @staticmethod
    def __valida_codigo(codigo: str) -> None:
        if not isinstance(codigo, str) or len(codigo.strip()) < 3:
            raise HttpBadRequestError("Codigo deve conter pelo menos 3 caracteres")

    @staticmethod
    def __valida_tipo(tipo: int) -> None:
        if not isinstance(tipo, int) or tipo < 0:
            raise HttpBadRequestError("Tipo deve ser um numero inteiro nao negativo")

    @staticmethod
    def __valida_descricao(descricao: str) -> None:
        if not isinstance(descricao, str) or len(descricao.strip()) == 0:
            raise HttpBadRequestError("Descricao nao pode estar vazia")

    @staticmethod
    def __valida_status(status: int) -> None:
        if not isinstance(status, int) or status not in (1, 2):
            raise HttpBadRequestError("Status deve ser 1 (inativo) ou 2 (ativo)")

    @staticmethod
    def __valida_data_fabricacao(data: date) -> None:

        if isinstance(data, str):
            try:
                data = datetime.strptime(data, "%Y-%m-%d")
            except ValueError:
                raise HttpBadRequestError("Data de fabricacao deve estar no formato YYYY-MM-DD")

        
        if not isinstance(data, date):
            raise HttpBadRequestError("Data de fabricacao deve ser um datetime valido")
        if data > datetime.now():
            raise HttpBadRequestError("Data de fabricaçao não pode estar no futuro")


            

