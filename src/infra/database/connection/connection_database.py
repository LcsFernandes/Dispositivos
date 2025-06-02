import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DRIVER = os.getenv("DB_DRIVER")

class DatabaseConnection:
    def __init__(self):
        self.__host = DB_HOST
        self.__database = DB_DATABASE
        self.__user = DB_USER
        self.__password = DB_PASSWORD
        self.__driver = DB_DRIVER
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            connectionString = f'DRIVER={self.__driver};SERVER={self.__host};DATABASE={self.__database};UID={self.__user};PWD={self.__password}'
            self.connection = pyodbc.connect(connectionString)
            self.cursor = self.connection.cursor()
            return self.cursor
        except Exception as e:
            raise Exception(f"Erro ao conectar no banco de dados: {e}")
        
    def execute(self, query: str, params: tuple = None):
        try:
            if params is None:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, params)
            
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise Exception(f"Erro ao executar a query: {e}")

    def fetchone(self):
        if self.cursor:
            return self.cursor.fetchone()

    def fetchall(self):
        if self.cursor:
            return self.cursor.fetchall()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

