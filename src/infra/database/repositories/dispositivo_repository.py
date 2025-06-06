from src.data.interfaces.dispositivo_repository import DispositivoRepositoryInterface
from src.infra.database.connection.connection_database import DatabaseConnection
from src.domain.entities.dispositivo import Dispositivo
from datetime import datetime
from typing import List


class DispositivoRepository(DispositivoRepositoryInterface):
    
    def get_dispositivo_by_codigo(self, codigo: str) -> Dispositivo:
        with DatabaseConnection() as database_connection:
            query = """ 
                SELECT id, codigo, tipo, descricao, vaga, status, data_fabricacao
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
                SELECT id, codigo, tipo, descricao, vaga, status, data_fabricacao, cliente
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
                SELECT id, codigo, tipo, descricao, vaga, status, data_fabricacao
                FROM dw_dispositivos;
                """
            try:
                database_connection.execute(query)
                results = database_connection.fetchall()
                return [Dispositivo(*item) for item in results] if results else []
            except Exception as exception:
                raise exception

   
    def adicionar_dispositivo(self, codigo: str, tipo: int, descricao: str, vaga: str, status: int, data_fabricacao: datetime) -> None:
        with DatabaseConnection() as database_connection:
            query = """ 
                INSERT INTO dw_dispositivos (codigo, tipo, descricao, vaga, status, data_fabricacao)
                VALUES (?, ?, ?, ?, ?, ?)
                """
            params = (codigo, tipo, descricao, vaga, status, data_fabricacao,)
            try:
                database_connection.execute(query, params)
            except Exception as exception:
                raise exception

    
    def atualizar_dispositivo(self, id: int, codigo: str, tipo: int, descricao: str, vaga: str, status: int, data_fabricacao: datetime) -> None:
        with DatabaseConnection() as database_connection:
            query = """ 
                UPDATE dw_dispositivos
                SET codigo = ?, tipo = ?, descricao = ?, vaga = ?, status = ?, data_fabricacao = ?
                WHERE id = ?
                """
            params = (codigo, tipo, descricao, vaga, status, data_fabricacao, id,)
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

    
    def verificar_status_dispositivo(self, codigo: str) -> bool:
        with DatabaseConnection() as database_connection:
            query = """ 
                SELECT status
                FROM dw_dispositivos
                WHERE codigo = ?;"""
            params = (codigo,)
            try:
                database_connection.execute(query, params)
                result = database_connection.fetchone()
                
                if result is not None and result[0] == 1:
                    return True
                
                return False
                
            except Exception as exception:
                raise exception