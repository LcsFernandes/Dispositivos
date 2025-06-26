from src.data.interfaces.vaga_repository import VagaRepositoryInterface
from src.infra.database.connection.connection_database import DatabaseConnection
from src.domain.entities.vaga import Vaga
from typing import List

class VagaRepository(VagaRepositoryInterface):

    def get_vaga_by_identificacao(self, identificacao: str) -> Vaga:
        with DatabaseConnection() as database_connection:
            query = """ 
                SELECT id, identificacao
                FROM dw_vaga_dispositivo
                WHERE identificacao = ?;
                """
            params = (identificacao,)
            try:
                database_connection.execute(query, params)
                result = database_connection.fetchone()

                if result:
                    return Vaga(*result)
                return None
            
            except Exception as exception:
                raise exception
            
    def get_vaga_by_id(self, id: int) -> Vaga:
        with DatabaseConnection() as database_connection:
            query = """ 
                SELECT id, identificacao
                FROM dw_vaga_dispositivo
                WHERE id = ?;
                """
            params = (id,)
            try:
                database_connection.execute(query, params)
                result = database_connection.fetchone()

                if result:
                    return Vaga(*result)
                return None
            
            except Exception as exception:
                raise exception
    
    
    def listar_vagas(self) -> List[Vaga]:
        with DatabaseConnection() as database_connection:
            query = """ 
                SELECT id, identificacao
                FROM dw_vaga_dispositivo
                """
            try:
                database_connection.execute(query)
                results = database_connection.fetchall()

                if results:
                    return [Vaga(*item) for item in results] if results else []
                return None
            
            except Exception as exception:
                raise exception
    
    def inserir_vaga(self, identificacao: str) -> None:
        with DatabaseConnection() as database_connection:
            query = """ 
                INSERT INTO dw_vaga_dispositivo (identificacao)
                VALUES (?);
                """
            params = (identificacao)
            try:
                database_connection.execute(query, params)
            except Exception as exception:
                raise exception

    def atualizar_vaga(self, id: int, identificacao: str) -> None:
        with DatabaseConnection() as database_connection:
            query = """ 
                UPDATE dw_vaga_dispositivo 
                SET identificacao = ? 
                WHERE id = ?;
                """
            params = (identificacao, id,)
            try:
                database_connection.execute(query, params)
            except Exception as exception:
                raise exception
    