import pytest
import logging
from src.infra.database.repositories.vaga_repository import VagaRepository
from src.domain.entities.vaga import Vaga
from src.infra.database.connection.connection_database import DatabaseConnection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="module", autouse=True)
def setup_dw_vaga():    
    with DatabaseConnection() as db:
        db.connection.autocommit = True
        logger.info("Criando tabela dw_vagas para testes...")
        db.execute("""
            IF OBJECT_ID('dw_vagas', 'U') IS NULL
            CREATE TABLE dw_vagas (
                id INT IDENTITY(1,1) PRIMARY KEY,
                deposito_id INT NOT NULL,
                identificacao VARCHAR(50) NOT NULL UNIQUE
            );
        """)
        logger.info("Tabela dw_vaga criada.")
    yield
    with DatabaseConnection() as db:
        db.connection.autocommit = True
        logger.info("Removendo tabela dw_vaga após os testes...")
        db.execute("IF OBJECT_ID('dw_vagas', 'U') IS NOT NULL DROP TABLE dw_vagas;")
        logger.info("Tabela dw_vaga removida.")

@pytest.fixture
def repo():
    return VagaRepository()

def test_inserir_e_get_vaga(repo):
    logger.info("Inserindo vaga de teste...")
    repo.inserir_vaga(deposito_id=1, identificacao="VAGA001")
    logger.info("Buscando vaga por identificação...")
    vaga = repo.get_vaga("VAGA001")
    assert vaga is not None
    assert vaga.deposito_id == 1
    assert vaga.identificacao == "VAGA001"
    logger.info(f"Vaga encontrada: {vaga}")

def test_listar_vagas(repo):
    logger.info("Listando todas as vagas...")
    vagas = repo.listar_vagas()
    assert isinstance(vagas, list)
    assert any(v.identificacao == "VAGA001" for v in vagas)
    logger.info(f"Total de vagas encontradas: {len(vagas)}")

def test_atualizar_vaga(repo):
    logger.info("Buscando vaga para atualizar...")
    vaga = repo.get_vaga("VAGA001")
    assert vaga is not None
    logger.info("Atualizando vaga...")
    repo.atualizar_vaga(id=vaga.id, deposito_id=2, identificacao="VAGA001-EDITADA")
    vaga_atualizada = repo.get_vaga("VAGA001-EDITADA")
    assert vaga_atualizada.deposito_id == 2
    assert vaga_atualizada.identificacao == "VAGA001-EDITADA"
    logger.info(f"Vaga atualizada: {vaga_atualizada}")