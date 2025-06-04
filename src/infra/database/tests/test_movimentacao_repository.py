import pytest
import logging
from datetime import datetime
from src.infra.database.repositories.movimentacao_repository import MovimentacaoRepository
from src.domain.entities.movimentacao import Movimentacao
from src.infra.database.connection.connection_database import DatabaseConnection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="module", autouse=True)
def setup_dw_movimentacao_dispositivo():
    with DatabaseConnection() as db:
        db.connection.autocommit = True
        logger.info("Criando tabela dw_movimentacao_dispositivo para testes...")
        db.execute("""
            IF OBJECT_ID('dw_movimentacao_dispositivo', 'U') IS NULL
            CREATE TABLE dw_movimentacao_dispositivo (
                id INT IDENTITY(1,1) PRIMARY KEY,
                id_dispositivo INT,
                local_origem INT,
                local_destino INT,
                data_movimentacao DATETIME,
                usuario_id INT,
                tipo INT
            );
        """)
        logger.info("Tabela dw_movimentacao_dispositivo criada.")
    yield
    with DatabaseConnection() as db:
        db.connection.autocommit = True
        logger.info("Removendo tabela dw_movimentacao_dispositivo após os testes...")
        db.execute("IF OBJECT_ID('dw_movimentacao_dispositivo', 'U') IS NOT NULL DROP TABLE dw_movimentacao_dispositivo;")
        logger.info("Tabela dw_movimentacao_dispositivo removida.")

@pytest.fixture
def repo():
    return MovimentacaoRepository()

def test_registrar_e_get_movimentacao(repo):
    logger.info("Registrando movimentação de teste...")
    repo.registrar_movimentacao(
        id_dispositivo=1,
        local_origem=10,
        local_destino=20,
        data_movimentacao=datetime(2025, 1, 1, 12, 0, 0),
        usuario_id=100,
        tipo=1
    )
    logger.info("Buscando movimentação registrada...")
    
    movimentacoes = repo.get_all_movimentacoes()
    assert len(movimentacoes) == 1
    mov = movimentacoes[-1]
    logger.info(f"Movimentação encontrada: {mov}")
    assert mov.id_dispositivo == 1
    assert mov.local_origem == 10
    assert mov.local_destino == 20
    assert mov.data_movimentacao == datetime(2025, 1, 1, 12, 0, 0)
    assert mov.usuario_id == 100
    assert mov.tipo == 1

def test_get_movimentacao_por_dispositivo(repo):
    logger.info("Buscando movimentação por id_dispositivo...")
    movimentacoes = repo.get_all_movimentacoes()
    assert len(movimentacoes) > 0
    id_dispositivo = movimentacoes[-1].id_dispositivo
    mov = repo.get_movimentacao_por_dispositivo(id_dispositivo)
    assert mov is not None
    logger.info(f"Movimentação por dispositivo retornada: {mov}")
    assert mov.id_dispositivo == id_dispositivo