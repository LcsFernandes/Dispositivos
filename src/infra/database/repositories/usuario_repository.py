from src.data.interfaces.usuario_repository import UsuarioRepositoryInterface 
from src.infra.database.connection.connection_database import DatabaseConnection

class UsuarioRepository(UsuarioRepositoryInterface):
    
    def criar_usuario(self, re: str, nome: str, senha: str):
        with DatabaseConnection() as database_connection:
            query = """ 
                INSERT INTO dw_usuario(re, nome, senha)
                VALUES (?, ?, ?)
                """
            params = (re, nome, senha,)
            try:
                database_connection.execute(query, params)
            except Exception as exception:
                raise exception