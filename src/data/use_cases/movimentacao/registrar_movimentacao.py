from src.infra.database.repositories.movimentacao_repository import MovimentacaoRepository
from src.infra.database.repositories.dispositivo_repository import DispositivoRepository
from src.domain.use_cases.movimentacao.registrar_movimentacao import RegistrarMovimentacao as RegistrarMovimentacaoInterface
from src.domain.entities.movimentacao import Movimentacao
from typing import List, Dict
from datetime import datetime

class RegistrarMovimentacao(RegistrarMovimentacaoInterface):

    def __init__(self, movimentacao_repository: MovimentacaoRepository, dispositivo_repository: DispositivoRepository):
        self.__movimentacao_repository = movimentacao_repository
        self.__dispositivo_repository = dispositivo_repository

    def registrar_movimentacao(self, id_dispositivo: int, local_origem: int, local_destino: int, data_movimentacao: datetime, usuario_id: int, tipo: int):
        pass
    
    def __valida_dispositivo(self, id_dispositivo: int):
        if not id_dispositivo or id_dispositivo < 0:
            raise Exception("id_dispositivo é um campo inteiro positivo obrigatório")
         

        dispositivo = self.__dispositivo_repository.get_dispositivo_by_id(id_dispositivo)
        
        if dispositivo:
            raise Exception(f"Dispositivo id {id_dispositivo} já cadastrado")
    
    def __valida_local(self, local: int):
        if not local:
            raise Exception("local é um campo inteiro positivo obrigatório")

####################### TERMINAR VAGA PARA PODER VALIDAR OS LOCAIS DE ORIGEME  DESTINO        
    def __valida_data_movimentacao(self, data_movimentacao: datetime):
        if not data_movimentacao:
            raise Exception("data_movimentacao é obrigatória")
        if not isinstance(data_movimentacao, datetime):
            raise Exception("data_movimentacao deve ser um datetime válido")
        if data_movimentacao > datetime.now():
            raise Exception("data_movimentacao não pode ser no futuro")

    def __valida_usuario(self, usuario_id: int):
        if not isinstance(usuario_id, int) or usuario_id <= 0:
            raise Exception("usuario_id é um campo inteiro positivo obrigatório")

    def __valida_tipo(self, tipo: int):
        if not isinstance(tipo, int) or tipo <= 0:
            raise Exception("tipo é um campo inteiro positivo obrigatório")