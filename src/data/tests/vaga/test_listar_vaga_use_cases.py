import pytest
import logging
from src.data.use_cases.vaga.listar_vaga import ListarVaga

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FakeVaga:
    def __init__(self, id, deposito_id, identificacao):
        self.id = id
        self.deposito_id = deposito_id
        self.identificacao = identificacao

class FakeVagaRepository:
    def __init__(self, vagas=None):
        self._vagas = vagas or []

    def listar_vagas(self):
        logger.info("Fake listar_vagas chamado")
        return self._vagas

def test_listar_vaga_sucesso():
    logger.info("Iniciando teste: test_listar_vaga_sucesso")
    vagas = [
        FakeVaga(id=1, deposito_id=74, identificacao="A12"),
        FakeVaga(id=2, deposito_id=74, identificacao="B13"),
        FakeVaga(id=3, deposito_id=74, identificacao="C14"),
    ]
    repo = FakeVagaRepository(vagas)
    use_case = ListarVaga(repo)
    result = use_case.listar_vagas()
    assert result["type"] == "Vaga"
    assert len(result["data"]) == 3
    esperado = [
        {"id": 1, "deposito_id": 74, "identificacao": "A12"},
        {"id": 2, "deposito_id": 74, "identificacao": "B13"},
        {"id": 3, "deposito_id": 74, "identificacao": "C14"},
    ]
    for i, vaga in enumerate(result["data"]):
        for campo in esperado[i]:
            assert vaga[campo] == esperado[i][campo], f"Falha no campo {campo} da vaga {i+1}"

def test_listar_vaga_vazio():
    logger.info("Iniciando teste: test_listar_vaga_vazio")
    repo = FakeVagaRepository([])
    use_case = ListarVaga(repo)
    result = use_case.listar_vagas()
    assert result is None