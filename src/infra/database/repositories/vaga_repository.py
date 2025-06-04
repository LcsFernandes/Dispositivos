from src.data.interfaces.vaga_repository import VagaRepositoryInterface
from src.infra.database.connection.connection_database import DatabaseConnection
from src.domain.entities.vaga import Vaga
from typing import List

class VagaRepository(VagaRepositoryInterface):

    def get_vaga(self, identificacao: str) -> Vaga:
        with DatabaseConnection() as database_connection:
            query = """ 
                SELECT id, deposito_id, identificacao
                FROM dw_vaga
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
    
    def listar_vagas(self) -> List[Vaga]:
        with DatabaseConnection() as database_connection:
            query = """ 
                SELECT id, deposito_id, identificacao
                FROM dw_vaga
                """
            try:
                database_connection.execute(query)
                results = database_connection.fetchall()

                if results:
                    return [Vaga(*item) for item in results] if results else []
                return None
            
            except Exception as exception:
                raise exception
    
    def inserir_vaga(self, deposito_id: int, identificacao: str) -> None:
        with DatabaseConnection() as database_connection:
            query = """ 
                INSERT INTO dw_vaga (deposito_id, identificacao)
                VALUES (?, ?);
                """
            params = (deposito_id, identificacao)
            try:
                database_connection.execute(query, params)
            except Exception as exception:
                raise exception

    def atualizar_vaga(self, id: int, deposito_id: int, identificacao: str) -> None:
        with DatabaseConnection() as database_connection:
            query = """ 
                UPDATE dw_vaga 
                SET deposito_id = ?, identificacao = ? 
                WHERE id = ?;
                """
            params = (deposito_id, identificacao, id,)
            try:
                database_connection.execute(query, params)
            except Exception as exception:
                raise exception
    