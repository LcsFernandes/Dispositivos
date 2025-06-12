import pytest
import logging
from src.data.use_cases.vaga.buscar_vaga_by_id import BuscarVagaById

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FakeVaga:
    def __init__(self, id, deposito_id, identificacao):
        self.id = id
        self.deposito_id = deposito_id
        self.identificacao = identificacao

class FakeVagaRepository:
    def __init__(self, vagas=None):
        self.vagas = vagas or []

    def get_vaga_by_id(self, id):
        logger.info(f"Fake get_vaga_by_id chamado: id={id}")
        for vaga in self.vagas:
            if vaga.id == id:
                return vaga
        return None

def test_buscar_vaga_by_id_sucesso():
    logger.info("Iniciando teste: test_buscar_vaga_by_id_sucesso")
    vaga = FakeVaga(id=1, deposito_id=74, identificacao="A12")
    repo = FakeVagaRepository([vaga])
    use_case = BuscarVagaById(repo)
    result = use_case.buscar_vaga_by_id(1)
    assert result == {
        "type": "Vaga",
        "data": {
            "id": 1,
            "deposito_id": 74,
            "identificacao": "A12"
        }
    }

@pytest.mark.parametrize("id", [None, "abc", -1])
def test_buscar_vaga_by_id_invalido(id):
    repo = FakeVagaRepository()
    use_case = BuscarVagaById(repo)
    with pytest.raises(Exception) as excinfo:
        use_case.buscar_vaga_by_id(id)
    assert "id da vaga é um campo obrigatorio" in str(excinfo.value) or \
           "o id é um campo obrigatorio inteiro positivo" in str(excinfo.value)

def test_buscar_vaga_by_id_nao_encontrada():
    repo = FakeVagaRepository([])
    use_case = BuscarVagaById(repo)
    result = use_case.buscar_vaga_by_id(999)
    assert result is None