import pytest
import logging
from datetime import datetime
from src.infra.database.repositories.dispositivo_repository import DispositivoRepository
from src.domain.entities.dispositivo import Dispositivo
from src.infra.database.connection.connection_database import DatabaseConnection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="module", autouse=True)
def setup_dw_dispositivos():
    with DatabaseConnection() as db:
        db.connection.autocommit = True
        logger.info("Criando tabela dw_dispositivos para testes...")
        db.execute("""
            IF OBJECT_ID('dw_dispositivos', 'U') IS NULL
            CREATE TABLE dw_dispositivos (
                id INT IDENTITY(1,1) PRIMARY KEY,
                codigo VARCHAR(50) UNIQUE,
                tipo INT,
                descricao VARCHAR(255),
                vaga VARCHAR(50),
                status INT,
                data_fabricacao DATETIME
            );
        """)
        logger.info("Tabela dw_dispositivos criada.")
    yield
    with DatabaseConnection() as db:
        db.connection.autocommit = True
        logger.info("Removendo tabela dw_dispositivos após os testes...")
        db.execute("IF OBJECT_ID('dw_dispositivos', 'U') IS NOT NULL DROP TABLE dw_dispositivos;")
        logger.info("Tabela dw_dispositivos removida.")

@pytest.fixture
def repo():
    return DispositivoRepository()

def test_adicionar_e_get_dispositivo(repo):
    codigo = "TESTE001"
    logger.info(f"Adicionando dispositivo de teste")
    repo.adicionar_dispositivo(
        codigo=codigo,
        tipo=1,
        descricao="Dispositivo de teste",
        vaga="A1",
        status=1,
        data_fabricacao=datetime(2025, 1, 1)
    )
    logger.info("Buscando dispositivo adicionado...")
    dispositivo = repo.get_dispositivo(codigo)
    assert dispositivo is not None
    assert dispositivo.codigo == codigo
    assert dispositivo.tipo == 1
    assert dispositivo.descricao == "Dispositivo de teste"
    assert dispositivo.vaga == "A1"
    assert dispositivo.status == 1
    assert dispositivo.data_fabricacao == datetime(2025, 1, 1)
    logger.info(f"Dispositivo encontrado: {dispositivo}")

def test_get_all_dispositivos(repo):
    logger.info("Adicionando múltiplos dispositivos para o teste de listagem...")
    dispositivos_para_inserir = [
        ("TESTE001", 1, "Dispositivo 1", "A1", 1, datetime(2025, 1, 1)),
        ("TESTE002", 2, "Dispositivo 2", "A2", 1, datetime(2025, 2, 1)),
        ("TESTE003", 1, "Dispositivo 3", "A3", 0, datetime(2025, 3, 1)),
        ("TESTE004", 2, "Dispositivo 4", "A4", 1, datetime(2025, 4, 1)),
        ("TESTE005", 1, "Dispositivo 5", "A5", 0, datetime(2025, 5, 1)),
    ]
    for codigo, tipo, descricao, vaga, status, data_fabricacao in dispositivos_para_inserir:
        if repo.get_dispositivo(codigo) is None:
            repo.adicionar_dispositivo(
                codigo=codigo,
                tipo=tipo,
                descricao=descricao,
                vaga=vaga,
                status=status,
                data_fabricacao=data_fabricacao
            )
            logger.info(f"Dispositivo {codigo} adicionado.")

    logger.info("Buscando todos os dispositivos...")
    dispositivos = repo.get_all_dispositivos()
    assert isinstance(dispositivos, list)
    codigos_esperados = {d[0] for d in dispositivos_para_inserir}
    codigos_encontrados = {d.codigo for d in dispositivos}
    assert codigos_esperados.issubset(codigos_encontrados)
    logger.info(f"Total de dispositivos encontrados: {len(dispositivos)}")
    logger.info(f"Códigos encontrados: {codigos_encontrados}")

def test_atualizar_dispositivo(repo):
    dispositivo = repo.get_dispositivo("TESTE001")
    assert dispositivo is not None
    logger.info("Atualizando dispositivo de teste...")
    repo.atualizar_dispositivo(
        id=dispositivo.id,
        codigo="TESTE001",
        tipo=2,
        descricao="Atualizado",
        vaga="B2",
        status=0,
        data_fabricacao=datetime(2025, 1, 1)
    )
    atualizado = repo.get_dispositivo("TESTE001")
    assert atualizado.tipo == 2
    assert atualizado.descricao == "Atualizado"
    assert atualizado.vaga == "B2"
    assert atualizado.status == 0
    assert atualizado.data_fabricacao == datetime(2025, 1, 1)
    logger.info(f"Dispositivo atualizado: {atualizado}")

def test_verificar_status_dispositivo(repo):
    logger.info("Verificando status do dispositivo (esperado False)...")
    assert repo.verificar_status_dispositivo("TESTE001") is False
    logger.info("Atualizando status do dispositivo para 1...")
    repo.atualizar_dispositivo(
        id=repo.get_dispositivo("TESTE001").id,
        codigo="TESTE001",
        tipo=2,
        descricao="Atualizado",
        vaga="B2",
        status=1,
        data_fabricacao=datetime(2025, 1, 1)
    )
    logger.info("Verificando status do dispositivo (esperado True)...")
    assert repo.verificar_status_dispositivo("TESTE001") is True

def test_excluir_dispositivo(repo):
    logger.info("Excluindo dispositivo de teste...")
    repo.excluir_dispositivo("TESTE001")
    assert repo.get_dispositivo("TESTE001") is None
    logger.info("Dispositivo excluído com sucesso.")