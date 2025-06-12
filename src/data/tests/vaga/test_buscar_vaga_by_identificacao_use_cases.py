import pytest
import logging
from src.data.use_cases.vaga.buscar_vaga_by_identificacao import BuscarVagaByIdentificacao

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

    def get_vaga_by_identificacao(self, identificacao):
        logger.info(f"Fake get_vaga_by_identificacao chamado: identificacao={identificacao}")
        for vaga in self.vagas:
            if vaga.identificacao == identificacao:
                return vaga
        return None

def test_buscar_vaga_by_identificacao_sucesso():
    logger.info("Iniciando teste: test_buscar_vaga_by_identificacao_sucesso")
    vaga = FakeVaga(id=1, deposito_id=74, identificacao="A12")
    repo = FakeVagaRepository([vaga])
    use_case = BuscarVagaByIdentificacao(repo)
    result = use_case.buscar_vaga_by_identificacao("A12")
    assert result == {
        "type": "Vaga",
        "data": {
            "id": 1,
            "deposito_id": 74,
            "identificacao": "A12"
        }
    }

@pytest.mark.parametrize("identificacao", [None, "", "A"])
def test_buscar_vaga_by_identificacao_invalida(identificacao):
    repo = FakeVagaRepository()
    use_case = BuscarVagaByIdentificacao(repo)
    with pytest.raises(Exception) as excinfo:
        use_case.buscar_vaga_by_identificacao(identificacao)
    assert "identificacao da vaga é um campo obrigatorio" in str(excinfo.value) or \
           "Identificacao incorreta" in str(excinfo.value)

def test_buscar_vaga_by_identificacao_nao_encontrada():
    repo = FakeVagaRepository([])
    use_case = BuscarVagaByIdentificacao(repo)
    result = use_case.buscar_vaga_by_identificacao("ZZZ")
    assert result is None