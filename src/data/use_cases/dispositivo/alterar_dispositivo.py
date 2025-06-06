from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.data.dto.dispositivo.alterar_dispositivo_dto import AlterarDispositivoDTO
from src.domain.use_cases.dispositivo.alterar_dispositivo import AlterarDispositivo as AlterarDispositivoInterface 
from datetime import datetime

class AlterarDispositivo(AlterarDispositivoInterface):

    def __init__ (self, dispositivo_repository: DispositivoRepositoryInterface):
        self.__dispositivo_repository = dispositivo_repository

    def alterar_dispositivo(self, dto: AlterarDispositivoDTO) -> None:
        self.__valida_id(dto.id)

        dispositivo = self.__dispositivo_repository.get_dispositivo_by_id(dto.id)
        
        if not dispositivo:
            raise Exception("dispositivo não encontrado")

        if dto.codigo is not None:
            self.__valida_codigo(dto.codigo)
            dispositivo.codigo = dto.codigo

        if dto.tipo is not None:
            self.__valida_tipo(dto.tipo)
            dispositivo.tipo = dto.tipo

        if dto.descricao is not None:
            self.__valida_descricao(dto.descricao)
            dispositivo.descricao = dto.descricao

        if dto.vaga is not None:
            self.__valida_vaga(dto.vaga)
            dispositivo.vaga = dto.vaga

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
            dispositivo.vaga,
            dispositivo.status,
            dispositivo.data_fabricacao,
            dispositivo.cliente
        )

    @staticmethod
    def __valida_id(id: int) -> None:
        if not isinstance(id, int) or id <= 0:
            raise Exception("O ID deve ser um inteiro positivo")

    @staticmethod
    def __valida_codigo(codigo: str) -> None:
        if not isinstance(codigo, str) or len(codigo.strip()) < 3:
            raise Exception("Código deve conter pelo menos 3 caracteres")

    @staticmethod
    def __valida_tipo(tipo: int) -> None:
        if not isinstance(tipo, int) or tipo < 0:
            raise Exception("Tipo deve ser um número inteiro não negativo")

    @staticmethod
    def __valida_descricao(descricao: str) -> None:
        if not isinstance(descricao, str) or len(descricao.strip()) == 0:
            raise Exception("Descrição não pode estar vazia")

    @staticmethod
    def __valida_vaga(vaga: str) -> None:
        if not isinstance(vaga, str) or len(vaga.strip()) == 0:
            raise Exception("Vaga não pode estar vazia")
        if len(vaga.strip()) < 3:
            raise Exception("Vaga invalida")

    @staticmethod
    def __valida_status(status: int) -> None:
        if not isinstance(status, int) or status not in (0, 1):
            raise Exception("Status deve ser 0 (inativo) ou 1 (ativo)")

    @staticmethod
    def __valida_data_fabricacao(data: datetime) -> None:
        if not isinstance(data, datetime):
            raise Exception("Data de fabricação deve ser um datetime válido")
        if data > datetime.now():
            raise Exception("Data de fabricação não pode estar no futuro")


            

