from src.data.interfaces.movimentacao_repository import MovimentacaoRepositoryInterface
from src.infra.database.connection.connection_database import DatabaseConnection
from src.domain.entities.movimentacao import Movimentacao
from typing import List
from datetime import datetime

class MovimentacaoRepository(MovimentacaoRepositoryInterface):

    
    def get_movimentacao_por_dispositivo(self, codigo: str) -> List[Movimentacao]:
        with DatabaseConnection() as database_connection:
            query = """ 
                SELECT TOP(50) movimentacao_dispositivo.id, dispositivo.codigo, vaga.identificacao AS local_origem, vaga2.identificacao AS local_destino, movimentacao_dispositivo.data_movimentacao, movimentacao_dispositivo.login_id
                FROM dw_movimentacao_dispositivo movimentacao_dispositivo
                INNER JOIN dw_vaga vaga
                ON movimentacao_dispositivo.local_origem = vaga.id
                INNER JOIN dw_vaga vaga2
                ON movimentacao_dispositivo.local_destino = vaga2.id
                INNER JOIN dw_dispositivos dispositivo
                ON movimentacao_dispositivo.id_dispositivo = dispositivo.id
                WHERE dispositivo.codigo = ?;
                """
            params = (codigo,)
            try:
                database_connection.execute(query, params)
                results = database_connection.fetchall()

                return [Movimentacao(*item) for item in results] if results else []
            except Exception as exception:
                raise exception

    
    def get_all_movimentacoes(self) -> List[Movimentacao]:
        with DatabaseConnection() as database_connection:
            query = """ 
                SELECT id, id_dispositivo, local_origem, local_destino, data_movimentacao, login_id
                FROM dw_movimentacao_dispositivo;
                """
            try:
                database_connection.execute(query)
                results = database_connection.fetchall()
                return [Movimentacao(*item) for item in results] if results else []
            except Exception as exception:
                raise exception

    
    def registrar_movimentacao(self, id_dispositivo: int, local_origem: int, local_destino: int, data_movimentacao: datetime, login_id: int) -> None:
        with DatabaseConnection() as database_connection:
            query = """
                INSERT INTO dw_movimentacao_dispositivo (id_dispositivo, local_origem, local_destino, data_movimentacao, login_id)
                VALUES (?, ?, ?, ?, ?);
                """
            params = (id_dispositivo, local_origem, local_destino, data_movimentacao, login_id)
            try:
                database_connection.execute(query, params)
            except Exception as exception:
                raise exception
