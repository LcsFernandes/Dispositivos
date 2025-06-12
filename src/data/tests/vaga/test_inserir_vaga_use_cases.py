import pytest
import logging
from src.data.use_cases.vaga.inserir_vaga import InserirVaga

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
        self.inserido = False
        self.args = None

    def inserir_vaga(self, deposito_id, identificacao):
        logger.info(f"Fake inserir_vaga chamado: deposito_id={deposito_id}, identificacao={identificacao}")
        self.inserido = True
        self.args = (deposito_id, identificacao)

    def get_vaga_by_identificacao(self, identificacao):
        logger.info(f"Fake get_vaga_by_identificacao chamado: identificacao={identificacao}")
        for vaga in self.vagas:
            if vaga.identificacao == identificacao:
                return vaga
        return None

def test_inserir_vaga_sucesso():
    logger.info("Iniciando teste: test_inserir_vaga_sucesso")
    repo = FakeVagaRepository([])
    use_case = InserirVaga(repo)
    use_case.inserir_vaga(deposito_id=74, identificacao="A12")
    assert repo.inserido is True
    assert repo.args == (74, "A12")

@pytest.mark.parametrize("deposito_id", [None, "abc", -1, 0])
def test_inserir_vaga_deposito_id_invalido(deposito_id):
    repo = FakeVagaRepository([])
    use_case = InserirVaga(repo)
    with pytest.raises(Exception) as excinfo:
        use_case.inserir_vaga(deposito_id=deposito_id, identificacao="A12")
    assert "o deposito_id é um campo obrigatorio inteiro positivo" in str(excinfo.value)

def test_inserir_vaga_deposito_id_errado():
    repo = FakeVagaRepository([])
    use_case = InserirVaga(repo)
    with pytest.raises(Exception) as excinfo:
        use_case.inserir_vaga(deposito_id=99, identificacao="A12")
    assert "deposito_id informado nao pertence ao armazem de dispositivos" in str(excinfo.value)

@pytest.mark.parametrize("identificacao", [None, "", "A"])
def test_inserir_vaga_identificacao_invalida(identificacao):
    repo = FakeVagaRepository([])
    use_case = InserirVaga(repo)
    with pytest.raises(Exception) as excinfo:
        use_case.inserir_vaga(deposito_id=74, identificacao=identificacao)
    assert "identificacao da vaga é um campo obrigatorio" in str(excinfo.value) or \
           "Nome de identificacao para vaga invalido" in str(excinfo.value)

def test_inserir_vaga_identificacao_duplicada():
    vaga_existente = FakeVaga(id=1, deposito_id=74, identificacao="A12")
    repo = FakeVagaRepository([vaga_existente])
    use_case = InserirVaga(repo)
    with pytest.raises(Exception) as excinfo:
        use_case.inserir_vaga(deposito_id=74, identificacao="A12")
    assert "A vaga com a identificacao A12 ja esta cadastrada" in str(excinfo.value)