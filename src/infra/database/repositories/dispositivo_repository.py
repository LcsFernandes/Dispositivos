from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.infra.database.connection.connection_database import DatabaseConnection
from src.domain.entities.dispositivo import Dispositivo
from datetime import datetime
from typing import List


class DispositivoRepository(DispositivoRepositoryInterface):
    
    def get_dispositivo_by_codigo(self, codigo: str) -> Dispositivo:
        with DatabaseConnection() as database_connection:
            query = """ 
                SELECT id, codigo, tipo, descricao, status, data_fabricacao, cliente
                FROM dw_dispositivos
                WHERE codigo = ?;
                """
            params = (codigo,)
            try:
                database_connection.execute(query, params)
                result = database_connection.fetchone()
                if result:
                    return Dispositivo(*result)
                return None
            except Exception as exception:
                raise exception
            
    def get_dispositivo_by_id(self, id: int) -> Dispositivo:
        with DatabaseConnection() as database_connection:
            query = """ 
                SELECT id, codigo, tipo, descricao, status, data_fabricacao, cliente
                FROM dw_dispositivos
                WHERE id = ?;
                """
            params = (id,)
            try:
                database_connection.execute(query, params)
                result = database_connection.fetchone()
                if result:
                    return Dispositivo(*result)
                return None
            except Exception as exception:
                raise exception
            
    def get_all_dispositivos(self) -> List[Dispositivo]:
        with DatabaseConnection() as database_connection:
            query = """ 
                SELECT id, codigo, tipo, descricao, status, data_fabricacao, cliente
                FROM dw_dispositivos;
                """
            try:
                database_connection.execute(query)
                results = database_connection.fetchall()
                return [Dispositivo(*item) for item in results] if results else []
            except Exception as exception:
                raise exception

   
    def adicionar_dispositivo(self, codigo: str, tipo: int, descricao: str, status: int, data_fabricacao: datetime, cliente: str) -> None:
        with DatabaseConnection() as database_connection:
            query = """ 
                INSERT INTO dw_dispositivos (codigo, tipo, descricao, status, data_fabricacao, cliente)
                VALUES (?, ?, ?, ?, ?, ?)
                """
            params = (codigo, tipo, descricao, status, data_fabricacao, cliente)
            try:
                database_connection.execute(query, params)
            except Exception as exception:
                raise exception

    
    def atualizar_dispositivo(self, id: int, codigo: str, tipo: int, descricao: str, status: int, data_fabricacao: datetime, cliente: str) -> None:
        with DatabaseConnection() as database_connection:
            query = """ 
                    UPDATE dw_dispositivos
                    SET codigo = ?, tipo = ?, descricao = ?, status = ?, data_fabricacao = ?, cliente = ?
                    WHERE id = ?
                """
            params = (codigo, tipo, descricao, status, data_fabricacao, cliente, id,)
            try:
                database_connection.execute(query, params)
            except Exception as exception:
                raise exception

    
    def excluir_dispositivo(self, codigo: str) -> None:
        with DatabaseConnection() as database_connection:
            query = """ 
                DELETE FROM dw_dispositivos
                WHERE codigo = ?
                """
            params = (codigo,)
            try:
                database_connection.execute(query, params)
            except Exception as exception:
                raise exception

    
    def verificar_status_dispositivo(self, codigo: str):
        with DatabaseConnection() as database_connection:
            query = """ 
                SELECT status.nome
                FROM dw_dispositivos dispositivos
                INNER JOIN dw_status_dispositivo status
                ON  status.id = dispositivos.status
                WHERE codigo = ?;"""
            params = (codigo,)
            try:
                database_connection.execute(query, params)
                result = database_connection.fetchone()
                return result
            except Exception as exception:
                raise exception
            
    
    
    def buscar_posicao_dispositivo(self, codigo: str):
        with DatabaseConnection() as database_connection:
            query = """ 
                SELECT TOP(1) dispositivo.codigo AS dispositivo, vaga.identificacao AS vaga
                FROM dw_movimentacao_dispositivo movimentacao
                INNER JOIN dw_dispositivos dispositivo
                    ON movimentacao.id_dispositivo = dispositivo.id
                INNER JOIN dw_vaga vaga
                    ON movimentacao.local_destino = vaga.id
                WHERE dispositivo.codigo = ?
                ORDER BY movimentacao.data_movimentacao DESC
                """
            params = (codigo,)
            try:
                database_connection.execute(query, params)
                result = database_connection.fetchone()
                return result
            except Exception as exception:
                raise exception