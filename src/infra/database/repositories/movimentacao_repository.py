from src.data.interfaces.movimentacao_repository import MovimentacaoRepositoryInterface
from src.infra.database.connection.connection_database import DatabaseConnection
from src.domain.entities.movimentacao import Movimentacao
from typing import List
from datetime import datetime

class MovimentacaoRepository(MovimentacaoRepositoryInterface):

    
    def get_movimentacao(self, id_dispositivo: int) -> List[Movimentacao]:
        with DatabaseConnection() as database_connection:
            query = """ 
                SELECT id, id_dispositivo, local_origem, local_destino, data_movimentacao, usuario_id, tipo
                FROM dw_movimentacao_dispositivo
                WHERE id_dispositivo = ?;
                """
            params = (id_dispositivo,)
            try:
                database_connection.execute(query, params)
                result = database_connection.fetchone()

                if result:
                    return Movimentacao(*result)
                return None
            except Exception as exception:
                raise exception

    
    def get_all_movimentacoes(self) -> List[Movimentacao]:
        with DatabaseConnection() as database_connection:
            query = """ 
                SELECT id, id_dispositivo, local_origem, local_destino, data_movimentacao, usuario_id, tipo
                FROM dw_movimentacao_dispositivo;
                """
            try:
                database_connection.execute(query)
                results = database_connection.fetchall()
                return [Movimentacao(*item) for item in results] if results else []
            except Exception as exception:
                raise exception

    
    def registrar_movimentacao(self, id_dispositivo: int, local_origem: int, local_destino: int, data_movimentacao: datetime, usuario_id: int, tipo: int) -> None:
        with DatabaseConnection() as database_connection:
            query = """
                INSERT INTO dw_movimentacao_dispositivo (id_dispositivo, local_origem, local_destino, data_movimentacao, usuario_id, tipo)
                VALUES (?, ?, ?, ?, ?, ?);
                """
            params = (id_dispositivo, local_origem, local_destino, data_movimentacao, usuario_id, tipo)
            try:
                database_connection.execute(query, params)
            except Exception as exception:
                raise exception
