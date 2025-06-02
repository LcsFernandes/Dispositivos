from src.infra.database.connection.connection_database import DatabaseConnection
import pytest
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def db_setup():
    
    with DatabaseConnection() as db:
        db.connection.autocommit = True
        db.execute("""
            IF OBJECT_ID('test_table', 'U') IS NULL
            CREATE TABLE test_table (
                id INT IDENTITY(1,1) PRIMARY KEY,
                name VARCHAR(50)
            );
        """)
    yield

    with DatabaseConnection() as db:
        db.connection.autocommit = True
        db.execute("IF OBJECT_ID('test_table', 'U') IS NOT NULL DROP TABLE test_table;")

def test_connection(db_setup):
    try:
        with DatabaseConnection() as db:
            assert db is not None
            logger.info("Conexão estabelecida com sucesso.")
    except Exception as e:
        pytest.fail(f"Erro de conexão: {e}")


def test_execute_insert_and_fetchone(db_setup):
    try:
        with DatabaseConnection() as db:
            db.execute("INSERT INTO test_table (name) VALUES (?);", ("Teste1",))
            db.execute("SELECT name FROM test_table WHERE name = ?;", ("Teste1",))
            result = db.fetchone()
            logger.info(f"fetchone result: {result}")
            assert result[0] == "Teste1"
    except Exception as e:
        pytest.fail(f"Erro no insert ou fetchone: {e}")

def test_execute_multiple_and_fetchall(db_setup):
    try:
        with DatabaseConnection() as db:
            db.execute("INSERT INTO test_table (name) VALUES (?), (?);", ("Teste2", "Teste3"))
            db.execute("SELECT name FROM test_table ORDER BY id;")
            results = db.fetchall()
            logger.info(f"fetchall results: {results}")
            assert len(results) == 2
    except Exception as e:
        pytest.fail(f"Erro no insert múltiplo ou fetchall: {e}")


def test_execute_with_invalid_query(db_setup):
    with pytest.raises(Exception) as exc_info:
        with DatabaseConnection() as db:
            db.execute("INVALID SQL STATEMENT;")
    logger.info(f"Erro esperado capturado: {exc_info.value}")


@pytest.mark.parametrize(
    "name_value", 
    [
        ("Testando",),
        ("Passando",),
        ("Parametros",)
    ]
)

def test_insert_with_params(db_setup, name_value):
    with DatabaseConnection() as db:
        insert_query = "INSERT INTO test_table (name) VALUES (?);"
        db.execute(insert_query, name_value)
        logger.info(f"Valor inserido: {name_value[0]}")

        db.execute("SELECT name FROM test_table WHERE name = ?;", name_value)
        result = db.fetchone()

        assert result is not None
        assert result[0] == name_value[0]
        logger.info(f"Valor inserido e recuperado: {result[0]}")

